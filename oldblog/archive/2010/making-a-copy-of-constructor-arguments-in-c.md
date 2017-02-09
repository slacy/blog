Title: Making a copy of constructor arguments in C++
Date: 2010-05-20 13:12
Author: slacy
Category: General
Tags: c++, pointers, python interface, refcounting, string
Status: published

Okay, maybe my C++ is getting rusty, but I'm stammering at coming up
with a reasonable solution to this problem:

Imagine a class, like this one:

    class Foo {
      public:
        Foo(string &name) : name_(name.c_str()) { }
      private:
        char *name_;
    }

As you can see, it takes the guts of the string argument passed to the
constructor, and stores them internally. In other words, it assumes that
the caller is going to manage the lifetime of the string argument so
that it lives at least as long as the instance of Foo. Ignore that this
might be horribly bad style for a second, and pretend that this is an
external class that you want to interface with. What I want to be able
to do is this:

    Foo f = Foo(string("foo"));

But, of course, that will totally crash. So, I'd like to write a wrapper
class, that looks like this:

    class FooWrapper : public Foo {
      public:
        FooWrapper(string &name) :
            Foo(make_a_copy(name, name_copy_)) { } 

        string &make_a_copy(string &src, string &dest) {
            dest = src;
            return dest;
        }

      private:
        string name_copy_;
    }

But here's the problem: The code in make\_a\_copy() crashes because the
guts of the string representation stored in name\_copy\_ is total
garbage and not initialized to a reasonable state yet. I could create a
factory function and add some yucky methods to FooWrapper, but I'd
really rather not. Is there an easier way to accomplish this "copy on
construct" behavior?
