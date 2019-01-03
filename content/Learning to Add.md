Title: Learning to Add
Category: TensorFlow From The Ground Up
Tags: Python, TensorFlow, Jupyter
Date: 2/8/2017 10:00am 
Author: slacyThis is the **third** post of my series [TensorFlow From The Ground Up]({category}tensorflow-from-the-ground-up).

In this post, we'll explore a toy Neural Network, and show our first Perceptron based code.  This is a simple example to get the thought process going, but will lead us to more insights in coming posts. 

## Introduction

Machine Learning problems can be thought of like this: 

* Define a highly-parameterized generic function of the form: $f(inputs) = outputs$
* Choose some *Training Data* that are example pairs of $(inputs, outputs)$.
* Feed the *Training Data* to an optimizer, which will find values for all the hidden parameters that optimize our *loss function*.
* After training, we can use the computed hidden parameters to *validate* example $(input, output)$ pairs that we did not use during training. 

The power of machine learning is in the design of the computation graph (i.e. "The Neural Network") that determines both the parameters, and also determines the flexibility and "adaptability" of the resulting model.  In other words:

> If we train a model on a collection of input data, does it produce the 
> expected results for data that it has never seen before?  
> 
> How can we choose a Network Design that we know will solve our target function? 

The key insight here is understanding your problem area domain, and "what's possible" versus "what's not possible" in Neural Networks.  We don't yet have this intuition, but we're on our way to building it. 

Once we have this intuition, it will steer our network design decisions, and can help us to debug any issues we have during the training process.  Additionally, it will guide our expectations about what's possible in the problem domain, and may even lead us into new areas of network and node design.  

But as you will see, the idea of a "Neural Network Node" is nothing more than an abstract idea that helps us reason about the computation graph.  There is really no such thing as a "node" in a network -- there is just a collection of parameters, stored as matrices, and a graph that does computations on these matrices. 

With that, let's get coding.
## Let's get concrete!

Everything above is pretty abstract, so let's start with a concrete problem.  Can we learn the function:

$$f(x,y) = x+y$$

Using a Neural Network? 

First, what does it mean to "learn" this function?  It will involve the following steps:

* Design a computation graph.
* Choose some training data, which will be a collection of $(x,y)$ pairs.
* Choose some validation data, which will be a collection of $(x,y)$ pairs that were never used during training. 
* Implement a *Loss function* to determine how correct the values computed are.  This determines the training and accuracy. 
* Write code to implement the graph, train and validate our problem set.

## The Computation Graph

Last time, we talked about TensorFlow ``tf.Variable`` objects, which we used to hold computed values in our graph.  Variables are generally Tensors (i.e. matrices) that hold all the hidden parameters that will be learned by the network. 

In addition to ``Variables``, we need to pass values to our network.  These values can be thought of the *inputs* to our function.  In TensorFlow, these inputs are instances of the type ``tf.placeholder``.  You can think of a ``placeholder`` as a slot where an input value will go, at runtime.  They aren't *learned parameters* like the ``Variable`` instances are. 

In general, ``Variable`` and ``placeholder`` instances behave pretty much the same, except that placeholders are *inputs* and Variables are *stored parameters*.  Variables require an initial value, and Placeholders are fed discrete values at runtime with each training iteration. 

For our learning task, we are going to use a traditional [Perceptron](https://en.wikipedia.org/wiki/Perceptron) based network. Our network will consist of:

* One input layer of our $(x,y)$ values.
* One middle layer of 2 values, computed using the Perceptron function.
* One output value.  

Each node in the middle layer will compute 

$$f(x) = \sum_{i=0}^n {w_i v_i+b_i}$$

The steps of the computation look roughly like this: 

$$\begin{array}{rl}
inputs & = \{x,y\} \\
l_1 & = w_1 x + w_2 y + b_1 \\
l_2 & = w_3 x + w_4 y + b_2 \\
output & = w_5 l_1 + w_6 l_2 + b_3
\end{array}$$

If we expand out the temporaries, we get: 

$$output = w_5 (w_1 x + w_2 y + b_1) + w_6 (w_3 x + w_4 y + b_2) + b_3$$

As you can see, we can easily implement $x+y$ by setting: 

$$\begin{array}{rl}
w_1, w_2, w_5 & = 1.0 \\
w_3, w_4, w_6 & = 0.0 \\
b_i & = 0.0 \\
\end{array}$$


We'll be using TensorFlow's matrix representations to implement these calculations.  All weights and biases shown above are stored as matrices. 


```python
import tensorflow as tf 
import random

# Here are the inputs to our computation Graph.  Note that the expected value 
# f(x,y)=x+y is passed a via a placeholder as well. 
x = tf.placeholder(shape=(1,), dtype=tf.float32, name='x')
y = tf.placeholder(shape=(1,), dtype=tf.float32, name='y')
expected = tf.placeholder(shape=(1,), dtype=tf.float32, name='expected')

# Inputs need to be in the form of a single tensor, so we concatenate and reshape 
# into a form that we can use below. 
inputs = tf.reshape(tf.concat([x,y], 0), (1,2))

# We are constructing a middle layer of 2 perceptron nodes.  Weights and biases 
# are our w_i and v_i from the above equations. 
input_weight = tf.Variable(expected_shape=[2,2], 
                           initial_value=tf.truncated_normal([2,2], mean=0, stddev=0.1))
input_bias = tf.Variable(expected_shape=[1, 2], 
                         initial_value=tf.truncated_normal([1, 2], mean=0, stddev=0.1))

# Our middle layer of "nodes" (can be thought of as just an intermediate value)
# Is an array of size (1,2) and each value is computed from our perceptron function: 
mid_layer = tf.add(tf.matmul(inputs, input_weight), input_bias)

# We're looking for a single output value, so we apply the same perceptron formula 
# to our middle layer, but this time multiplying by a tensor of size (2,1) to produce 
# an output of size (1,1).  We then "squeeze" this value down to a tensor of size (1)
out_weight = tf.Variable(expected_shape=[2,1], 
                         initial_value=tf.truncated_normal([2,1], mean=0, stddev=0.1))
out_bias = tf.Variable(expected_shape=[1, 1], 
                       initial_value=tf.truncated_normal([1,1], mean=0, stddev=0.1))

# Perceptron formula again, and the squeeze to get a single value. 
output = tf.squeeze(tf.add(tf.matmul(mid_layer, out_weight), out_bias))

# Our error function is computed as "Squared Difference" between the computed output
# and the expected value. 
loss = tf.pow(output - expected, 2)

# Learning rate and optimizer similar to our previous examples. 
learning_rate = 0.001
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss)

def f(x,y): return x + y

with tf.Session(config=tf.ConfigProto(log_device_placement=True)) as sess: 
    sess.run([tf.local_variables_initializer(), 
              tf.global_variables_initializer()])
    
    # Training: 
    #
    # Iterate many times with random inputs to "learn" the parameters
    # stored in input_wegiht, input_bias, out_weight, out_bias Variables above.  
    # For this example, we only pass in **even** numbers in the range [0,20]
    # 
    # We will use odd values during our validation phase below to ensure that 
    # we never validate on any of the inputs that were in the training set. 
    print "TRAIN"
    train_iterations = 10000
    for i in xrange(train_iterations):
        ix = [random.randrange(0, 10) * 2,]
        iy = [random.randrange(0, 10) * 2,]
        e = [f(ix[0],iy[0]),]
        _, l = sess.run([optimizer, loss], feed_dict={x:ix, y:iy, expected:e})
        if i % 1000 == 0:
            print "i=",i," loss=", l
            
    # Once we have learned the parameters, we can validate by passing inputs 
    # never seen before.  For this case, we expand the range of our inputs 
    # to include all odd numbers in the range [-40,40].  
    print "VALIDATE"
    validate_iterations = 10
    for i in xrange(validate_iterations):
        ix = [random.randrange(-20, 20) * 2 + 1,]
        iy = [random.randrange(-20, 20) * 2 + 1,]
        e = [f(ix[0], iy[0]),]
        out, l = sess.run([output, loss], feed_dict={x:ix, y:iy, expected:e})
        print "x=",ix[0], " y=",iy[0], " out=", out, " loss=", l
    
    # Print out the computed weights and bisaes for inspection. 
    print sess.run([input_weight, input_bias, out_weight, out_bias])
```

    TRAIN
    i= 0  loss= [ 32.81954193]
    i= 1000  loss= [ 0.01804398]
    i= 2000  loss= [ 0.00302923]
    i= 3000  loss= [  1.86966245e-05]
    i= 4000  loss= [ 0.00014678]
    i= 5000  loss= [  1.73764784e-05]
    i= 6000  loss= [  1.85982572e-06]
    i= 7000  loss= [  1.63308869e-08]
    i= 8000  loss= [  1.06378138e-07]
    i= 9000  loss= [  6.57109922e-09]
    VALIDATE
    x= 3  y= -11  out= -7.9998  loss= [  3.93483788e-08]
    x= 23  y= -19  out= 4.00007  loss= [  4.26757651e-09]
    x= 13  y= 27  out= 39.9998  loss= [  2.94676283e-08]
    x= -3  y= -29  out= -31.9996  loss= [  1.46977982e-07]
    x= 9  y= 3  out= 12.0  loss= [  1.60434865e-09]
    x= -13  y= -15  out= -27.9996  loss= [  1.42623321e-07]
    x= -19  y= 3  out= -15.9997  loss= [  9.25510903e-08]
    x= -9  y= -17  out= -25.9996  loss= [  1.24509825e-07]
    x= -13  y= 11  out= -1.99981  loss= [  3.63343275e-08]
    x= 5  y= -19  out= -13.9998  loss= [  5.59375621e-08]
    [array([[-0.41777897,  0.73986024],
           [-0.41391361,  0.74204183]], dtype=float32), array([[ 0.08377501, -0.10600967]], dtype=float32), array([[-0.57803202],
           [ 1.02519488]], dtype=float32), array([[ 0.15725224]], dtype=float32)]

## It worked!

Looking at the output above, we can see that even when we pass in inputs that are outside the range of the original training data, we produce values for $x+y$ that are approximately within our final loss (i.e. error estimate) value.  

**Our network has "Learned To Add" just like we thought!**

This result isn't a huge surprise, because the perceptron algorithm is a collection of linear functions composed together, and $x+y$ is linear, so it does a great job.  By this same logic, we could easily have this network learn any function that takes the same form as the equation $output$ shown above. 
## Can we view the parameters? 

Looking back to the original $output$ equation above, we can see that there are many combinations of weights and biases that will exactly solve our equation.  Which one will the optimizer find?  

It turns out that it doesn't really matter, as long as the result is correct.  In fact, it might find other non-obvious combinations of parameters that simplify down to exactly $x+y$.   We can change the code above to print out the values for the weights & biases.  With one run from above, I got the following results: 

$$\begin{array}{rl}
input\_weight & = \begin{bmatrix}-0.83800858 & 0.15946344 \\
       -0.84973776 & 0.08742908\end{bmatrix} \\
input\_bias & = \begin{bmatrix}0.13537928 & -0.1656988\end{bmatrix} \\
out\_weight & = \begin{bmatrix}-1.15744114 & 0.18846205\end{bmatrix} \\
out\_bias & = 0.18807185
\end{array}$$

I'll just let you trust me that if you pass these values into the graph above that the result approximates $x+y$.

## You should play with this code a little bit.

Here's a collection of random ideas for how to play around with the code example above and gain some insights:

* Modify the "f()" function to try other linear combinations of x & y.  Can it learn $x-y$?  Can it learn $0.5x + 0.75y - 0.33$? 
* Modify the size of the middle layer.  We use 2 middle layer nodes.  What if you use 200?  How does that impact learning rate?   
* Modify the size of the middle layer, and have it try to learn something "Hard" like $x\cdot y$. Did it work?  Do you have any thoughts about why or why not?
