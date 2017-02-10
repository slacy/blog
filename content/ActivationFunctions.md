Title: Activation Functions
Category: TensorFlow From The Ground Up
Tags: Python, TensorFlow, Jupyter
Date: 2/8/2017 10:00am 
Author: slacy

This is the **fourth** post of my series [TensorFlow From The Ground Up]({category}tensorflow-from-the-ground-up).

In this post, we'll expand on our "Adding" example Neural Network, and talk about Activation Functions and how they impact the functioning of your system. 

## What are activation functions?

As we saw in the previous post, [Learning to Add]({filename}Learning to Add.md), we can compute some real-vauled functions directly using a Neural Network style architecture. 

This is useful for functions like $f(x) = x+y$ and other linear and "linear-ish" problems.  

A different, but very useful class of functions to model are simple conditionals.  But, the computation graph expressed by TensorFlow has no notion of control flow statements like an *if statement*.  So, how do we model functions that look like conditionals?  

## We use activation functions!

Activation functions are transformations applied to the middle layer of our neural network to modify their values in well-defined ways.  For example, let's think about writing a neural network that implements this behavior: 

$$f(x, y)= 
\begin{cases}
    1.0, & \text{if } x > y \\
    0,         & \text{otherwise}
\end{cases}
$$

There's **no way** to express a function like this using traditional linear equations.  We need to introduce "something more" into the middle of our network.  You might also notice that the output is always either $1.0$ or $0.0$ so maybe there's something we can add to the output layer as well that will "clamp" values into this range.  

You can think of an activation function as describing when a middle-layer node is "on" and when it's "off". 
## Let's look at the common activation functions

There are 3 common activation functions used in Neural Networks, **tanh**, **sigmoid**, and **ReLU**.  Their formulas and graphs of their outputs are show below:  


```python
%matplotlib inline
%config InlineBackend.figure_format = 'svg'
```


```python
import numpy as np
import matplotlib.pyplot as plt
import math
```


```python
x = np.linspace(-4, 4, 500)
plt.plot(x, np.tanh(x))
plt.title('tanh')
plt.show()
```


![svg]({filename}images/ActivationFunctions_files/ActivationFunctions_5_0.svg)

**tanh** takes any real value as input, and always produces a value in the range (-1,1).  At $x=0$, tanh has the value $0.0$.  tanh is symmetric. 


```python
def sigmoid(x): return 1. / (1. + math.exp(-x))

x = np.linspace(-4, 4, 500)
y = [sigmoid(v) for v in x]
plt.plot(x, y)
plt.title('sigmoid')
plt.show()
```


![svg]({filename}images/ActivationFunctions_files/ActivationFunctions_7_0.svg)

**sigmoid** takes any real value as input, and returns a value in the range (0,1).  sigmoid is useful for passing to subsequent analysis (logits, softmax).  sigmoid is also useful for treating nodes "like they have only binary values".  sigmoid is symmetric. 


```python
def relu(x): 
    if x > 0: return x 
    else: return 0

x = np.linspace(-4, 4, 500)
y = [relu(v) for v in x]
plt.plot(x, y)
plt.title('ReLU')
plt.show()
```


![svg]({filename}images/ActivationFunctions_files/ActivationFunctions_9_0.svg)

**relu** is linear for values $x>0$ and otherwise it is zero.  ReLU is not symmetric.  ReLU output values are unbounded for positive vaules.  ReLU is useful for piecewise linear function reconstruction. 
## The Computation Graph

The graph that I'm going to use in this example is **exactly the same** as the graph that I used for the $f(x,y)=x+y$ example, except that I'm going to make two very small changes.  I've duplicated and slightly simplified the code from the [Learning To Add]({filename}/Learning to Add.md) post. 


```python
import tensorflow as tf 
import random

inputs = tf.placeholder(shape=(1, 2), dtype=tf.float32, name='inputs')
expected = tf.placeholder(shape=(1, 1), dtype=tf.float32, name='expected')

# Middle layer with 2 nodes
input_weight = tf.Variable(
    expected_shape=(2, 2), 
    initial_value=tf.truncated_normal((2, 2), mean=0, stddev=0.1))
input_bias = tf.Variable(
    expected_shape=(1, 2), 
    initial_value=tf.truncated_normal((1, 2), mean=0, stddev=0.1))

# Here's where we apply the sigmoid Activation Fuction 
mid_layer = tf.add(tf.matmul(inputs, input_weight), input_bias)

out_weight = tf.Variable(
    expected_shape=(2, 1), 
    initial_value=tf.truncated_normal((2, 1), mean=0, stddev=0.1))
out_bias = tf.Variable(
    expected_shape=(1, 1), 
    initial_value=tf.truncated_normal((1, 1), mean=0, stddev=0.1))

output = tf.nn.sigmoid(
    tf.squeeze(tf.add(tf.matmul(mid_layer, out_weight), out_bias)))
loss = tf.pow(output - expected, 2)

learning_rate = 0.001
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss)

def f(x,y): 
    if x > y: return 1.0 
    return 0.0 

with tf.Session() as sess: 
    sess.run([tf.local_variables_initializer(), 
              tf.global_variables_initializer()])
    
    print "TRAIN"
    train_iterations = 20000
    for i in xrange(train_iterations):
        inp = [random.randrange(0, 10) * 2, random.randrange(0, 10) * 2,]
        e = [f(inp[0],inp[1]),]
        _, l = sess.run([optimizer, loss], feed_dict={inputs:[inp,], expected:[e,]})
        if i % 5000 == 0:
            print "i=",i," loss=", l
            
    print "VALIDATE"
    validate_iterations = 25
    for i in xrange(validate_iterations):
        inp = [random.randrange(0, 100) * 2, random.randrange(0, 100) * 2,]
        e = [f(inp[0], inp[1]),]
        out, l = sess.run([output, loss], feed_dict={inputs:[inp,], expected:[e,]})
        print "x=",inp[0], " y=",inp[1], " out=", out, " loss=", l
```

    TRAIN
    i= 0  loss= [[ 0.34609184]]
    i= 5000  loss= [[ 0.0070237]]
    i= 10000  loss= [[ 0.15544029]]
    i= 15000  loss= [[  1.23779591e-05]]
    VALIDATE
    x= 42  y= 146  out= 0.0  loss= [[ 0.]]
    x= 198  y= 40  out= 1.0  loss= [[ 0.]]
    x= 54  y= 4  out= 1.0  loss= [[ 0.]]
    x= 170  y= 32  out= 1.0  loss= [[ 0.]]
    x= 62  y= 156  out= 0.0  loss= [[ 0.]]
    x= 106  y= 76  out= 1.0  loss= [[ 0.]]
    x= 144  y= 182  out= 1.62947e-21  loss= [[  2.65546059e-42]]
    x= 198  y= 84  out= 1.0  loss= [[ 0.]]
    x= 140  y= 120  out= 0.999665  loss= [[  1.11970863e-07]]
    x= 14  y= 158  out= 0.0  loss= [[ 0.]]
    x= 194  y= 0  out= 1.0  loss= [[ 0.]]
    x= 136  y= 154  out= 6.37686e-13  loss= [[  4.06643129e-25]]
    x= 34  y= 174  out= 0.0  loss= [[ 0.]]
    x= 90  y= 154  out= 1.73523e-30  loss= [[ 0.]]
    x= 62  y= 24  out= 1.0  loss= [[ 0.]]
    x= 130  y= 52  out= 1.0  loss= [[ 0.]]
    x= 2  y= 94  out= 3.93515e-39  loss= [[ 0.]]
    x= 98  y= 68  out= 1.0  loss= [[ 0.]]
    x= 38  y= 58  out= 2.07436e-10  loss= [[  4.30298902e-20]]
    x= 158  y= 54  out= 1.0  loss= [[ 0.]]
    x= 142  y= 38  out= 1.0  loss= [[ 0.]]
    x= 140  y= 76  out= 1.0  loss= [[ 0.]]
    x= 186  y= 104  out= 1.0  loss= [[ 0.]]
    x= 190  y= 124  out= 1.0  loss= [[ 0.]]
    x= 72  y= 28  out= 1.0  loss= [[ 0.]]

## You should play with this code a little bit.

Here's a collection of random ideas for how to play around with the code example above and gain some insights:

* Modify the "f()" function to try other linear combinations of x & y.  Can it learn $x-y$?  Can it learn $0.5x + 0.75y - 0.33$? 
* Modify the size of the middle layer.  We use 2 middle layer nodes.  What if you use 200?  How does that impact learning rate?   
* Modify the size of the middle layer, and have it try to learn something "Hard" like $x\cdot y$. Did it work?  Do you have any thoughts about why or why not?
