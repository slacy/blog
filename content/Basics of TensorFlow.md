Title: Basics of TensorFlow
Category: TensorFlow From The Ground Up
Tags: Python, TensorFlow, Jupyter
Date: 1/31/2017 11:00pm 
Author: slacy
  When I first heard about TensorFlow, it was described as a library for doing Machine Learning, which I equated with Neural Networks.  (Neural Networks are just one type of Machine Learning).  

I had read many other blog posts about Neural Network architectures, so I assumed it would have an API that looked something like this:


```python
# Here's What I thought the *core* TensorFlow API might look like, 
# before I had read any code or documentation about it.
network = tf.Network() 
network = network.AddConvolutionalLayer(...)
network = network.AddMaxPoolingLayer(...)
network = network.AddSigmoidActivation(...)
network.Train(data)
```
## Boy, was I wrong!  

The *core* API of TensorFlow is much lower level than what I've shown above!

They do provide highlevel NN abstractions like the one I've shown above, but they are wrapped up in some pretty domain-specific APIs.  Additionally, I'd like to understand what the *lowest level* part of the API is.  Where are the *guts* of TensorFlow and how do they work? 

So, after a little bit of digging, I found some of the lowest level parts.  The APIs revolve around a process that goes like this: 
* Construct some inputs, outputs, and parameters to learn (your "Tensors") 
* Construct a computation graph for what you want to do with your variables. 
* Run an Optimizer to apply one of several different algorithms to compute your hidden parameters. 
* Save models to disk and use them for inferrence in the futrue. 

TensorFlow can be thought of as being most similar to the Python library [SymPy](http://www.sympy.org/en/index.html) or other 
symbolic mathematics packages/languages like R, Matlab or Mathematica.    But, TensorFlow isn't a generic symbolic math package, it's a symbolic math library whose sole purpose is to calculate numeric approximations of functions.  In other words, you can think of it like a "solver" using an algorithm like [Newton's Method](https://en.wikipedia.org/wiki/Newton%27s_method) or [Runge-Kutta](https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_methods), except that it's specifically focused on techniques used in ML: Stochastic Gradient Descent.  

I know that sounds like a lot, and you really don't need to know what all that stuff means!   

When using TensorFlow, what you're doing is setting up 
a [computation graph](https://www.tensorflow.org/get_started/basic_usage#the_computation_graph) for your function(s).  
## Computing y=x^2 using TensorFlow

Let's write a quick example TensorFlow program and see how the simple parts work.  Here, we're going to compute $y=x^2$ using TensorFlow.  This is about as close to "Hello World" as we'll get.


```python
import tensorflow as tf

# TensorFlow Variables are for values used during computation:
x = tf.Variable(dtype=tf.float32, initial_value=2.0, name='x') 

# Even though this looks like native python math, it is not. 
# 'x' is a TensorFlow variable, so "x**2" doesn't just 
# compute a value, it returns a computation graph that computes
# "x^2" for whatever the current value of x is.  
y = x**2

with tf.Session() as sess:
    # There are internal global variables that always need to be initialized, 
    # as well as our own "initial_value=1.0" for 'x'.  
    sess.run([tf.local_variables_initializer(), tf.global_variables_initializer()])
    print "Initial value of x = ", sess.run(x)

    # Now, we can confirm that y=2^2 produces 4.0: 
    print "Initial value of y=x^2 = ", sess.run(y)
    
    # We can't just say "x=5" because that would change the type of x from a 
    # tf.Variable into a native Python float.  We need to create & run a 
    # graph that reassigns the value of x.  
    sess.run(x.assign(5))
    
    # Once we have reassigned x, we can re-compute the 'y' graph. 
    print "5^2 = ", sess.run(y)
```

    Initial value of x =  2.0
    Initial value of y=x^2 =  4.0
    5^2 =  25.0

So, there you have it.  TensorFlow can compute some values, which is not a huge surprise.  The syntax is a bit verbose, but the general program structure I've used above is very common, even in larger systems, so its useful to start out this way. 

Now, on to bigger and better things.  How to we run a Solver?
## Running a solver & finding the minimum of our function

Before we run a solver, we must create a computation graph whose result is a single value that we would like to **minimize**.  Finding values that minimize functions is what TensorFlow is really, really good at. 

Given our $x^2$ example from above, let's just assume that what we want to compute is $\min(x^2)$ so we restate this as "Find me the value of '$x$' that minimizes the function $x^2$" 
 
So, here's the code:


```python
import tensorflow as tf

x = tf.Variable(dtype=tf.float32, initial_value=1.0, name='x')
y = tf.pow(x, 2)

learning_rate = 0.001 
optimizer = tf.train.GradientDescentOptimizer(learning_rate)

with tf.Session() as sess: 
    sess.run(tf.global_variables_initializer())
    sess.run(optimizer.minimize(y))
    print "min x = ", sess.run(x)
```

    min x =  0.998

## Wait, what happened?

We know that the minimum of $x^2$ is at $x=0$ so what happened?  Where did $0.998$ come from, and what's "Learning Rate"? 

Remember, TensorFlow uses GradientDescent, which is an iterative process.  The code above only ran *one iteration* of the algorithm, so only made a small change to the initial value of $x$.  The Good Thing is that it seems to be going in the right direction.  

What it actually computed was:
$$x_1=x_0 -(learning\_rate * \frac{\partial x^2}{\partial x})$$

$learning\_rate = 0.001$, 
the derivative of $x^2$ is $2x$, and 
the initial value of $x$ was $1.0$, that leaves us with:

$$x_1=1.0-0.001*2x$$

Which is exactly 0.998.  Whew!  

What we learned is: 

> With each iteration of an optimizer, TensorFlow takes us one "learning_rate sized step" closer towards 
> the solution we're looking for. 

So, now we can rewrite our solver to iterate many times, and we'll get pretty close to a true solution. 

## A solver that actually "works"


```python
import tensorflow as tf

x = tf.Variable(dtype=tf.float32, initial_value=1.0, name='x')
y = tf.pow(x, 2)

learning_rate = 0.001 
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(y)

with tf.Session() as sess: 
    sess.run(tf.global_variables_initializer())
    
    num_iterations = 10000
    for i in xrange(num_iterations):
        sess.run(optimizer)
        if i % 1000 == 0:
            print "i=",i," x=", sess.run(x)
    print "final x = ", sess.run(x), " y=", sess.run(y)
```

    i= 0  x= 0.998
    i= 1000  x= 0.134794
    i= 2000  x= 0.0182059
    i= 3000  x= 0.00245898
    i= 4000  x= 0.000332121
    i= 5000  x= 4.48577e-05
    i= 6000  x= 6.05868e-06
    i= 7000  x= 8.18312e-07
    i= 8000  x= 1.10525e-07
    i= 9000  x= 1.4928e-08
    final x =  2.02028e-09  y= 4.08155e-18

Well, it *almost* actually works, right? 

Yes, the code above works, and this is *exactly* what you should expect from a numerical solver.  It's going to take a very large number of iterations for the `GradientDescent` alrogithm to reach the exact solution of $x=0$. 
## Conclusion

We have explored the most basic comptation functions of TensorFlow, and we've run a very simple solver to approximate the minimum value of the function $x^2$.  Values to be compted in TensorFlow are stored in **tf.Variable** instances, and the main unit of work is a **computation graph** which is constructed by calling into the core TensorFlow API. 

We've seen that TensorFlow is a numerical solver, and does **not** produce exact results.  We've also shown that it takes a fairly large number of iterations to get to a final result value, for a trivial example using naive Gradient Descent. 
