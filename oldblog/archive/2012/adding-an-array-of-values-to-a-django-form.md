Title: Adding an array of values to a Django form 
Date: 2012-04-25 15:54
Author: slacy
Category: General
Status: published

It's possible to have an array-valued field in a Django Form, it's just
really, really not clear how to do it.

Background: I'm writing a series of REST APIs using a Django backend,
and I like to define the parameters for POST and PUT as Django Forms
objects.  I'm never rendering my Forms as HTML, as they just define the
API.

In some cases, I'd like to pass an array of values.  Let's say, an array
of string tags for a blog post in the POST method that creates a blog
post.  The form for this API would look like this:

    class CreateBlogForm(forms.Form):
        title = forms.CharField(max_length=2000)
        body = forms.CharField()
        tags = forms.CharField(widget=forms.MultipleHiddenInput)

Then, in my View code, I would write a snippet that looked like this:

        blog_form = CreateBlogForm(request.POST)
        if not blog_form.is_valid(): 
            raise Exception("Invalid form")
        blog_data = blog_form.cleaned_data 
        blog = Blog.objects.create(title=blog_data['title'], body=blog_data['body'])
        for tag in blog_data.tags: blog.add_tag(tag)

Note how I'm accessing the tags members as an array? Exactly what I
wanted!
