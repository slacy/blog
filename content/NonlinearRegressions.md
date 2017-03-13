Title: Nonlinear Regressions
Category: TensorFlow From The Ground Up
Tags: Python, TensorFlow, Jupyter
Date: 2/10/2017 11:00am 
Author: slacy

This post part of my series [TensorFlow From The Ground Up]({category}tensorflow-from-the-ground-up).

In my previous post [Learning to Add]({filename}Learning to Add.md), I showed how a Neural Network architecture can learn a simple linear function of two variables.  

In this post, we'll explore how to take our functions from linear to nonlinear.  Additionally, we'll work on going some **regressions** and see what happens when we try to learn nonlinear functions. 
## Composing linear functions

One of the key points of linear functions is that the composition of two linear functions is also a linear function.  The math behind this is fairly straightforward: 

$$\begin{array}{rl}
f(x) & = wx+b \\
f(f(x)) & = w_2(w_1x+b_1)+b_2 \\
& = (w_2w_1)x+(w_2b_1+b_2) \\
\end{array}$$

As you can see, the composed form of $f(f(x))$ is also a linear function, just with $w = w_2w_1$ and $b = w_2b_1+b_2$

Or, to think of this differently:  Without any **nonlinear elements** in our neural network architecture, there's no reason to have any more than one node in the middle layer, because even a giant collection of linear functions still result in a single linear transformation.  

An exception to this is functions of multiple variables, like $f(x,y) = \{a,b\}$  We can work the math backwards, but let it suffice to say that for functions of $N$ inputs and $M$ outputs, we need no more than $\max(N,M)$ linear 
nodes in the middle layer. 

## How do we introduce nonlinearity?

All we need to do is apply some elementwise nonlinear function to all the values in the middle layer of our network.  It ends up making our computation graph look like this: 

$$\begin{array}{rl}
middle\ layer & = input \times W_{mid} + B_{mid} \\
middle\ nonlinear & = f(middle\ layer) \\ 
output & = (midle\ nonlinear) \times W_{out} + B_{out}
\end{array}$$

It's that easy, we just need to choose the right nonlinear function to insert there.  Thankfully, this has been heavily researched, and there are 3 very commonly used functions:

* **Sigmoid**
* **tanh**
* **ReLu** 

The best way to get a grasp on these is to look at them visually, so here we go: 


```python
%matplotlib inline
%config InlineBackend.figure_format = 'svg'
```


```python
import math
import matplotlib.pyplot as plt
import numpy as np
import random
import tensorflow as tf 

def f(x): 
    return math.sin(x*(math.pi/10.0))

x = tf.placeholder(shape=(None, 1), dtype=tf.float32, name='x')
y = tf.placeholder(shape=(None, 1), dtype=tf.float32, name='y')

mid_layer_size = 8

# We are constructing a middle layer of 2 perceptron nodes.  Weights and biases 
# are our w_i and v_i from the above equations. 
input_weight = tf.Variable(expected_shape=(1, mid_layer_size), 
                           initial_value=tf.truncated_normal((1, mid_layer_size), mean=1, stddev=0.1))
input_bias = tf.Variable(expected_shape=(1, mid_layer_size,), 
                         initial_value=tf.truncated_normal((1, mid_layer_size), mean=0, stddev=0.1))

mid_layer = tf.nn.relu(tf.add(tf.matmul(x, input_weight), input_bias))

out_weight = tf.Variable(expected_shape=(mid_layer_size, 1), 
                         initial_value=tf.truncated_normal((mid_layer_size, 1), mean=1, stddev=0.1))
out_bias = tf.Variable(expected_shape=(1, 1), 
                       initial_value=tf.truncated_normal((1, 1), mean=0, stddev=0.1))

output = tf.add(tf.matmul(mid_layer, out_weight), out_bias)

# Our error function is computed as "Mean Squared Difference" between the computed output
# and the expected value. 
loss = tf.reduce_mean(tf.pow(output - y, 2))

# Learning rate and optimizer similar to our previous examples. 
learning_rate = 0.001
optimizer = tf.train.RMSPropOptimizer(learning_rate).minimize(loss)

with tf.Session() as sess: 
    sess.run([tf.local_variables_initializer(), 
              tf.global_variables_initializer()])
    
    print "TRAIN"
    batch_size = 100
    train_iterations = 30000
    li = 6 
    for i in xrange(train_iterations):
        feed = {x:[], y:[]}
        for b in xrange(batch_size):
            v = random.uniform(0, 20)
            feed[x].append([v,])
            feed[y].append([f(v)])
        _, l, out = sess.run([optimizer, loss, output], feed_dict=feed)
        if math.log(i+1) >= li+1:
            li = math.log(i)
            print "i=",i," loss=", l
            tx = np.linspace(0,20,500)
            ys = sess.run(output, feed_dict={x:[[t,] for t in tx],})
            plt.plot(tx, [v[0] for v in ys])
            plt.plot(tx, [f(t) for t in tx])
            # print "feed = ", feed, " output = ", out
            
   
    print "GRAPH"
    tx = np.linspace(0,20,500)
    plt.plot(tx, [f(t) for t in tx])
    plt.show()
```

    TRAIN
    i= 1096  loss= 0.97226
    i= 2979  loss= 0.00867264
    i= 8097  loss= 0.00252741
    i= 22009  loss= 0.00598667
    GRAPH



![svg]({filename}images/NonlinearRegressions_files/NonlinearRegressions_5_1.svg)

## You should play with this code a little bit.

Here's a collection of random ideas for how to play around with the code example above and gain some insights:

* Modify the "f()" function to try other linear combinations of x & y.  Can it learn $x-y$?  Can it learn $0.5x + 0.75y - 0.33$? 
* Modify the size of the middle layer.  We use 2 middle layer nodes.  What if you use 200?  How does that impact learning rate?   
* Modify the size of the middle layer, and have it try to learn something "Hard" like $x\cdot y$. Did it work?  Do you have any thoughts about why or why not?
