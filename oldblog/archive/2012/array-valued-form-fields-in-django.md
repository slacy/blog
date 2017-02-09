Title: Array valued Form fields in Django.
Date: 2012-04-26 12:46
Author: slacy
Category: General
Status: published

So, you want to pass an array of values into a Form in Django.  It's not
exactly obvious what the right solution is. You could read up on
MultiValueField
(<https://docs.djangoproject.com/en/dev/ref/forms/fields/#multivaluefield>)
or you could read about widgets.MultipleHiddenInput
(<https://docs.djangoproject.com/en/dev/ref/forms/widgets/#multiplehiddeninput>)
but you'll realize that neither of these allows for custom validation of
the individual entries.

Here's a generic ArrayField that might be of use:

    class ArrayField(forms.Field):

        def __init__(self, *args, **kwargs):
            self.base_type = kwargs.pop('base_type')
            self.widget = MultipleHiddenInput
            super(ArrayField, self).__init__(*args, **kwargs)

        def clean(self, value):
            for subvalue in value:
                self.base_type.validate(subvalue)

            return [self.base_type.clean(subvalue) for subvalue in value]

Here's the code I'm using to unit test this puppy:

    class TestCharArrayForm(forms.Form):
        multi_char = ArrayField(base_type=forms.CharField(max_length=3))


    class TestArrayField(ExaTestCase):

        def test_array_good(self):
            query_dict = QueryDict('a=1', mutable=True)
            query_dict.setlist('multi_char', ('abc', 'def', 'ghi'))
            test_form = TestCharArrayForm(query_dict)
            self.assertTrue(test_form.is_valid())
            self.assertEqual(test_form.cleaned_data['multi_char'],
                             ['abc', 'def', 'ghi'])

        def test_array_invalid(self):
            query_dict = QueryDict('a=1', mutable=True)
            query_dict.setlist('multi_char', ('abcd' * 10, # too long
                                              'deff' * 10,
                                              '1234' * 10))
            test_form = TestCharArrayForm(query_dict)
            self.assertFalse(test_form.is_valid())

It would be very straightforward to add extra fields on ArrayField to
check for number of items in the array or any other characteristics you
want.
