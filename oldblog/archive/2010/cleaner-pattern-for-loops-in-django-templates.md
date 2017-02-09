Title: Cleaner pattern for  loops in Django templates?
Date: 2010-10-21 14:26
Author: slacy
Category: General
Tags: django, html, templates
Status: published

I find myself typing stuff like this a lot:

    {% for item in list %}
      {% if forloop.first %}<ul>{% endif %}
      <li>{{ item.value }}</li>
      {% if forloop.last %}</ul>{% endif %}
    {% empty %}
      <p>No items in list.</p>
    {% endif %}

Is there a cleaner way to do this? It's a lot of code for creating a
simple loop.  I'm tempted to make a "listloop" class that wraps up all
the ul and li logic right into the templatetag, but that seems like it
hides a lot.
