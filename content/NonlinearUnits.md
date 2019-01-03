Title: Nonlinear Units
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

* **sigmoid** : ``tf.nn.sigmoid``
* **tanh** : ``tf.nn.tanh``
* **ReLu**  : ``tf.nn.relu``

The best way to get a grasp on these is to look at them visually, so here we go: 


```python
%matplotlib inline
%config InlineBackend.figure_format = 'svg'
```


```python
import math
import numpy as np 
import matplotlib.pyplot as plt 

def sigmoid(x): return 1 / (1 + math.exp(-x))
def relu(x):
    if x>0: 
        return x
    else: return 0 

x = np.linspace(-5,5, 100)
plt.figure(figsize=(10,8))
plt.subplot(2,2,1)
plt.plot(x, [sigmoid(v) for v in x])
plt.title("sigmoid")

plt.subplot(2,2,2)
plt.plot(x, np.tanh(x))
plt.title("tanh")

plt.subplot(2,2,3)
plt.plot(x, [relu(v) for v in x])
plt.title("ReLU")
plt.show()
```


![svg]({filename}images/NonlinearUnits_files/NonlinearUnits_5_0.svg)

## Simple Example

As an example of computation that requires nonlinear units, I'd like to propose that we implement a function like this: 
$$f(x) = \begin{cases}
    1.0, & \text{if } \lfloor x \rfloor = 42 \\
    0,         & \text{otherwise}
\end{cases}
$$

This function isn't easily expressed through any combination of linear operators.  Additionally, the fact that the output should be either 1.0 or 0.0 after training suggests that we should use the **sigmoid** function for activation of the neuron(s) in the network. 


```python
import math
import tensorflow as tf 
import random

t = 30.
min_t = 25.
max_t = 35.
def f(x): 
    if x >= t:
        return 1 
    return 0

i = tf.placeholder(shape=(None, 1), dtype=tf.float32, name='input')
o = tf.placeholder(shape=(None, 1), dtype=tf.float32, name='output')

num_hidden = 32

i_w = tf.Variable(expected_shape=(1, num_hidden), 
                initial_value=tf.random.truncated_normal((1, num_hidden), mean=1, stddev=1))
i_b = tf.Variable(expected_shape=(1, num_hidden), 
                initial_value=tf.random.truncated_normal((1, num_hidden), mean=0, stddev=1))

mid = tf.nn.relu(tf.add(tf.matmul(i, i_w), i_b))
# mid = tf.add(tf.matmul(i, i_w), i_b)

o_w = tf.Variable(
    expected_shape=(num_hidden, 1), 
    initial_value=tf.random.truncated_normal((num_hidden, 1), mean=1, stddev=1))
o_b = tf.Variable(
    expected_shape=(1, 1), 
    initial_value=tf.random.truncated_normal((1, 1), mean=0, stddev=1))

output = tf.nn.relu(tf.add(tf.matmul(mid, o_w), o_b))
# output = tf.add(tf.matmul(mid, o_w), o_b)

# Our error function is computed as "Mean Squared Difference" between the computed output
# and the expected value. 
loss = tf.pow(output - o, 2)
mean_loss = tf.reduce_mean(loss)

# Learning rate and optimizer similar to our previous examples. 
# learning_rate = 0.0001
optimizer = tf.train.AdamOptimizer().minimize(loss)

with tf.Session() as sess: 
    sess.run([tf.local_variables_initializer(), 
              tf.global_variables_initializer()])
    
    print "TRAIN"
    batch_size = 200
    train_iterations = 50000
    for step in xrange(train_iterations):
        feed = {i:[], o:[]}
        for b in xrange(batch_size/2):
            v = random.uniform(min_t, max_t)
            feed[i].append([v,])
            feed[o].append([f(v),])
        _, l, out = sess.run([optimizer, mean_loss, output], feed_dict=feed)
        if step % 5000 == 0:
            print "step =",step," loss=", l
            
    print "VALIDATE"
    validate_iterations = 15
    for step in xrange(validate_iterations):
        feed = {i:[], o:[]}
        v = random.uniform(min_t, max_t)
        feed[i].append([v,])
        feed[o].append([f(v),])
        _, l, out = sess.run([optimizer, mean_loss, output], feed_dict=feed)
        print "in = ", feed[i], "output =", out, "expected = ", f(v), " loss=", l
        
        
    print "GRAPH"
    tx = np.linspace(min_t,max_t,100)
    ys = sess.run(output, feed_dict={i:[[ix,] for ix in tx],})
    plt.plot(tx, [v[0] for v in ys], label="learned")
    plt.plot(tx, [f(fx) for fx in tx], label="f(x)")
    plt.legend()
    plt.show()
```

    TRAIN
    step = 0  loss= 1.83179e+06
    step = 5000  loss= 0.156334
    step = 10000  loss= 0.197727
    step = 15000  loss= 0.145691
    step = 20000  loss= 0.0489364
    step = 25000  loss= 0.0920705
    step = 30000  loss= 0.0996958
    step = 35000  loss= 0.0495032
    step = 40000  loss= 0.0642934
    step = 45000  loss= 0.0641886
    VALIDATE
    in =  [[32.003762118671474]] output = [[ 0.76464736]] expected =  1  loss= 0.0553909
    in =  [[32.36696377797531]] output = [[ 0.82751727]] expected =  1  loss= 0.0297503
    in =  [[29.104202468396544]] output = [[ 0.24386668]] expected =  0  loss= 0.059471
    in =  [[25.386498517093727]] output = [[ 0.]] expected =  0  loss= 0.0
    in =  [[33.06359502062598]] output = [[ 0.94786686]] expected =  1  loss= 0.00271786
    in =  [[25.46369592630006]] output = [[ 0.]] expected =  0  loss= 0.0
    in =  [[34.76348901877117]] output = [[ 1.2494638]] expected =  1  loss= 0.0622322
    in =  [[32.77071202248998]] output = [[ 0.88596189]] expected =  1  loss= 0.0130047
    in =  [[33.86705852782782]] output = [[ 1.07837367]] expected =  1  loss= 0.00614243
    in =  [[33.21695256720534]] output = [[ 0.95710593]] expected =  1  loss= 0.0018399
    in =  [[25.06452496846031]] output = [[ 0.]] expected =  0  loss= 0.0
    in =  [[26.761287670627226]] output = [[ 0.]] expected =  0  loss= 0.0
    in =  [[31.26943022484645]] output = [[ 0.60015279]] expected =  1  loss= 0.159878
    in =  [[34.61701252905589]] output = [[ 1.20263445]] expected =  1  loss= 0.0410607
    in =  [[31.322623992257483]] output = [[ 0.61499643]] expected =  1  loss= 0.148228
    GRAPH



![svg]({filename}images/NonlinearUnits_files/NonlinearUnits_7_1.svg)

## You should play with this code a little bit.

Here's a collection of random ideas for how to play around with the code example above and gain some insights:

* Modify the "f()" function to try other linear combinations of x & y.  Can it learn $x-y$?  Can it learn $0.5x + 0.75y - 0.33$? 
* Modify the size of the middle layer.  We use 2 middle layer nodes.  What if you use 200?  How does that impact learning rate?   
* Modify the size of the middle layer, and have it try to learn something "Hard" like $x\cdot y$. Did it work?  Do you have any thoughts about why or why not?
