

```python
import tensorflow as tf
import numpy
import random
import math
```


```python
# tf Graph Input
num_inputs = 64
num_hidden_1 = 2
num_hidden_2 = 2
num_outputs = 1

inputs = tf.placeholder(dtype=tf.float32, shape=[None, num_inputs], name="inputs")
expected = tf.placeholder(dtype=tf.float32, shape=[None, num_outputs], name="expected")

# First hidden layer of the network 
h1w = tf.Variable(expected_shape=[num_inputs, num_hidden_1], name="hidden_1_weight", 
                 initial_value=tf.truncated_normal([num_inputs, num_hidden_1], stddev=0.25))
h1m = tf.Variable(expected_shape=[num_inputs, num_hidden_1], name="hidden_1_weight", 
                 initial_value=tf.zeros([num_inputs, num_hidden_1]))
h1b = tf.Variable(expected_shape=[1, num_hidden_1], name="hidden_1_bias", 
                 initial_value=tf.truncated_normal([1, num_hidden_1], stddev=0.25))

h1l = tf.nn.sigmoid(tf.multiply(tf.matmul(inputs, h1m), tf.add(tf.matmul(inputs, h1w), h1b)))

# Weight and biases used to turn hidden layer into final output value. 
ow = tf.Variable(expected_shape=[num_hidden_2, num_outputs], name="output_weight", 
                 initial_value=tf.truncated_normal([num_hidden_2, num_outputs], stddev=0.25))
ob = tf.Variable(expected_shape=[1, num_outputs], name="output_bias", 
                 initial_value=tf.truncated_normal([1, num_outputs], stddev=0.25))

output = tf.add(tf.matmul(h1l, ow), ob)

# We compute error as the mean square difference 
error = tf.reduce_mean(tf.pow(tf.subtract(output, expected), 2))
```


```python
# Parameters
learning_rate = 0.0025

# Gradient descent
optimizer = tf.train.AdagradOptimizer(learning_rate).minimize(error)
# optimizer = tf.train.AdamOptimizer(learning_rate).minimize(error)
# optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(error)

# optimizer = tf.train.RMSPropOptimizer(learning_rate).minimize(error)
```


```python
training_steps = 250000

min = 1
max = 11

display_step = 1500
batch_size = 20


def binlist(x, length):
    return [1.0 * (0!=(x&(1<<b))) for b in range(length)]

def onehot(x, length):
    return [1.0 * (x==b) for b in range(length)]

def lesshot(x, length):
    return [1.0 * (x<=b) for b in range(length)]

def zero(length): return [0] * length 

def makeinput(x,y):
    return [x, y]

def f(x,y):  
    return [x*y,]

# Launch the graph
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    
    for epoch in range(training_steps):
        data = { inputs: [], expected: []}
        for b in range(batch_size):
            x = random.randint(min,max)
            y = random.randint(min,max)
            data[inputs].append(makeinput(x,y))
            data[expected].append(f(x,y))
        sess.run(optimizer, feed_dict=data)

        if epoch % display_step == 0:
            e = sess.run(error, feed_dict=data)
            print "Epoch:", epoch, " error=", e
    for x in range(min, max):
        for y in range(min, max):
            data = {inputs: [makeinput(x,y)], expected: [f(x,y)]}
            print " x=", x, " y=", y, " final=", sess.run(output, feed_dict=data), " err=",  sess.run(error, feed_dict=data)
```

    Epoch: 0  error= 2655.56
    Epoch: 1500  error= 1203.85
    Epoch: 3000  error= 2372.36
    Epoch: 4500  error= 1984.28
    Epoch: 6000  error= 1819.93
    Epoch: 7500  error= 1666.59
    Epoch: 9000  error= 1911.48
    Epoch: 10500  error= 2224.03
    Epoch: 12000  error= 1725.16
    Epoch: 13500  error= 1550.02
    Epoch: 15000  error= 2287.33
    Epoch: 16500  error= 3097.88
    Epoch: 18000  error= 1873.38
    Epoch: 19500  error= 2159.08
    Epoch: 21000  error= 959.357
    Epoch: 22500  error= 1786.47
    Epoch: 24000  error= 3274.55
    Epoch: 25500  error= 2559.68
    Epoch: 27000  error= 2117.3
    Epoch: 28500  error= 2083.7
    Epoch: 30000  error= 2214.67
    Epoch: 31500  error= 2470.99
    Epoch: 33000  error= 1872.45
    Epoch: 34500  error= 2712.25
    Epoch: 36000  error= 1123.4
    Epoch: 37500  error= 1683.16
    Epoch: 39000  error= 2583.32
    Epoch: 40500  error= 3411.64
    Epoch: 42000  error= 1130.31
    Epoch: 43500  error= 1463.51
    Epoch: 45000  error= 1032.44
    Epoch: 46500  error= 1873.51
    Epoch: 48000  error= 2398.01
    Epoch: 49500  error= 2054.88
    Epoch: 51000  error= 2270.29
    Epoch: 52500  error= 1743.31
    Epoch: 54000  error= 1543.1
    Epoch: 55500  error= 1442.08
    Epoch: 57000  error= 2096.29
    Epoch: 58500  error= 1146.11
    Epoch: 60000  error= 1653.71
    Epoch: 61500  error= 1741.51
    Epoch: 63000  error= 1464.45
    Epoch: 64500  error= 686.565
    Epoch: 66000  error= 1166.8
    Epoch: 67500  error= 999.876
    Epoch: 69000  error= 2386.23
    Epoch: 70500  error= 2463.44
    Epoch: 72000  error= 3186.19
    Epoch: 73500  error= 960.084



```python
# Regression result
```


```python

```


```python

```
