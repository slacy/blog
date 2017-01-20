Title: SimpleTwoLayer
Date: 2017-01-20 13:10
Category: Tensorflow
Tags: Tensorflow, iPython 


```python
import tensorflow as tf
import numpy
import random
import math
```


```python
# tf Graph Input
num_inputs = 32
num_hidden_1 = 256
num_hidden_2 = 256
num_outputs = 32

inputs = tf.placeholder(dtype=tf.float32, shape=[None, num_inputs], name="inputs")
expected = tf.placeholder(dtype=tf.float32, shape=[None, num_outputs], name="expected")

# First hidden layer of the network 
h1w = tf.Variable(expected_shape=[num_inputs, num_hidden_1], name="hidden_1_weight", 
                 initial_value=tf.truncated_normal([num_inputs, num_hidden_1], stddev=0.25))
h1b = tf.Variable(expected_shape=[1, num_hidden_1], name="hidden_1_bias", 
                 initial_value=tf.truncated_normal([1, num_hidden_1], stddev=0.25))

h1l = tf.nn.sigmoid(tf.add(tf.matmul(inputs, h1w), h1b))

# Second hidden layer of the network 
h2w = tf.Variable(expected_shape=[num_hidden_1, num_hidden_2], name="hidden_2_weight", 
                 initial_value=tf.truncated_normal([num_hidden_1, num_hidden_2], stddev=0.25))
h2b = tf.Variable(expected_shape=[1, num_hidden_2], name="hidden_2_bias", 
                 initial_value=tf.truncated_normal([1, num_hidden_2], stddev=0.25))

h2l = tf.nn.sigmoid(tf.add(tf.matmul(h1l, h2w), h2b))

# Weight and biases used to turn hidden layer into final output value. 
ow = tf.Variable(expected_shape=[num_hidden_2, num_outputs], name="output_weight", 
                 initial_value=tf.truncated_normal([num_hidden_2, num_outputs], stddev=0.25))
ob = tf.Variable(expected_shape=[1, num_outputs], name="output_bias", 
                 initial_value=tf.truncated_normal([1, num_outputs], stddev=0.25))

output = tf.add(tf.matmul(h2l, ow), ob)
final = tf.argmax(tf.nn.softmax(output),1)

# We compute error as the mean square difference 
error = tf.reduce_mean(tf.pow(tf.subtract(output, expected), 2))
```


```python
# Parameters
learning_rate = 0.0025

# Gradient descent
# optimizer = tf.train.AdagradOptimizer(learning_rate).minimize(error)
# optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(error)

optimizer = tf.train.RMSPropOptimizer(learning_rate).minimize(error)
```


```python
training_steps = 25000

min = 1
max = 11

display_step = 500
batch_size = 123


def binlist(x, length):
    return [1.0 * (0!=(x&(1<<b))) for b in range(length)]

def onehot(x, length):
    return [1.0 * (x==b) for b in range(length)]

def lesshot(x, length):
    return [1.0 * (x<=b) for b in range(length)]

def zero(length): return [0] * length 

def makeinput(x,y):
    return [x, math.log(x)] + onehot(x, 14) + [y, math.log(y)] + onehot(y, 14)

def f(x,y):  
    return onehot(x*y, 32)

# Launch the graph
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    
    for epoch in range(training_steps):
        data = { inputs: [], expected: []}
        for b in range(batch_size):
#            x = random.uniform(min,max)
#            y = random.uniform(min,max)
            x = random.randint(min,max)
            y = random.randint(min,max)
            data[inputs].append(makeinput(x,y))
            data[expected].append(f(x,y))
        sess.run(optimizer, feed_dict=data)

        if epoch % display_step == 0:
#           print "data=", data 
            e = sess.run(error, feed_dict=data)
            print "Epoch:", epoch, " error=", e
#    print "iw= ", sess.run(h1w)
#    print "ib= ", sess.run(h1b)
#    print "ow= ", sess.run(ow)
#    print "ob= ", sess.run(ob)
    for x in range(min, max):
        for y in range(min, max):
            data = {inputs: [makeinput(x,y)], expected: [f(x,y)]}
            print " x=", x, " y=", y, " final=", sess.run(final, feed_dict=data), " err=",  sess.run(error, feed_dict=data)
```

    Epoch: 0  error= 4.77259
    Epoch: 500  error= 0.0349073
    Epoch: 1000  error= 0.0294826
    Epoch: 1500  error= 0.0283848
    Epoch: 2000  error= 0.0250567
    Epoch: 2500  error= 0.0259698
    Epoch: 3000  error= 0.0279335
    Epoch: 3500  error= 0.0249026
    Epoch: 4000  error= 0.0185042
    Epoch: 4500  error= 0.0217147
    Epoch: 5000  error= 0.0186127
    Epoch: 5500  error= 0.0204421
    Epoch: 6000  error= 0.0188873
    Epoch: 6500  error= 0.0203958
    Epoch: 7000  error= 0.0215895
    Epoch: 7500  error= 0.0201102
    Epoch: 8000  error= 0.0181754
    Epoch: 8500  error= 0.0196443
    Epoch: 9000  error= 0.0195766
    Epoch: 9500  error= 0.0194217
    Epoch: 10000  error= 0.020162
    Epoch: 10500  error= 0.0211055
    Epoch: 11000  error= 0.021412
    Epoch: 11500  error= 0.0204951
    Epoch: 12000  error= 0.0198731
    Epoch: 12500  error= 0.0193826
    Epoch: 13000  error= 0.0209889
    Epoch: 13500  error= 0.0202145
    Epoch: 14000  error= 0.0200615
    Epoch: 14500  error= 0.0202297
    Epoch: 15000  error= 0.0188876
    Epoch: 15500  error= 0.022628
    Epoch: 16000  error= 0.0184934
    Epoch: 16500  error= 0.0193896
    Epoch: 17000  error= 0.0201786
    Epoch: 17500  error= 0.0207515
    Epoch: 18000  error= 0.0203698
    Epoch: 18500  error= 0.0198319
    Epoch: 19000  error= 0.0198839
    Epoch: 19500  error= 0.0192824
    Epoch: 20000  error= 0.019172
    Epoch: 20500  error= 0.0181997
    Epoch: 21000  error= 0.0203081
    Epoch: 21500  error= 0.0193622
    Epoch: 22000  error= 0.0194352
    Epoch: 22500  error= 0.0179964
    Epoch: 23000  error= 0.0198102
    Epoch: 23500  error= 0.0210747
    Epoch: 24000  error= 0.0205689
    Epoch: 24500  error= 0.0204065
     x= 1  y= 1  final= [1]  err= 0.017748
     x= 1  y= 2  final= [2]  err= 0.0156026
     x= 1  y= 3  final= [3]  err= 0.0167551
     x= 1  y= 4  final= [4]  err= 0.0149964
     x= 1  y= 5  final= [5]  err= 0.0213292
     x= 1  y= 6  final= [6]  err= 0.0170464
     x= 1  y= 7  final= [7]  err= 0.0178607
     x= 1  y= 8  final= [8]  err= 0.0138175
     x= 1  y= 9  final= [9]  err= 0.0200177
     x= 1  y= 10  final= [10]  err= 0.0179931
     x= 2  y= 1  final= [2]  err= 0.018411
     x= 2  y= 2  final= [4]  err= 0.0175102
     x= 2  y= 3  final= [6]  err= 0.0195138
     x= 2  y= 4  final= [8]  err= 0.0192228
     x= 2  y= 5  final= [10]  err= 0.02061
     x= 2  y= 6  final= [12]  err= 0.0183887
     x= 2  y= 7  final= [14]  err= 0.0229745
     x= 2  y= 8  final= [16]  err= 0.020118
     x= 2  y= 9  final= [18]  err= 0.0182974
     x= 2  y= 10  final= [20]  err= 0.0174547
     x= 3  y= 1  final= [3]  err= 0.016586
     x= 3  y= 2  final= [6]  err= 0.0194152
     x= 3  y= 3  final= [9]  err= 0.0160293
     x= 3  y= 4  final= [12]  err= 0.0172353
     x= 3  y= 5  final= [15]  err= 0.0199596
     x= 3  y= 6  final= [18]  err= 0.0139718
     x= 3  y= 7  final= [21]  err= 0.0200283
     x= 3  y= 8  final= [24]  err= 0.0193671
     x= 3  y= 9  final= [27]  err= 0.0148442
     x= 3  y= 10  final= [30]  err= 0.016972
     x= 4  y= 1  final= [4]  err= 0.0181802
     x= 4  y= 2  final= [8]  err= 0.0193645
     x= 4  y= 3  final= [12]  err= 0.0160701
     x= 4  y= 4  final= [16]  err= 0.0198869
     x= 4  y= 5  final= [20]  err= 0.0174199
     x= 4  y= 6  final= [24]  err= 0.0220794
     x= 4  y= 7  final= [28]  err= 0.0218914
     x= 4  y= 8  final= [27]  err= 0.0190898
     x= 4  y= 9  final= [2]  err= 0.019299
     x= 4  y= 10  final= [27]  err= 0.019107
     x= 5  y= 1  final= [5]  err= 0.0157037
     x= 5  y= 2  final= [10]  err= 0.0225148
     x= 5  y= 3  final= [15]  err= 0.0194957
     x= 5  y= 4  final= [20]  err= 0.0169652
     x= 5  y= 5  final= [25]  err= 0.0225768
     x= 5  y= 6  final= [30]  err= 0.0174705
     x= 5  y= 7  final= [27]  err= 0.0192931
     x= 5  y= 8  final= [27]  err= 0.0192087
     x= 5  y= 9  final= [27]  err= 0.0193552
     x= 5  y= 10  final= [27]  err= 0.0193359
     x= 6  y= 1  final= [6]  err= 0.0196952
     x= 6  y= 2  final= [12]  err= 0.0221897
     x= 6  y= 3  final= [18]  err= 0.0144802
     x= 6  y= 4  final= [24]  err= 0.0222366
     x= 6  y= 5  final= [30]  err= 0.017663
     x= 6  y= 6  final= [27]  err= 0.019617
     x= 6  y= 7  final= [27]  err= 0.019319
     x= 6  y= 8  final= [27]  err= 0.019293
     x= 6  y= 9  final= [27]  err= 0.019373
     x= 6  y= 10  final= [27]  err= 0.0193068
     x= 7  y= 1  final= [7]  err= 0.0233906
     x= 7  y= 2  final= [14]  err= 0.0197051
     x= 7  y= 3  final= [21]  err= 0.0202752
     x= 7  y= 4  final= [28]  err= 0.0217221
     x= 7  y= 5  final= [2]  err= 0.0194225
     x= 7  y= 6  final= [27]  err= 0.0193226
     x= 7  y= 7  final= [27]  err= 0.0192805
     x= 7  y= 8  final= [27]  err= 0.0193565
     x= 7  y= 9  final= [27]  err= 0.0193667
     x= 7  y= 10  final= [27]  err= 0.0193388
     x= 8  y= 1  final= [8]  err= 0.0199535
     x= 8  y= 2  final= [16]  err= 0.0198605
     x= 8  y= 3  final= [24]  err= 0.0202155
     x= 8  y= 4  final= [27]  err= 0.0193109
     x= 8  y= 5  final= [2]  err= 0.0192252
     x= 8  y= 6  final= [27]  err= 0.019348
     x= 8  y= 7  final= [27]  err= 0.019376
     x= 8  y= 8  final= [27]  err= 0.0195537
     x= 8  y= 9  final= [27]  err= 0.0193971
     x= 8  y= 10  final= [27]  err= 0.0193842
     x= 9  y= 1  final= [9]  err= 0.0187502
     x= 9  y= 2  final= [18]  err= 0.0149961
     x= 9  y= 3  final= [27]  err= 0.020852
     x= 9  y= 4  final= [2]  err= 0.0192454
     x= 9  y= 5  final= [27]  err= 0.0193908
     x= 9  y= 6  final= [27]  err= 0.0193216
     x= 9  y= 7  final= [27]  err= 0.0193272
     x= 9  y= 8  final= [27]  err= 0.019358
     x= 9  y= 9  final= [27]  err= 0.0193752
     x= 9  y= 10  final= [27]  err= 0.0193549
     x= 10  y= 1  final= [10]  err= 0.0174703
     x= 10  y= 2  final= [20]  err= 0.0182103
     x= 10  y= 3  final= [30]  err= 0.017932
     x= 10  y= 4  final= [2]  err= 0.0192752
     x= 10  y= 5  final= [27]  err= 0.0194601
     x= 10  y= 6  final= [27]  err= 0.0193733
     x= 10  y= 7  final= [27]  err= 0.0193753
     x= 10  y= 8  final= [27]  err= 0.0194009
     x= 10  y= 9  final= [27]  err= 0.019444
     x= 10  y= 10  final= [27]  err= 0.0194707



```python
# Regression result
```


```python

```


```python

```
