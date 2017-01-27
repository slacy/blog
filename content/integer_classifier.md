

```python
# From Hello TensorFlow
# https://www.oreilly.com/learning/hello-tensorflow
```


```python
import tensorflow as tf
import random
import tensorflow.contrib.layers as layers
```


```python
i = tf.placeholder(tf.float32, shape=(1, 8), name="i")
l1 = layers.fully_connected(i, num_outputs=8)
l2 = layers.fully_connected(l1, num_outputs=3)
l3 = layers.fully_connected(l2, num_outputs=8)
n = l3[0].get_shape()[0]
loss = sum([tf.pow(l3[0][x]-i[0][x],2.0) for x in range(n)])
print i

```

    Tensor("i_24:0", shape=(1, 8), dtype=float32)



```python
optimizer = tf.train.GradientDescentOptimizer(0.025).minimize(loss)

```


```python

init = tf.global_variables_initializer() 
with tf.Session() as sess: 
    sess.run(init)
    for i in range(1000):
        v = random.randint(0,8)
        vv = [float(v==i) for i in range(8)]
        print v, vv
        sess.run(optimizer, feed_dict={i:[vv,]})
        print "Step %d" % i, " loss=%g " % sess.run(loss)
    print sess.run(l1), sess.run(l2), sess.run(l3)
```

    2 [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]



    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-57-3afb09e3d962> in <module>()
          7         vv = [float(v==i) for i in range(8)]
          8         print v, vv
    ----> 9         sess.run(optimizer, feed_dict={i:[vv,]})
         10         print "Step %d" % i, " loss=%g " % sess.run(loss)
         11     print sess.run(l1), sess.run(l2), sess.run(l3)


    /home/slacy/src/tensorflow/env/local/lib/python2.7/site-packages/tensorflow/python/client/session.pyc in run(self, fetches, feed_dict, options, run_metadata)
        764     try:
        765       result = self._run(None, fetches, feed_dict, options_ptr,
    --> 766                          run_metadata_ptr)
        767       if run_metadata:
        768         proto_data = tf_session.TF_GetBuffer(run_metadata_ptr)


    /home/slacy/src/tensorflow/env/local/lib/python2.7/site-packages/tensorflow/python/client/session.pyc in _run(self, handle, fetches, feed_dict, options, run_metadata)
        919           except Exception as e:
        920             raise TypeError('Cannot interpret feed_dict key as Tensor: '
    --> 921                             + e.args[0])
        922 
        923           if isinstance(subfeed_val, ops.Tensor):


    TypeError: Cannot interpret feed_dict key as Tensor: Can not convert a int into a Tensor.



```python

```
