

```python
import tensorflow as tf
# import numpy
import random
import math
```


```python
# tf Graph Input
num_inputs = 16
num_hidden_1 = num_inputs*32
num_hidden_2 = num_inputs*32
num_outputs = 16
stddev = 1.0 

with tf.device('/gpu:0'):
    inputs = tf.placeholder(dtype=tf.float32, shape=[None, num_inputs], name="inputs")
    expected = tf.placeholder(dtype=tf.float32, shape=[None, num_outputs], name="expected")

    # First hidden layer of the network 
    h1w = tf.Variable(expected_shape=[num_inputs, num_hidden_1], name="hidden_1_weight", 
                     initial_value=tf.truncated_normal([num_inputs, num_hidden_1], stddev=stddev))
    h1b = tf.Variable(expected_shape=[1, num_hidden_1], name="hidden_1_bias", 
                     initial_value=tf.truncated_normal([1, num_hidden_1], stddev=stddev))

    h1l = tf.nn.sigmoid(tf.add(tf.matmul(inputs, h1w), h1b))

    # Second hidden layer of the network 
    h2w = tf.Variable(expected_shape=[num_hidden_1, num_hidden_2], name="hidden_2_weight", 
                     initial_value=tf.truncated_normal([num_hidden_1, num_hidden_2], stddev=stddev))
    h2b = tf.Variable(expected_shape=[1, num_hidden_2], name="hidden_2_bias", 
                     initial_value=tf.truncated_normal([1, num_hidden_2], stddev=stddev))

    h2l = tf.nn.sigmoid(tf.add(tf.matmul(h1l, h2w), h2b))

    # Weight and biases used to turn hidden layer into final output value. 
    ow = tf.Variable(expected_shape=[num_hidden_2, num_outputs], name="output_weight", 
                     initial_value=tf.truncated_normal([num_hidden_2, num_outputs], stddev=stddev))
    ob = tf.Variable(expected_shape=[1, num_outputs], name="output_bias", 
                     initial_value=tf.truncated_normal([1, num_outputs], stddev=stddev))

    output = tf.add(tf.matmul(h2l, ow), ob)

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
training_steps = 10000

min = 1
max = 2**num_inputs
parity_max = 16

display_step = 500
batch_size = 32

def binlist(x, length):
    return [1.0 * (0!=(x&(1<<b))) for b in range(length)]

def onehot(x, length):
    return [1.0 * (x==b) for b in range(length)]

def lesshot(x, length):
    return [1.0 * (x<=b) for b in range(length)]

def zero(length): return [0] * length 

def makeinput(x):
    return binlist(x, num_inputs)

def f(x):  
    binx = binlist(x, num_inputs)
    numbits = sum([binx[i] for i in range(parity_max)])
    return onehot(numbits, num_inputs)

# Launch the graph
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    
    for epoch in range(training_steps):
        data = { inputs: [], expected: []}
        for b in range(batch_size):
            x = random.randint(min,max)
            data[inputs].append(makeinput(x))
            data[expected].append(f(x))
        sess.run(optimizer, feed_dict=data)

        if epoch % display_step == 0:
            e = sess.run(error, feed_dict=data)
            print "Epoch:", epoch, " error=", e
    for x in range(min, parity_max):
        data = {inputs: [makeinput(x)], expected: [f(x)]}
        print (" x=", x, " output=", sess.run(output, feed_dict=data), 
        " expected=", data[expected], 
        " err=",  sess.run(error, feed_dict=data))
```

    Epoch: 0  error= 160.914
    Epoch: 500  error= 0.174251
    Epoch: 1000  error= 0.139204
    Epoch: 1500  error= 0.138081
    Epoch: 2000  error= 0.150861
    Epoch: 2500  error= 0.139574
    Epoch: 3000  error= 0.127498
    Epoch: 3500  error= 0.140545
    Epoch: 4000  error= 0.177505
    Epoch: 4500  error= 0.160604
    Epoch: 5000  error= 0.124091
    Epoch: 5500  error= 0.145918
    Epoch: 6000  error= 0.119354
    Epoch: 6500  error= 0.12316
    Epoch: 7000  error= 0.160334
    Epoch: 7500  error= 0.171522
    Epoch: 8000  error= 0.153141
    Epoch: 8500  error= 0.165144
    Epoch: 9000  error= 0.11152
    Epoch: 9500  error= 0.114472
    (' x=', 1, ' output=', array([[ 0.29957753,  0.3047058 ,  0.31570122,  0.48503971,  0.67529303,
             0.50044376,  0.67335773, -0.50412762,  0.04999673, -0.48846126,
            -0.39888275, -0.4102124 , -0.10306102,  0.3734566 ,  0.2925266 ,
             0.30002248]], dtype=float32), ' expected=', [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], ' err=', 0.20101775)
    (' x=', 2, ' output=', array([[ 0.2942782 ,  0.31659716,  0.34198198,  0.49605322,  0.6865046 ,
             0.51475537,  0.65644491, -0.51937079,  0.04686451, -0.49936175,
            -0.42238152, -0.40602666, -0.12405235,  0.37673956,  0.28263378,
             0.28323674]], dtype=float32), ' expected=', [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], ' err=', 0.20411475)
    (' x=', 3, ' output=', array([[ 0.28929669,  0.29824513,  0.321089  ,  0.47406459,  0.68340695,
             0.50331074,  0.68912733, -0.51150048,  0.05525929, -0.49102592,
            -0.40090442, -0.3935923 , -0.10140127,  0.38934511,  0.28892934,
             0.29753721]], dtype=float32), ' expected=', [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], ' err=', 0.20055473)
    (' x=', 4, ' output=', array([[ 0.26413995,  0.32465893,  0.3553302 ,  0.50308371,  0.72583735,
             0.51330811,  0.62959898, -0.53334963,  0.0344463 , -0.50666165,
            -0.46745855, -0.39424235, -0.11552316,  0.41038913,  0.29538369,
             0.27414107]], dtype=float32), ' expected=', [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], ' err=', 0.20952481)
    (' x=', 5, ' output=', array([[ 0.27896053,  0.29756421,  0.32148811,  0.47502506,  0.69537735,
             0.50086856,  0.68596864, -0.51471114,  0.05322146, -0.49383831,
            -0.41024685, -0.39041513, -0.09535581,  0.39991289,  0.29439795,
             0.29684377]], dtype=float32), ' expected=', [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], ' err=', 0.20209593)
    (' x=', 6, ' output=', array([[ 0.28597742,  0.30618244,  0.33227643,  0.48323762,  0.69250441,
             0.50824839,  0.67350364, -0.51909864,  0.0492717 , -0.49640226,
            -0.41723442, -0.39595431, -0.10873383,  0.39051253,  0.28723145,
             0.2906121 ]], dtype=float32), ' expected=', [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], ' err=', 0.20167756)
    (' x=', 7, ' output=', array([[ 0.28591949,  0.29841167,  0.32122061,  0.47437567,  0.68802196,
             0.50335175,  0.68834674, -0.51291025,  0.05441308, -0.49200034,
            -0.40356219, -0.39136332, -0.09997493,  0.39325196,  0.29031706,
             0.29708064]], dtype=float32), ' expected=', [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], ' err=', 0.18200839)
    (' x=', 8, ' output=', array([[ 0.29691821,  0.33310777,  0.33469507,  0.52035999,  0.67657244,
             0.51163894,  0.62214482, -0.50932169,  0.04786658, -0.48751122,
            -0.41276675, -0.42702019, -0.13401419,  0.35121906,  0.29310894,
             0.29769623]], dtype=float32), ' expected=', [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], ' err=', 0.19938937)
    (' x=', 9, ' output=', array([[ 0.28912979,  0.29706204,  0.3203778 ,  0.47345912,  0.68283594,
             0.50277346,  0.69011605, -0.51146555,  0.0560267 , -0.49044418,
            -0.39966035, -0.39399987, -0.09981257,  0.38921058,  0.28964913,
             0.29867995]], dtype=float32), ' expected=', [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], ' err=', 0.20049922)
    (' x=', 10, ' output=', array([[ 0.28744549,  0.30154711,  0.32460567,  0.47886693,  0.68408632,
             0.5047918 ,  0.68278563, -0.51304412,  0.05572999, -0.49148607,
            -0.40262604, -0.39490837, -0.10555023,  0.3871631 ,  0.28880489,
             0.29757774]], dtype=float32), ' expected=', [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], ' err=', 0.20043421)
    (' x=', 11, ' output=', array([[ 0.28877765,  0.29697824,  0.3202996 ,  0.47294259,  0.68283492,
             0.50269741,  0.69068706, -0.5112083 ,  0.05607861, -0.49062657,
            -0.39955127, -0.39316511, -0.09992665,  0.38990676,  0.28922057,
             0.29873967]], dtype=float32), ' expected=', [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], ' err=', 0.18139416)
    (' x=', 12, ' output=', array([[ 0.28640956,  0.30857831,  0.33478758,  0.48456383,  0.68944794,
             0.51115626,  0.66991961, -0.51886725,  0.05193543, -0.49428439,
            -0.41701895, -0.39660221, -0.11238331,  0.38769114,  0.28721404,
             0.29012799]], dtype=float32), ' expected=', [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], ' err=', 0.20106302)
    (' x=', 13, ' output=', array([[ 0.28798634,  0.29717177,  0.32064959,  0.47311872,  0.68387127,
             0.5028522 ,  0.69064236, -0.51168871,  0.05585504, -0.49062157,
            -0.40033782, -0.39284742, -0.09972852,  0.39037687,  0.2897445 ,
             0.29867542]], dtype=float32), ' expected=', [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], ' err=', 0.18155919)
    (' x=', 14, ' output=', array([[ 0.28811866,  0.29948336,  0.3236185 ,  0.47553599,  0.6843847 ,
             0.50447232,  0.68630183, -0.51290929,  0.05509853, -0.4915415 ,
            -0.40329528, -0.3938058 , -0.10254639,  0.38953394,  0.28882599,
             0.2969259 ]], dtype=float32), ' expected=', [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], ' err=', 0.18160449)
    (' x=', 15, ' output=', array([[ 0.2887364 ,  0.29742014,  0.32021949,  0.47276866,  0.683173  ,
             0.50292063,  0.69102538, -0.51060057,  0.05603838, -0.4906354 ,
            -0.39959145, -0.39253896, -0.10030991,  0.39022303,  0.28924942,
             0.29847324]], dtype=float32), ' expected=', [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], ' err=', 0.15513293)



```python
# Regression result
```


```python

```


```python

```
