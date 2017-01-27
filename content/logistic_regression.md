

```python
# A logistic regression learning algorithm example using TensorFlow library.
# This example is using the MNIST database of handwritten digits 
# (http://yann.lecun.com/exdb/mnist/)

# Author: Aymeric Damien
# Project: https://github.com/aymericdamien/TensorFlow-Examples/
```


```python
import tensorflow as tf

# Import MINST data
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)
```

    Successfully downloaded train-images-idx3-ubyte.gz 9912422 bytes.
    Extracting /tmp/data/train-images-idx3-ubyte.gz
    Successfully downloaded train-labels-idx1-ubyte.gz 28881 bytes.
    Extracting /tmp/data/train-labels-idx1-ubyte.gz
    Successfully downloaded t10k-images-idx3-ubyte.gz 1648877 bytes.
    Extracting /tmp/data/t10k-images-idx3-ubyte.gz
    Successfully downloaded t10k-labels-idx1-ubyte.gz 4542 bytes.
    Extracting /tmp/data/t10k-labels-idx1-ubyte.gz



```python
# Parameters
learning_rate = 0.01
training_epochs = 25
batch_size = 100
display_step = 1

# tf Graph Input
x = tf.placeholder(tf.float32, [None, 784]) # mnist data image of shape 28*28=784
y = tf.placeholder(tf.float32, [None, 10]) # 0-9 digits recognition => 10 classes

# Set model weights
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

# Construct model
pred = tf.nn.softmax(tf.matmul(x, W) + b) # Softmax

# Minimize error using cross entropy
cost = tf.reduce_mean(-tf.reduce_sum(y*tf.log(pred), reduction_indices=1))
# Gradient Descent
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

# Initializing the variables
init = tf.initialize_all_variables()
```


```python
# Launch the graph
with tf.Session() as sess:
    sess.run(init)

    # Training cycle
    for epoch in range(training_epochs):
        avg_cost = 0.
        total_batch = int(mnist.train.num_examples/batch_size)
        # Loop over all batches
        for i in range(total_batch):
            batch_xs, batch_ys = mnist.train.next_batch(batch_size)
            # Fit training using batch data
            _, c = sess.run([optimizer, cost], feed_dict={x: batch_xs,
                                                          y: batch_ys})
            # Compute average loss
            avg_cost += c / total_batch
        # Display logs per epoch step
        if (epoch+1) % display_step == 0:
            print "Epoch:", '%04d' % (epoch+1), "cost=", "{:.9f}".format(avg_cost)

    print "Optimization Finished!"

    # Test model
    correct_prediction = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
    # Calculate accuracy for 3000 examples
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    print "Accuracy:", accuracy.eval({x: mnist.test.images[:3000], y: mnist.test.labels[:3000]})
```

    Epoch: 0001 cost= 1.182138977
    Epoch: 0002 cost= 0.664789904
    Epoch: 0003 cost= 0.552636867
    Epoch: 0004 cost= 0.498574648
    Epoch: 0005 cost= 0.465456409
    Epoch: 0006 cost= 0.442567715
    Epoch: 0007 cost= 0.425510132
    Epoch: 0008 cost= 0.412189296
    Epoch: 0009 cost= 0.401334072
    Epoch: 0010 cost= 0.392399208
    Epoch: 0011 cost= 0.384745641
    Epoch: 0012 cost= 0.378189677
    Epoch: 0013 cost= 0.372416052
    Epoch: 0014 cost= 0.367304044
    Epoch: 0015 cost= 0.362686445
    Epoch: 0016 cost= 0.358591286
    Epoch: 0017 cost= 0.354824922
    Epoch: 0018 cost= 0.351472360
    Epoch: 0019 cost= 0.348298853
    Epoch: 0020 cost= 0.345431258
    Epoch: 0021 cost= 0.342709450
    Epoch: 0022 cost= 0.340217283
    Epoch: 0023 cost= 0.337922486
    Epoch: 0024 cost= 0.335748573
    Epoch: 0025 cost= 0.333718066
    Optimization Finished!
    Accuracy: 0.888667

