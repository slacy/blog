

```python
import tensorflow as tf
import numpy
import random
```


```python
# tf Graph Input
num_inputs = 2
num_hidden = 2**16

inputs = tf.placeholder(dtype=tf.float32, shape=[None, num_inputs], name="inputs")
expected = tf.placeholder(dtype=tf.float32, shape=[None, 1], name="expected")

iw = tf.Variable(expected_shape=[num_inputs, num_hidden], name="input_weights", 
                 initial_value=tf.truncated_normal([num_inputs, num_hidden], stddev=0.25))
ib = tf.Variable(expected_shape=[1, num_hidden], name="input_biases", 
                 initial_value=tf.truncated_normal([1, num_hidden], stddev=0.25))

# Middle "hidden" layer values of the network 
l = tf.nn.relu(tf.add(tf.matmul(inputs, iw), ib))

# Weight and biases used to turn hidden layer into final output value. 
ow = tf.Variable(expected_shape=[num_hidden, 1], name="output_weight", 
                 initial_value=tf.truncated_normal([num_hidden, 1], stddev=0.25))
ob = tf.Variable(expected_shape=[1, 1], name="output_bias", 
                 initial_value=tf.truncated_normal([1, 1], stddev=0.25))

output = tf.add(tf.matmul(l, ow), ob)

# We compute error as the mean square difference 
error = tf.reduce_mean(tf.pow(tf.subtract(output, expected), 2))
```


```python
# Parameters
learning_rate = 0.0001 

# Gradient descent
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(error)
```


```python
training_steps = 15000

min = -1
max = 5

display_step = 100
batch_size = 250

# Launch the graph
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    
    for epoch in range(training_steps):
        data = { inputs: [], expected: []}
        for b in range(batch_size):
            x = random.uniform(min,max)
            y = random.uniform(min,max)
            data[inputs].append([x,y])
            data[expected].append([x*y,])
        sess.run(optimizer, feed_dict=data)

        if epoch % display_step == 0:
#           print "data=", data 
            e = sess.run(error, feed_dict=data)
            print "Epoch:", epoch, " error=", e
    print "iw= ", sess.run(iw)
    print "ib= ", sess.run(ib)
    print "ow= ", sess.run(ow)
    print "ob= ", sess.run(ob)
    for x in range(min, max):
        for y in range(min, max):
            data = {inputs: [[x,y],], expected: [[x*y,],]}
            print "x=", x, " y=", y, " out=", sess.run(output, feed_dict=data)
```

    Epoch: 0  error= 5558.23
    Epoch: 100  error= 11097.4
    Epoch: 200  error= 4815.07
    Epoch: 300  error= 328.96
    Epoch: 400  error= 561.612
    Epoch: 500  error= 397.593
    Epoch: 600  error= 194.758
    Epoch: 700  error= 144.604
    Epoch: 800  error= 185.569
    Epoch: 900  error= 128.551
    Epoch: 1000  error= 130.063
    Epoch: 1100  error= 114.86
    Epoch: 1200  error= 150.941
    Epoch: 1300  error= 71.6601
    Epoch: 1400  error= 38.9361
    Epoch: 1500  error= 25.3115
    Epoch: 1600  error= 41.65
    Epoch: 1700  error= 52.1016
    Epoch: 1800  error= 29.0106
    Epoch: 1900  error= 45.9973
    Epoch: 2000  error= 167.69
    Epoch: 2100  error= 42.9436
    Epoch: 2200  error= 67.1462
    Epoch: 2300  error= 11.8913
    Epoch: 2400  error= 15.9855
    Epoch: 2500  error= 11.3068
    Epoch: 2600  error= 21.6484
    Epoch: 2700  error= 11.6775
    Epoch: 2800  error= 10.828
    Epoch: 2900  error= 20.1986



    ---------------------------------------------------------------------------

    KeyboardInterrupt                         Traceback (most recent call last)

    <ipython-input-96-1ee70506aeee> in <module>()
         18             data[inputs].append([x,y])
         19             data[expected].append([x*y,])
    ---> 20         sess.run(optimizer, feed_dict=data)
         21 
         22         if epoch % display_step == 0:


    /home/slacy/src/tensorflow/env/local/lib/python2.7/site-packages/tensorflow/python/client/session.pyc in run(self, fetches, feed_dict, options, run_metadata)
        764     try:
        765       result = self._run(None, fetches, feed_dict, options_ptr,
    --> 766                          run_metadata_ptr)
        767       if run_metadata:
        768         proto_data = tf_session.TF_GetBuffer(run_metadata_ptr)


    /home/slacy/src/tensorflow/env/local/lib/python2.7/site-packages/tensorflow/python/client/session.pyc in _run(self, handle, fetches, feed_dict, options, run_metadata)
        962     if final_fetches or final_targets:
        963       results = self._do_run(handle, final_targets, final_fetches,
    --> 964                              feed_dict_string, options, run_metadata)
        965     else:
        966       results = []


    /home/slacy/src/tensorflow/env/local/lib/python2.7/site-packages/tensorflow/python/client/session.pyc in _do_run(self, handle, target_list, fetch_list, feed_dict, options, run_metadata)
       1012     if handle is None:
       1013       return self._do_call(_run_fn, self._session, feed_dict, fetch_list,
    -> 1014                            target_list, options, run_metadata)
       1015     else:
       1016       return self._do_call(_prun_fn, self._session, handle, feed_dict,


    /home/slacy/src/tensorflow/env/local/lib/python2.7/site-packages/tensorflow/python/client/session.pyc in _do_call(self, fn, *args)
       1019   def _do_call(self, fn, *args):
       1020     try:
    -> 1021       return fn(*args)
       1022     except errors.OpError as e:
       1023       message = compat.as_text(e.message)


    /home/slacy/src/tensorflow/env/local/lib/python2.7/site-packages/tensorflow/python/client/session.pyc in _run_fn(session, feed_dict, fetch_list, target_list, options, run_metadata)
       1001         return tf_session.TF_Run(session, options,
       1002                                  feed_dict, fetch_list, target_list,
    -> 1003                                  status, run_metadata)
       1004 
       1005     def _prun_fn(session, handle, feed_dict, fetch_list):


    KeyboardInterrupt: 



```python
# Regression result
```


```python

```


```python

```
