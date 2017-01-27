

```python
# From Hello TensorFlow
# https://www.oreilly.com/learning/hello-tensorflow
```


```python
import tensorflow as tf
import random

x = tf.constant(2.0, name='input')
w1 = tf.Variable(random.uniform(-100,100), name='weight')
w2 = tf.Variable(random.uniform(-100,100), name='weight')
b = tf.Variable(random.uniform(-100,100), name='bias')
y = (x**2 * w2) + (x*w1) + b
y_ = tf.constant(0.0, name='correct_value')
loss = tf.pow(y - y_, 2, name='loss')
optimizer = tf.train.GradientDescentOptimizer(0.025).minimize(loss)

for value in [x, w, y, y_, loss]:
    tf.summary.scalar(value.op.name, value)
```


```python

init = tf.global_variables_initializer() 
with tf.Session() as sess: 
    sess.run(init)
    for i in range(1000):
        sess.run(optimizer)
        if i%100==0:
            print "Step %d" % i, " loss=%g " % sess.run(loss), " w=%g"% sess.run(w1)
    print sess.run(w2), sess.run(w1), sess.run(b)
```

    Step 0  loss=770.085   w=-24.7893
    Step 100  loss=1.42109e-14   w=-27.4322
    Step 200  loss=1.42109e-14   w=-27.4322
    Step 300  loss=1.42109e-14   w=-27.4322
    Step 400  loss=1.42109e-14   w=-27.4322
    Step 500  loss=1.42109e-14   w=-27.4322
    Step 600  loss=1.42109e-14   w=-27.4322
    Step 700  loss=1.42109e-14   w=-27.4322
    Step 800  loss=1.42109e-14   w=-27.4322
    Step 900  loss=1.42109e-14   w=-27.4322
    13.9073 -27.4322 -0.764954



```python

```
