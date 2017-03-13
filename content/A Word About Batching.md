Title: A Word About Batching
Category: TensorFlow From The Ground Up
Tags: Python, TensorFlow, Jupyter
Date: 2/9/2017 1:10pm
Author: slacy
Status: draft
This is an **interlude** from my series [TensorFlow From The Ground Up]({category}tensorflow-from-the-ground-up).

In a previous post, [Learning to Add]({filename}Learning to Add.md) I showed simple code to run & train a neural network.  That code example trains "one example at a time".  This is generally *not* how you implement a typical large ML training system. 

Its much more typical to train in **batches**.  Batches are a way to pass a medium to large collection of training examples to our network, run the expensive calculations just once on the entire batch, then update the gradients and train on the next batch.   Because everything in TensorFlow is a *tensor* (a multi-dimensional array), the process of batching is nothing more than adding an extra dimension to all the tensors used in the system.  In fact, there are several parts of TensorFlow that assume that the first dimension of a tensor is the size of a batch.  Here is an example using an unknown batch size:


```python
import tensorflow as tf

# This declares a batch of unknown size, of tensors of size 4. 
ins = tf.placeholder(dtype=tf.float32, shape=(None, 4))

# Our weights and biases are declared as usual.  The batch size does 
# not effect their declaration. 
w = tf.Variable(
    expected_shape=(4, 3), dtype=tf.float32, 
    initial_value=tf.ones(shape=(4, 3)))
b = tf.Variable(
    expected_shape=(3,), dtype=tf.float32, 
    initial_value=tf.ones(shape=(3,)))

# We compute "out = ins * w + b" without worrying what the first dimension of 
# these tensors are. 
out = tf.add(tf.matmul(ins, w), b)

# When we print the shape of the final output, it has an unknown 
# size for the first dimension as well. 
print "Shape of intermediate =", out.get_shape()
```

    Shape of intermediate = (?, 3)

## Additional benefits of batching

Batching our training data can actually make training faster as well, and not just because the computation is more efficient.  Remember that we're training via *GradientDescent* (and similar algorithms).  These algorithms look at the current set of inputs, and decide how to tweak internally stored parameters to minimize the *loss function*.  

But, there are lots of cases where optimizing one training example has the opposite effect on other training examples.  These examples can tend to "See-saw" back and forth between two not very optimial sets of parameters during training.  You can think of each example as *pulling* the parameters in opposite directions.

When we batch, we give multiple training examples to the optimizer.  If two examples pull parmeters in opposite directions, then they will end up cancelling each other out, and other solutions will be tried.

There are several library functions within TensorFlow itself to facilitate batching, but here, I'm going to be doing the work myself, to make it more clear how batching really works.
## Examples

The example that I'm going to use an example is a 4-bit parity problem.  My input is going to be a Tensor of shape (4), with each value being either 0.0 or 1.0.  Expressed as a mathematical function, what I'd like to compute is: 

$$f(x_i)= \sum_{i=0}^n{x_i} \bmod{2}$$

The network we'll use will be a one-layer network with 16 nodes in the middle layer. 

So, here we go: 


```python
import tensorflow as tf 
import random

inputs = tf.placeholder(shape=(4,), dtype=tf.float32, name='y')
expected = tf.placeholder(shape=(1,), dtype=tf.float32, name='expected')

# We are constructing a middle layer of 2 perceptron nodes.  Weights and biases 
# are our w_i and v_i from the above equations. 
input_weight = tf.Variable(expected_shape=(4, 16), 
                           initial_value=tf.truncated_normal((4, 16), mean=0, stddev=0.1))
input_bias = tf.Variable(expected_shape=(1, 16), 
                         initial_value=tf.truncated_normal((1, 16), mean=0, stddev=0.1))

mid_layer = tf.nn.sigmoid(tf.add(tf.matmul(inputs, input_weight), input_bias))

out_weight = tf.Variable(expected_shape=(16, 1), 
                         initial_value=tf.truncated_normal((16, 1), mean=0, stddev=0.1))
out_bias = tf.Variable(expected_shape=(1, 1), 
                       initial_value=tf.truncated_normal((1, 1), mean=0, stddev=0.1))

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
