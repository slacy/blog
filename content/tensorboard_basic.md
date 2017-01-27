

```python
'''
Graph and Loss visualization using Tensorboard.
This example is using the MNIST database of handwritten digits
(http://yann.lecun.com/exdb/mnist/)

Author: Aymeric Damien
Project: https://github.com/aymericdamien/TensorFlow-Examples/
'''
```




    '\nGraph and Loss visualization using Tensorboard.\nThis example is using the MNIST database of handwritten digits\n(http://yann.lecun.com/exdb/mnist/)\n\nAuthor: Aymeric Damien\nProject: https://github.com/aymericdamien/TensorFlow-Examples/\n'




```python
import tensorflow as tf

# Import MINST data
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)
```

    Extracting /tmp/data/train-images-idx3-ubyte.gz
    Extracting /tmp/data/train-labels-idx1-ubyte.gz
    Extracting /tmp/data/t10k-images-idx3-ubyte.gz
    Extracting /tmp/data/t10k-labels-idx1-ubyte.gz



```python
# Parameters
learning_rate = 0.01
training_epochs = 25
batch_size = 100
display_step = 1
logs_path = '/tmp/tensorflow_logs/example'

# tf Graph Input
# mnist data image of shape 28*28=784
x = tf.placeholder(tf.float32, [None, 784], name='InputData')
# 0-9 digits recognition => 10 classes
y = tf.placeholder(tf.float32, [None, 10], name='LabelData')

# Set model weights
W = tf.Variable(tf.zeros([784, 10]), name='Weights')
b = tf.Variable(tf.zeros([10]), name='Bias')
```


```python
# Construct model and encapsulating all ops into scopes, making
# Tensorboard's Graph visualization more convenient
with tf.name_scope('Model'):
    # Model
    pred = tf.nn.softmax(tf.matmul(x, W) + b) # Softmax
with tf.name_scope('Loss'):
    # Minimize error using cross entropy
    cost = tf.reduce_mean(-tf.reduce_sum(y*tf.log(pred), reduction_indices=1))
with tf.name_scope('SGD'):
    # Gradient Descent
    optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)
with tf.name_scope('Accuracy'):
    # Accuracy
    acc = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
    acc = tf.reduce_mean(tf.cast(acc, tf.float32))

# Initializing the variables
init = tf.initialize_all_variables()

# Create a summary to monitor cost tensor
tf.scalar_summary("loss", cost)
# Create a summary to monitor accuracy tensor
tf.scalar_summary("accuracy", acc)
# Merge all summaries into a single op
merged_summary_op = tf.merge_all_summaries()
```

    WARNING:tensorflow:From <ipython-input-4-ead11f5f6d78>:18 in <module>.: initialize_all_variables (from tensorflow.python.ops.variables) is deprecated and will be removed after 2017-03-02.
    Instructions for updating:
    Use `tf.global_variables_initializer` instead.
    WARNING:tensorflow:From <ipython-input-4-ead11f5f6d78>:21 in <module>.: scalar_summary (from tensorflow.python.ops.logging_ops) is deprecated and will be removed after 2016-11-30.
    Instructions for updating:
    Please switch to tf.summary.scalar. Note that tf.summary.scalar uses the node name instead of the tag. This means that TensorFlow will automatically de-duplicate summary names based on the scope they are created in. Also, passing a tensor or list of tags to a scalar summary op is no longer supported.
    WARNING:tensorflow:From <ipython-input-4-ead11f5f6d78>:23 in <module>.: scalar_summary (from tensorflow.python.ops.logging_ops) is deprecated and will be removed after 2016-11-30.
    Instructions for updating:
    Please switch to tf.summary.scalar. Note that tf.summary.scalar uses the node name instead of the tag. This means that TensorFlow will automatically de-duplicate summary names based on the scope they are created in. Also, passing a tensor or list of tags to a scalar summary op is no longer supported.
    WARNING:tensorflow:From <ipython-input-4-ead11f5f6d78>:25 in <module>.: merge_all_summaries (from tensorflow.python.ops.logging_ops) is deprecated and will be removed after 2016-11-30.
    Instructions for updating:
    Please switch to tf.summary.merge_all.
    WARNING:tensorflow:From /home/slacy/src/tensorflow/env/local/lib/python2.7/site-packages/tensorflow/python/ops/logging_ops.py:264 in merge_all_summaries.: merge_summary (from tensorflow.python.ops.logging_ops) is deprecated and will be removed after 2016-11-30.
    Instructions for updating:
    Please switch to tf.summary.merge.



```python
# Launch the graph
with tf.Session() as sess:
    sess.run(init)

    # op to write logs to Tensorboard
    summary_writer = tf.train.SummaryWriter(logs_path, graph=tf.get_default_graph())

    # Training cycle
    for epoch in range(training_epochs):
        avg_cost = 0.
        total_batch = int(mnist.train.num_examples/batch_size)
        # Loop over all batches
        for i in range(total_batch):
            batch_xs, batch_ys = mnist.train.next_batch(batch_size)
            # Run optimization op (backprop), cost op (to get loss value)
            # and summary nodes
            _, c, summary = sess.run([optimizer, cost, merged_summary_op],
                                     feed_dict={x: batch_xs, y: batch_ys})
            # Write logs at every iteration
            summary_writer.add_summary(summary, epoch * total_batch + i)
            # Compute average loss
            avg_cost += c / total_batch
        # Display logs per epoch step
        if (epoch+1) % display_step == 0:
            print "Epoch:", '%04d' % (epoch+1), "cost=", "{:.9f}".format(avg_cost)

    print "Optimization Finished!"

    # Test model
    # Calculate accuracy
    print "Accuracy:", acc.eval({x: mnist.test.images, y: mnist.test.labels})

    print "Run the command line:\n" \
          "--> tensorboard --logdir=/tmp/tensorflow_logs " \
          "\nThen open http://0.0.0.0:6006/ into your web browser"
```

    WARNING:tensorflow:From <ipython-input-5-114f451f914d>:6 in <module>.: __init__ (from tensorflow.python.training.summary_io) is deprecated and will be removed after 2016-11-30.
    Instructions for updating:
    Please switch to tf.summary.FileWriter. The interface and behavior is the same; this is just a rename.
    Epoch: 0001 cost= 1.182138977
    Epoch: 0002 cost= 0.664712671
    Epoch: 0003 cost= 0.552637806
    Epoch: 0004 cost= 0.498585057
    Epoch: 0005 cost= 0.465485415
    Epoch: 0006 cost= 0.442553723
    Epoch: 0007 cost= 0.425481992
    Epoch: 0008 cost= 0.412176605
    Epoch: 0009 cost= 0.401382315
    Epoch: 0010 cost= 0.392372539
    Epoch: 0011 cost= 0.384789605
    Epoch: 0012 cost= 0.378123702
    Epoch: 0013 cost= 0.372390615
    Epoch: 0014 cost= 0.367258584
    Epoch: 0015 cost= 0.362734734
    Epoch: 0016 cost= 0.358609475
    Epoch: 0017 cost= 0.354891097
    Epoch: 0018 cost= 0.351447768
    Epoch: 0019 cost= 0.348329672
    Epoch: 0020 cost= 0.345413255
    Epoch: 0021 cost= 0.342736861
    Epoch: 0022 cost= 0.340226690
    Epoch: 0023 cost= 0.337903535
    Epoch: 0024 cost= 0.335745576
    Epoch: 0025 cost= 0.333722533
    Optimization Finished!
    Accuracy: 0.9138
    Run the command line:
    --> tensorboard --logdir=/tmp/tensorflow_logs 
    Then open http://0.0.0.0:6006/ into your web browser



```python
# Loss and accuracy Visualization
```


```python
# Graph Visualization
```


```python

```
