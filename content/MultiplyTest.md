

```python
import tensorflow as tf
import numpy
import random
import math
```


```python
# tf Graph Input
num_inputs = 2
num_hidden_1 = 2**9
num_hidden_2 = 2**9
num_outputs = 1

with tf.device("/cpu:0"):
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
training_steps = 500000

min = 1
max = 11

display_step = 1500
batch_size = 10000


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
with tf.Session(config=tf.ConfigProto(log_device_placement=True)) as sess:
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

    Epoch: 0  error= 2050.41
    Epoch: 1500  error= 191.019
    Epoch: 3000  error= 108.287
    Epoch: 4500  error= 73.1853
    Epoch: 6000  error= 58.3512
    Epoch: 7500  error= 46.7543
    Epoch: 9000  error= 41.9739
    Epoch: 10500  error= 34.487
    Epoch: 12000  error= 30.188
    Epoch: 13500  error= 25.582
    Epoch: 15000  error= 23.3378
    Epoch: 16500  error= 20.3602
    Epoch: 18000  error= 18.2277
    Epoch: 19500  error= 16.7097
    Epoch: 21000  error= 13.8739
    Epoch: 22500  error= 12.5283
    Epoch: 24000  error= 11.5058
    Epoch: 25500  error= 10.5898
    Epoch: 27000  error= 9.51226
    Epoch: 28500  error= 8.67877
    Epoch: 30000  error= 8.51565
    Epoch: 31500  error= 7.54449
    Epoch: 33000  error= 6.71541
    Epoch: 34500  error= 6.14442
    Epoch: 36000  error= 6.13817
    Epoch: 37500  error= 5.05782
    Epoch: 39000  error= 5.13202
    Epoch: 40500  error= 4.5342
    Epoch: 42000  error= 4.33378
    Epoch: 43500  error= 4.04114
    Epoch: 45000  error= 3.82566
    Epoch: 46500  error= 3.83586
    Epoch: 48000  error= 3.49676
    Epoch: 49500  error= 3.32453
    Epoch: 51000  error= 3.3072
    Epoch: 52500  error= 3.11653
    Epoch: 54000  error= 3.06762
    Epoch: 55500  error= 2.853
    Epoch: 57000  error= 2.61942
    Epoch: 58500  error= 2.75164
    Epoch: 60000  error= 2.58866
    Epoch: 61500  error= 2.36473
    Epoch: 63000  error= 2.36366
    Epoch: 64500  error= 2.35512
    Epoch: 66000  error= 2.22289
    Epoch: 67500  error= 2.18966
    Epoch: 69000  error= 2.203
    Epoch: 70500  error= 2.00775
    Epoch: 72000  error= 1.94228
    Epoch: 73500  error= 1.89771
    Epoch: 75000  error= 1.92025
    Epoch: 76500  error= 1.725
    Epoch: 78000  error= 1.82255
    Epoch: 79500  error= 1.68853
    Epoch: 81000  error= 1.78539
    Epoch: 82500  error= 1.68297
    Epoch: 84000  error= 1.60413
    Epoch: 85500  error= 1.64171
    Epoch: 87000  error= 1.53166
    Epoch: 88500  error= 1.5657
    Epoch: 90000  error= 1.52302
    Epoch: 91500  error= 1.4283
    Epoch: 93000  error= 1.51561
    Epoch: 94500  error= 1.41314
    Epoch: 96000  error= 1.47648
    Epoch: 97500  error= 1.32661
    Epoch: 99000  error= 1.30973
    Epoch: 100500  error= 1.25958
    Epoch: 102000  error= 1.3133
    Epoch: 103500  error= 1.27346
    Epoch: 105000  error= 1.24649
    Epoch: 106500  error= 1.17345
    Epoch: 108000  error= 1.28041
    Epoch: 109500  error= 1.17457
    Epoch: 111000  error= 1.14091
    Epoch: 112500  error= 1.12941
    Epoch: 114000  error= 1.09826
    Epoch: 115500  error= 1.08073
    Epoch: 117000  error= 1.07543
    Epoch: 118500  error= 1.06687
    Epoch: 120000  error= 1.05921
    Epoch: 121500  error= 1.05256
    Epoch: 123000  error= 0.973081
    Epoch: 124500  error= 1.06719
    Epoch: 126000  error= 0.998388
    Epoch: 127500  error= 0.95802
    Epoch: 129000  error= 0.931299
    Epoch: 130500  error= 0.87659
    Epoch: 132000  error= 0.888521
    Epoch: 133500  error= 0.878168
    Epoch: 135000  error= 0.891105
    Epoch: 136500  error= 0.850319
    Epoch: 138000  error= 0.895172
    Epoch: 139500  error= 0.811795
    Epoch: 141000  error= 0.802373
    Epoch: 142500  error= 0.810641
    Epoch: 144000  error= 0.849691
    Epoch: 145500  error= 0.749127
    Epoch: 147000  error= 0.722847
    Epoch: 148500  error= 0.765856
    Epoch: 150000  error= 0.762195
    Epoch: 151500  error= 0.700087
    Epoch: 153000  error= 0.738815
    Epoch: 154500  error= 0.707467
    Epoch: 156000  error= 0.67901
    Epoch: 157500  error= 0.695824
    Epoch: 159000  error= 0.650161
    Epoch: 160500  error= 0.715403
    Epoch: 162000  error= 0.636672
    Epoch: 163500  error= 0.610803
    Epoch: 165000  error= 0.64
    Epoch: 166500  error= 0.635668
    Epoch: 168000  error= 0.667733
    Epoch: 169500  error= 0.634117
    Epoch: 171000  error= 0.58141
    Epoch: 172500  error= 0.603595
    Epoch: 174000  error= 0.599736
    Epoch: 175500  error= 0.542104
    Epoch: 177000  error= 0.557591
    Epoch: 178500  error= 0.527298
    Epoch: 180000  error= 0.588672
    Epoch: 181500  error= 0.526927
    Epoch: 183000  error= 0.522668
    Epoch: 184500  error= 0.530291



```python
# Regression result
```


```python

```


```python

```
