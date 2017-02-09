Title: Subject Oriented Programming (SOP) vs. Object Oriented Programming (OOP)
Date: 2010-03-22 15:03
Author: slacy
Category: General
Tags: c++, direct object, indirect object, object-oriented, programming, python, subject-oriented
Status: published

When I'm programming, I usually anthroporporphize the code and the
actors involved, and that means when I'm thinking about program flow, I
think of it as if they're real actors doing the tasks needed, and then I
convert that back into code.  But, when reading other people's code, I
often times find it hard to convert back into my internal actor-based
representation.  I realized that this is because the term "Object
Oriented Programming" should likely be called "Subject Oriented
Programming"  I'm using the term Subject the way you use it when
describing English sentence structure.  Take a look at this:

"The boy put the box in the bag."

Just to refresh your grade school English (which I had to do as well),
take a brief look at the [sentence diagramming article on
wikipedia](http://en.wikipedia.org/wiki/Sentence_diagram). Our sentence
above boils down to:

Subject: "The boy"  
Predicate & Direct object: "put the box"  
Indirect object: "in the bag"

How would you represent that in code? Think about it for a second before
continuing. So, here are the possibilities of how this could be written
with a single method call:

    // Subject-Oriented programming:
    // "The boy put the box in the bag"
    boy.PutIn(box, bag);

    // Direct-object oriented programming:
    // "The box was put in the bag by the boy"
    box.PutIn(bag, boy);

    // Indirect-object oriented programming:
    // "The bag, to which was added a box, was done by the boy."  OR
    // "A bag now has a box that was put there by the boy."
    bag.AddTo(box, boy);

So, which is correct via the principles of OOP? What's the correct place
for the method that does the work? Is it on the Subject of the sentence?
The Direct Object? Were you taught how to design this? (i.e. in school?)

In practice, method placement is one of the biggest factors in how
maintainable & testable your code is, and code is rarely as simple as
what I've shown above. How do you figure out where the right place for
your methods are?

One code base where this was thought about a lot was in Python's
handling of string & list methods. The split() and join() methods in
Python are both on the string type. In other words: The list type is
rigid in that its methods contain no string-manipulation. This seems
good at first until you read the code:

    s = "Hello, world"
    # Split the string into a list of "Hello" and "world":
    l = s.split(',')
    # Now, take that resulting list, and join it back together:
    j = ','.join(l)

Wow, that last line looks weird! What's going on there? We're creating a
temporary string "," and then calling the join() method! Weird! For that
last line, I would have much preferred to write:

    j = l.join(',')

To be symmetric with the original splitting code, but to write things
that way would place a string generating method "join()" on the list
class, which also seems wrong.
