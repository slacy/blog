Title: Django: Why can't I put newlines inside my {{...}} blocks?
Date: 2010-06-28 09:36
Author: slacy
Category: General
Status: published

Why is this okay:

    {{ variable }}

But this is not:

    {{
    variable
    }}

This totally sucks for long variable names that are indented or have a
long filter after them.  Allow newlines as whitespace inside {{...}}
blocks!
