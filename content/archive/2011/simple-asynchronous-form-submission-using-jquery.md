Title: Simple asynchronous form submission using jQuery
Date: 2011-03-18 15:26
Author: slacy
Category: General
Tags: ajax, asynchronous form post, dialog, forms, html, jquery, post
Status: published

It's not hard to submit a form asynchronously in jQuery. Here's a little
example. I put a block like this right below my form element.

    <script type="text/javascript">
    $("#my_form").submit(function() {
        $.ajax({
            type: "POST",
            url: "/path/to/post/handler/",
            data: $("#my_form").serializeArray(),
            success: function() {
                // Whatever you want here, like close dialog box, etc. 
            }
            });
        return false;
    });</script>

I did have to be careful to make the form like this:

    <form action="javascript:true;">...
