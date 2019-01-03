Title: Feature Engineering (Counting the Bits)
Category: TensorFlow From The Ground Up
Tags: Python, TensorFlow, Jupyter
Date: 3/13/2017 4:30pm
Author: slacy
Status: draft
Feature engineering is the task of deciding how to represent the data that goes in and out of your Machine Learning system.  Feature Engineering is a vital part of network design, because it turns out that how features (i.e. data) is represented has a huge impact on how easy it will be for your system to learn the task that you are interested in.

To illustrate how important Feature Engineering is, one good approach is to "make up" some synthetic examples with synthetic inputs & outputs, and see if we can learn the task at hand. 

## Counting Bits in Binary 

For this exercise, we are going to use "counting the binary bits" (also referred to as "*popcount*" or "*Hamming Distance*") as the function we are trying to learn.  This function cannot be represented by a linear function, se we'll be using a 2-layer network.  We will constrain our input our values in the range $[0,1024)$, and our outputs will be in the range $[0,10]$.  We can think of our training set as looking somewhat like this:

$$
\begin{array}{|c|c|}
\hline input & popcount(input) \\\hline
  374 & 5 \\\hline
  924 & 6 \\\hline
  708 & 4 \\\hline
  6 & 2 \\\hline
  ... & ... \\\hline
\end{array}
$$

Let's try passing these integer values directly into the first layer of the network and see what happens!


```python
import tensorflow as tf 
import random

inputs = tf.placeholder(shape=(None, 1), dtype=tf.float32, name='input')
popcount = tf.placeholder(shape=(None, 1), dtype=tf.float32, name='popcount')

input_weight = tf.Variable(expected_shape=(1, 16), 
                           initial_value=tf.truncated_normal((1, 16), mean=0, stddev=0.1))
input_bias = tf.Variable(expected_shape=(1,16), 
                         initial_value=tf.truncated_normal((1,16), mean=0, stddev=0.1))

# "Perceptron" 
mid_layer = tf.nn.sigmoid(tf.add(tf.matmul(inputs, input_weight), input_bias))

out_weight = tf.Variable(expected_shape=(16, 1), 
                         initial_value=tf.truncated_normal((16, 1), mean=0, stddev=0.1))
out_bias = tf.Variable(expected_shape=(1, 1), 
                       initial_value=tf.truncated_normal((1, 1), mean=0, stddev=0.1))

# Perceptron formula again.
output = tf.add(tf.matmul(mid_layer, out_weight), out_bias)

# Our error function is computed as "Squared Difference" between the computed output
# and the expected value. 
loss = tf.reduce_mean(tf.pow(output - popcount, 2))

# Learning rate and optimizer similar to our previous examples. 
learning_rate = 0.001
optimizer = tf.train.AdamOptimizer(learning_rate).minimize(loss)

def f(x): 
    popcount = 0 
    while x: 
        if x&1:
            popcount+=1
        x>>=1 
    return popcount

def makeinput(x):
    return [x,]

with tf.Session() as sess: 
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
    train_iterations = 100000
    batch_size = 128
    max_value = 16
    for it in xrange(train_iterations):
        feed = {inputs:[], popcount:[]}
        for bt in xrange(batch_size):
            v = random.randrange(0, max_value)
            feed[inputs].append(makeinput(v))
            feed[popcount].append(makeinput(f(v)))
        _, l = sess.run([optimizer, loss], feed_dict=feed)
        if it % 1000 == 0:
            print "i=",it," loss=", l
            
    # Once we have learned the parameters, we can validate by passing inputs 
    # never seen before.  For this case, we expand the range of our inputs 
    # to include all odd numbers in the range [-40,40].  
    print "VALIDATE"
    validate_iterations = 25
    for it in xrange(validate_iterations):
        v = random.randrange(0, max_value)
        i = [makeinput(v),]
        e = [makeinput(f(v)),]
        out, l = sess.run([output, loss], feed_dict={inputs:i, popcount:e})
        print "input=",i," out=", out, "actual=,", e," loss=", l

```

    TRAIN
    i= 0  loss= 4.62908
    i= 1000  loss= 0.419672
    i= 2000  loss= 0.350638
    i= 3000  loss= 0.413125
    i= 4000  loss= 0.352155
    i= 5000  loss= 0.327442
    i= 6000  loss= 0.344848
    i= 7000  loss= 0.356394
    i= 8000  loss= 0.305952
    i= 9000  loss= 0.308031
    i= 10000  loss= 0.283118
    i= 11000  loss= 0.369738
    i= 12000  loss= 0.303562
    i= 13000  loss= 0.308296
    i= 14000  loss= 0.333424
    i= 15000  loss= 0.30559
    i= 16000  loss= 0.291579
    i= 17000  loss= 0.351013
    i= 18000  loss= 0.338948
    i= 19000  loss= 0.362444
    i= 20000  loss= 0.304563
    i= 21000  loss= 0.180726
    i= 22000  loss= 0.266295
    i= 23000  loss= 0.270902
    i= 24000  loss= 0.25015
    i= 25000  loss= 0.241592
    i= 26000  loss= 0.272542
    i= 27000  loss= 0.272879
    i= 28000  loss= 0.263778
    i= 29000  loss= 0.211322
    i= 30000  loss= 0.282963
    i= 31000  loss= 0.319068
    i= 32000  loss= 0.230075
    i= 33000  loss= 0.284408
    i= 34000  loss= 0.301685
    i= 35000  loss= 0.247171
    i= 36000  loss= 0.319898
    i= 37000  loss= 0.253544
    i= 38000  loss= 0.240501
    i= 39000  loss= 0.2356
    i= 40000  loss= 0.280686
    i= 41000  loss= 0.226019
    i= 42000  loss= 0.214324
    i= 43000  loss= 0.262179
    i= 44000  loss= 0.198153
    i= 45000  loss= 0.261084
    i= 46000  loss= 0.240503
    i= 47000  loss= 0.235443
    i= 48000  loss= 0.269355
    i= 49000  loss= 0.314097
    i= 50000  loss= 0.238789
    i= 51000  loss= 0.203914
    i= 52000  loss= 0.29305
    i= 53000  loss= 0.291942
    i= 54000  loss= 0.302206
    i= 55000  loss= 0.242575
    i= 56000  loss= 0.27227
    i= 57000  loss= 0.223717
    i= 58000  loss= 0.249152
    i= 59000  loss= 0.202866
    i= 60000  loss= 0.208728
    i= 61000  loss= 0.235625
    i= 62000  loss= 0.203516
    i= 63000  loss= 0.245659
    i= 64000  loss= 0.253923
    i= 65000  loss= 0.213467
    i= 66000  loss= 0.239217
    i= 67000  loss= 0.231245
    i= 68000  loss= 0.256408
    i= 69000  loss= 0.231592
    i= 70000  loss= 0.197811
    i= 71000  loss= 0.231928
    i= 72000  loss= 0.254814
    i= 73000  loss= 0.227593
    i= 74000  loss= 0.217913
    i= 75000  loss= 0.254691
    i= 76000  loss= 0.285135
    i= 77000  loss= 0.235177
    i= 78000  loss= 0.205863
    i= 79000  loss= 0.21152
    i= 80000  loss= 0.244499
    i= 81000  loss= 0.227693
    i= 82000  loss= 0.229226
    i= 83000  loss= 0.219194
    i= 84000  loss= 0.232463
    i= 85000  loss= 0.210225
    i= 86000  loss= 0.246284
    i= 87000  loss= 0.222384
    i= 88000  loss= 0.234835
    i= 89000  loss= 0.214603
    i= 90000  loss= 0.21836
    i= 91000  loss= 0.241133
    i= 92000  loss= 0.222177
    i= 93000  loss= 0.233147
    i= 94000  loss= 0.238967
    i= 95000  loss= 0.200362
    i= 96000  loss= 0.215999
    i= 97000  loss= 0.193563
    i= 98000  loss= 0.207447
    i= 99000  loss= 0.230364
    VALIDATE
    input= [[7]]  out= [[ 2.09152031]] actual=, [[3]]  loss= 0.825335
    input= [[3]]  out= [[ 1.37256026]] actual=, [[2]]  loss= 0.393681
    input= [[5]]  out= [[ 1.95039511]] actual=, [[2]]  loss= 0.00246065
    input= [[11]]  out= [[ 2.25213575]] actual=, [[3]]  loss= 0.559301
    input= [[10]]  out= [[ 1.9918443]] actual=, [[2]]  loss= 6.65155e-05
    input= [[3]]  out= [[ 1.37256026]] actual=, [[2]]  loss= 0.393681
    input= [[10]]  out= [[ 1.9918443]] actual=, [[2]]  loss= 6.65155e-05
    input= [[9]]  out= [[ 1.8509928]] actual=, [[2]]  loss= 0.0222031
    input= [[14]]  out= [[ 3.30856967]] actual=, [[3]]  loss= 0.0952152
    input= [[11]]  out= [[ 2.25213575]] actual=, [[3]]  loss= 0.559301
    input= [[1]]  out= [[ 0.97653669]] actual=, [[1]]  loss= 0.000550527
    input= [[12]]  out= [[ 2.57091808]] actual=, [[2]]  loss= 0.325947
    input= [[8]]  out= [[ 1.90836024]] actual=, [[1]]  loss= 0.825118
    input= [[3]]  out= [[ 1.37256026]] actual=, [[2]]  loss= 0.393681
    input= [[3]]  out= [[ 1.37256026]] actual=, [[2]]  loss= 0.393681
    input= [[10]]  out= [[ 1.9918443]] actual=, [[2]]  loss= 6.65155e-05
    input= [[6]]  out= [[ 2.13547993]] actual=, [[2]]  loss= 0.0183548
    input= [[11]]  out= [[ 2.25213575]] actual=, [[3]]  loss= 0.559301
    input= [[12]]  out= [[ 2.57091808]] actual=, [[2]]  loss= 0.325947
    input= [[3]]  out= [[ 1.37256026]] actual=, [[2]]  loss= 0.393681
    input= [[0]]  out= [[ 0.00694078]] actual=, [[0]]  loss= 4.81745e-05
    input= [[12]]  out= [[ 2.57091808]] actual=, [[2]]  loss= 0.325947
    input= [[10]]  out= [[ 1.9918443]] actual=, [[2]]  loss= 6.65155e-05
    input= [[5]]  out= [[ 1.95039511]] actual=, [[2]]  loss= 0.00246065
    input= [[1]]  out= [[ 0.97653669]] actual=, [[1]]  loss= 0.000550527

