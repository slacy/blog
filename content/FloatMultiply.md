

```python
import tensorflow as tf 
import random 

ENC_SIZE = 4
ENC_LAYERSIZE = 50
DEC_LAYERSIZE = 50
LEARN_LAYERSIZE = 50
RANGE = 10

def func(x,y): return x*y

def encode_float(input_tensor):
    with tf.variable_scope("encode", reuse=tf.AUTO_REUSE):
        iw_1 = tf.get_variable("iw_1", shape=[1,ENC_LAYERSIZE])
        ib_1 = tf.get_variable("ib_1", shape=[ENC_LAYERSIZE,])
        l1 = tf.nn.relu(tf.add(tf.matmul(input_tensor, iw_1), ib_1))
        
        iw_2 = tf.get_variable("iw_2", shape=[ENC_LAYERSIZE,ENC_LAYERSIZE/2])
        ib_2 = tf.get_variable("ib_2", shape=[ENC_LAYERSIZE/2,])
        l2 = tf.nn.relu(tf.add(tf.matmul(l1, iw_2), ib_2))
        
        iw_3 = tf.get_variable("iw_3", shape=[ENC_LAYERSIZE/2,ENC_SIZE])
        ib_3 = tf.get_variable("ib_3", shape=[ENC_SIZE,])
        l3 = tf.nn.relu(tf.add(tf.matmul(l2, iw_3), ib_3))
    return l3

def decode_float(input_encoded):
    with tf.variable_scope("decode", reuse=tf.AUTO_REUSE):
        iw_1 = tf.get_variable("iw_1", shape=[ENC_SIZE,DEC_LAYERSIZE])
        ib_1 = tf.get_variable("ib_1", shape=[DEC_LAYERSIZE,])
        l1 = tf.nn.relu(tf.add(tf.matmul(input_encoded, iw_1), ib_1))
        
        iw_2 = tf.get_variable("iw_2", shape=[DEC_LAYERSIZE,DEC_LAYERSIZE/2])
        ib_2 = tf.get_variable("ib_2", shape=[DEC_LAYERSIZE/2,])
        l2 = tf.nn.relu(tf.add(tf.matmul(l1, iw_2), ib_2))
        
        iw_3 = tf.get_variable("iw_3", shape=[DEC_LAYERSIZE/2,1])
        ib_3 = tf.get_variable("ib_3", shape=[1,])
        l3 = tf.add(tf.matmul(l2, iw_3), ib_3)
    return l3 

def learn_func(x,y):
    x_enc = encode_float(x)
    y_enc = encode_float(y)
    expected_enc = encode_float(expected)
    inputs = tf.concat([x_enc,y_enc],1)
    with tf.variable_scope("learn", reuse=tf.AUTO_REUSE):
        iw_1 = tf.get_variable("iw_1", shape=(2*ENC_SIZE, LEARN_LAYERSIZE))
        ib_1 = tf.get_variable("ib_1", shape=(LEARN_LAYERSIZE,))
        l1 = tf.nn.relu(tf.add(tf.matmul(inputs, iw_1), ib_1))
        
        iw_2 = tf.get_variable("iw_2", shape=(LEARN_LAYERSIZE, LEARN_LAYERSIZE/2))
        ib_2 = tf.get_variable("ib_2", shape=(LEARN_LAYERSIZE/2,))
        l2 = tf.nn.relu(tf.add(tf.matmul(l1, iw_2), ib_2))
        
        iw_3 = tf.get_variable("iw_3", shape=(LEARN_LAYERSIZE/2, ENC_SIZE))
        ib_3 = tf.get_variable("ib_3", shape=(ENC_SIZE,))
        l3 = tf.nn.relu(tf.add(tf.matmul(l2, iw_3), ib_3))
    return l3 


x = tf.placeholder(shape=(None,1), dtype=tf.float32, name='x')
y = tf.placeholder(shape=(None,1), dtype=tf.float32, name='y')
expected = tf.placeholder(shape=(None,1), dtype=tf.float32, name='expected')

learned = learn_func(x,y)
# loss = tf.reduce_mean(tf.losses.mean_squared_error(learned, encode_float(expected)) ) + tf.reduce_mean(tf.losses.mean_squared_error(expected, decode_float(learned)))
loss = (tf.losses.mean_squared_error(expected, decode_float(learned)) + 
        tf.losses.mean_squared_error(encode_float(expected), learned) + 
        tf.losses.mean_squared_error(x, decode_float(encode_float(x)))  + 
        tf.losses.mean_squared_error(y, decode_float(encode_float(y))) +
        tf.losses.mean_squared_error(expected, decode_float(encode_float(expected))))

with tf.Session() as sess: 
    with tf.variable_scope("sess", reuse=tf.AUTO_REUSE):
        optimizer = tf.train.AdamOptimizer().minimize(loss)
    sess.run([tf.local_variables_initializer(), 
              tf.global_variables_initializer()])
    
    print "TRAIN"
    train_iterations = 25000
    batch_size = 100 
    for i in xrange(train_iterations):
        feed = { x:[], y:[], expected:[]}
        for b in range(batch_size):
            ix = random.uniform(-RANGE, RANGE)
            iy = random.uniform(-RANGE, RANGE)
            e = func(ix, iy)
            feed[x].append([ix,])
            feed[y].append([iy,])
            feed[expected].append([e,])
        _, l = sess.run([optimizer, loss], feed_dict=feed)
        if i % 2500 == 0:
            print "i=",i," loss=", l
    for i in range(-RANGE, RANGE):
        f = float(i)
        enc = sess.run([encode_float([[f,],])])
        print "enc = ", f, " = ", enc
        print "dec = ", sess.run([decode_float(enc[0])])
    for i in range(25):
        tx = random.uniform(-RANGE,RANGE)
        ty = random.uniform(-RANGE,RANGE) 
        te = func(tx, ty) 
        print tx, ty, te 
#        print "learn = ", sess.run([learn_func([[tx,],],[[ty,],])], feed_dict={x:[[tx,],], y:[[ty,],], expected:[[te,],]})
        print "decode_learn = ", sess.run([decode_float(learn_func([[tx,],],[[ty,],]))], feed_dict={x:[[tx,],], y:[[ty,],], expected:[[te,],]})
        print "loss = ", sess.run([loss], feed_dict={x:[[tx,],], y:[[ty,],], expected:[[te,],]})

```

    TRAIN
    i= 0  loss= 2017.81
    i= 2500  loss= 0.960452
    i= 5000  loss= 0.52289
    i= 7500  loss= 0.28749
    i= 10000  loss= 0.121323
    i= 12500  loss= 0.161903
    i= 15000  loss= 0.271373
    i= 17500  loss= 0.103738
    i= 20000  loss= 0.164337
    i= 22500  loss= 0.11577
    enc =  -10.0  =  [array([[ 2.34517288,  0.27773932,  0.        ,  0.        ]], dtype=float32)]
    dec =  [array([[-9.99434853]], dtype=float32)]
    enc =  -9.0  =  [array([[ 2.08889246,  0.11650184,  0.        ,  0.        ]], dtype=float32)]
    dec =  [array([[-8.9802351]], dtype=float32)]
    enc =  -8.0  =  [array([[ 1.82675648,  0.        ,  0.        ,  0.0213536 ]], dtype=float32)]
    dec =  [array([[-7.99868107]], dtype=float32)]
    enc =  -7.0  =  [array([[ 1.5655961 ,  0.        ,  0.        ,  0.12094355]], dtype=float32)]
    dec =  [array([[-6.97428942]], dtype=float32)]
    enc =  -6.0  =  [array([[ 1.3299427 ,  0.        ,  0.        ,  0.18070233]], dtype=float32)]
    dec =  [array([[-5.96759796]], dtype=float32)]
    enc =  -5.0  =  [array([[ 1.10779285,  0.        ,  0.        ,  0.22334749]], dtype=float32)]
    dec =  [array([[-4.97298908]], dtype=float32)]
    enc =  -4.0  =  [array([[ 0.88985413,  0.        ,  0.        ,  0.25108016]], dtype=float32)]
    dec =  [array([[-3.98106694]], dtype=float32)]
    enc =  -3.0  =  [array([[ 0.67933232,  0.        ,  0.        ,  0.28351384]], dtype=float32)]
    dec =  [array([[-2.99213147]], dtype=float32)]
    enc =  -2.0  =  [array([[ 0.4711892 ,  0.        ,  0.        ,  0.32135177]], dtype=float32)]
    dec =  [array([[-2.00821304]], dtype=float32)]
    enc =  -1.0  =  [array([[ 0.24630851,  0.        ,  0.        ,  0.37405425]], dtype=float32)]
    dec =  [array([[-0.99869615]], dtype=float32)]
    enc =  0.0  =  [array([[ 0.03558221,  0.        ,  0.        ,  0.44536012]], dtype=float32)]
    dec =  [array([[ 0.00421314]], dtype=float32)]
    enc =  1.0  =  [array([[ 0.        ,  0.        ,  0.        ,  0.65894413]], dtype=float32)]
    dec =  [array([[ 0.98836178]], dtype=float32)]
    enc =  2.0  =  [array([[ 0.        ,  0.        ,  0.        ,  0.93758082]], dtype=float32)]
    dec =  [array([[ 1.97765827]], dtype=float32)]
    enc =  3.0  =  [array([[ 0.        ,  0.        ,  0.        ,  1.21227872]], dtype=float32)]
    dec =  [array([[ 2.97535276]], dtype=float32)]
    enc =  4.0  =  [array([[ 0.        ,  0.        ,  0.        ,  1.50549245]], dtype=float32)]
    dec =  [array([[ 3.98856091]], dtype=float32)]
    enc =  5.0  =  [array([[ 0.        ,  0.        ,  0.        ,  1.83683205]], dtype=float32)]
    dec =  [array([[ 4.98420858]], dtype=float32)]
    enc =  6.0  =  [array([[ 0.        ,  0.        ,  0.        ,  2.20098615]], dtype=float32)]
    dec =  [array([[ 5.99874353]], dtype=float32)]
    enc =  7.0  =  [array([[ 0.08913583,  0.        ,  0.        ,  2.56915545]], dtype=float32)]
    dec =  [array([[ 7.02822018]], dtype=float32)]
    enc =  8.0  =  [array([[ 0.20194757,  0.        ,  0.        ,  2.95653033]], dtype=float32)]
    dec =  [array([[ 8.02958202]], dtype=float32)]
    enc =  9.0  =  [array([[ 0.35159034,  0.        ,  0.        ,  3.34571338]], dtype=float32)]
    dec =  [array([[ 9.01790333]], dtype=float32)]
    -0.932180553861 -8.17295039823 7.61866542891
    decode_learn =  [array([[ 7.6894989]], dtype=float32)]
    loss =  [0.0095091052]
    9.09395357235 8.34657733974 75.9033868156
    decode_learn =  [array([[ 76.81848145]], dtype=float32)]
    loss =  [0.92132831]
    1.75145909591 -9.69869143292 -16.9868613286
    decode_learn =  [array([[-16.85243988]], dtype=float32)]
    loss =  [0.028132619]
    -2.36132638316 8.18150637095 -19.3192068477
    decode_learn =  [array([[-19.1207428]], dtype=float32)]
    loss =  [0.055181146]
    -0.383012405425 -2.13955802902 0.819477267241
    decode_learn =  [array([[ 0.45101666]], dtype=float32)]
    loss =  [0.14617206]
    -3.50569579493 8.5337046779 -29.9165726045
    decode_learn =  [array([[-29.75508118]], dtype=float32)]
    loss =  [0.056257203]
    -8.96061235068 5.47629320228 -49.0709405043
    decode_learn =  [array([[-49.15358353]], dtype=float32)]
    loss =  [0.066341698]
    0.187158737808 -6.850027127 -1.28204243104
    decode_learn =  [array([[-1.39929688]], dtype=float32)]
    loss =  [0.028878247]
    7.01899093253 2.63024562649 18.4616702027
    decode_learn =  [array([[ 18.48875999]], dtype=float32)]
    loss =  [0.0030565308]
    0.0721336041956 -2.7742220189 -0.200114633062
    decode_learn =  [array([[-0.09706245]], dtype=float32)]
    loss =  [0.014328312]
    -9.3183154506 -7.79880152487 72.6716927454
    decode_learn =  [array([[ 72.66538239]], dtype=float32)]
    loss =  [0.073292434]
    1.03343368559 -1.83969144217 -1.90119910742
    decode_learn =  [array([[-1.72055602]], dtype=float32)]
    loss =  [0.059457414]
    0.999796294812 5.46218545813 5.46107278262
    decode_learn =  [array([[ 5.60559654]], dtype=float32)]
    loss =  [0.022058684]
    6.64454526777 6.35499863653 42.226076117
    decode_learn =  [array([[ 42.42594528]], dtype=float32)]
    loss =  [0.06389305]
    6.84156387187 2.20681914442 15.0980941302
    decode_learn =  [array([[ 15.24669456]], dtype=float32)]
    loss =  [0.0312635]
    7.69201315519 -9.09742561113 -69.9775174791
    decode_learn =  [array([[-70.05825806]], dtype=float32)]
    loss =  [0.1274592]
    -5.32030455225 -6.31825306712 33.6150305552
    decode_learn =  [array([[ 33.39521408]], dtype=float32)]
    loss =  [0.067687556]
    -2.82029782633 -0.914909326367 2.58031678444
    decode_learn =  [array([[ 2.69408011]], dtype=float32)]
    loss =  [0.0133528]
    -9.59641466692 -7.43909095982 71.3886015954
    decode_learn =  [array([[ 71.28066254]], dtype=float32)]
    loss =  [0.083082095]
    6.35535183178 3.12143862348 19.8378406735
    decode_learn =  [array([[ 20.27935982]], dtype=float32)]
    loss =  [0.19964676]
    9.20595996217 -5.65025032575 -52.0159782751
    decode_learn =  [array([[-51.92444992]], dtype=float32)]
    loss =  [0.073752053]
    3.60618108492 -6.80127871649 -24.5266426607
    decode_learn =  [array([[-24.66298485]], dtype=float32)]
    loss =  [0.043813132]
    4.3044464244 0.156327307815 0.672902521158
    decode_learn =  [array([[ 0.71339422]], dtype=float32)]
    loss =  [0.0029237957]
    -1.10216253922 -5.79164638033 6.38333568078
    decode_learn =  [array([[ 6.56668091]], dtype=float32)]
    loss =  [0.037614603]
    -8.34749014921 7.63073085559 -63.6974506483
    decode_learn =  [array([[-63.42816544]], dtype=float32)]
    loss =  [0.15896809]



```python

```


```python

```
