Title: Learning to Multiply, Part 1
Category: TensorFlow From The Ground Up
Tags: Python, TensorFlow, Jupyter
Date: 2/9/2017 1:00pm
Author: slacy
Status: draft

This is the **fourth** post of my series [TensorFlow From The Ground Up]({category}tensorflow-from-the-ground-up).

In my previous post, [Learning to Add]({filename}/Learning to Add.md) I demonstrated a toy neural network that was able to learn how to add two real-valued variables.  It learned a general formula that applied to *any* real-valued input values, even though we only trained it on values in the range [0,20].  (Note: This is *really* amazing!) 

Now, we're going to start to ask some more difficult questions:

> How do we know when a network is able to learn a function, and when it isn't? 
>
> What parameters can we tweak help a network to learn? 
>
> Is it possible that some functions are "unlearnable"? 


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
inputs = tf.reshape(tf.concat(0, [x,y]), (1,2))

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
    i= 0  loss= [ 343.70489502]
    i= 1000  loss= [ 0.00222525]
    i= 2000  loss= [  9.52743212e-05]
    i= 3000  loss= [  7.60952462e-05]
    i= 4000  loss= [  2.87974472e-05]
    i= 5000  loss= [  2.28197314e-06]
    i= 6000  loss= [  6.43522071e-08]
    i= 7000  loss= [  3.78495315e-08]
    i= 8000  loss= [  1.07751148e-05]
    i= 9000  loss= [  5.25324140e-09]
    VALIDATE
    x= -15  y= 29  out= 14.0  loss= [  1.78260962e-10]
    x= -19  y= -11  out= -29.9999  loss= [  1.88592821e-08]
    x= 7  y= 9  out= 16.0  loss= [ 0.]
    x= 3  y= 9  out= 12.0  loss= [  9.09494702e-11]
    x= -1  y= -35  out= -35.9998  loss= [  2.94676283e-08]
    x= 21  y= -13  out= 8.00004  loss= [  1.60434865e-09]
    x= -39  y= 7  out= -31.9999  loss= [  1.63308869e-08]
    x= -3  y= 17  out= 14.0  loss= [  3.63797881e-12]
    x= 21  y= 29  out= 49.9999  loss= [  1.14087015e-08]
    x= -33  y= 3  out= -29.9999  loss= [  1.53704605e-08]
    [array([[-0.73145592,  0.41055757],
           [-0.71037835,  0.44684216]], dtype=float32), array([[ 0.12508716,  0.19557403]], dtype=float32), array([[-1.03099132],
           [ 0.59887499]], dtype=float32), array([[ 0.01188867]], dtype=float32)]

## You should play with this code a little bit.

Here's a collection of random ideas for how to play around with the code example above and gain some insights:

* Modify the "f()" function to try other linear combinations of x & y.  Can it learn $x-y$?  Can it learn $0.5x + 0.75y - 0.33$? 
* Modify the size of the middle layer.  We use 2 middle layer nodes.  What if you use 200?  How does that impact learning rate?   
* Modify the size of the middle layer, and have it try to learn something "Hard" like $x\cdot y$. Did it work?  Do you have any thoughts about why or why not?
