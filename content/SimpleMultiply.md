

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
learning_rate = 0.000001 

# Gradient descent
# optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(error)
optimizer = tf.train.RMSPropOptimizer(learning_rate).minimize(error)

```


```python
training_steps = 25000

min = -1
max = 5

display_step = 100
batch_size = 1500

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

    Epoch: 0  error= 236.22
    Epoch: 100  error= 93.4262
    Epoch: 200  error= 23.571
    Epoch: 300  error= 5.11089
    Epoch: 400  error= 3.28986
    Epoch: 500  error= 2.32373
    Epoch: 600  error= 1.42074
    Epoch: 700  error= 1.07786
    Epoch: 800  error= 0.819217
    Epoch: 900  error= 0.560817
    Epoch: 1000  error= 0.510289
    Epoch: 1100  error= 0.375189
    Epoch: 1200  error= 0.327775
    Epoch: 1300  error= 0.251442
    Epoch: 1400  error= 0.222358
    Epoch: 1500  error= 0.187605
    Epoch: 1600  error= 0.173659
    Epoch: 1700  error= 0.146098
    Epoch: 1800  error= 0.128391
    Epoch: 1900  error= 0.106425
    Epoch: 2000  error= 0.095566
    Epoch: 2100  error= 0.0797614
    Epoch: 2200  error= 0.0716584
    Epoch: 2300  error= 0.0706716
    Epoch: 2400  error= 0.0620029
    Epoch: 2500  error= 0.0584875
    Epoch: 2600  error= 0.0509813
    Epoch: 2700  error= 0.0487353
    Epoch: 2800  error= 0.0438902
    Epoch: 2900  error= 0.0393957
    Epoch: 3000  error= 0.0357144
    Epoch: 3100  error= 0.0314247
    Epoch: 3200  error= 0.0325135
    Epoch: 3300  error= 0.0273895
    Epoch: 3400  error= 0.0297003
    Epoch: 3500  error= 0.02791
    Epoch: 3600  error= 0.0250562
    Epoch: 3700  error= 0.0238952
    Epoch: 3800  error= 0.0238257
    Epoch: 3900  error= 0.0224855
    Epoch: 4000  error= 0.0209293
    Epoch: 4100  error= 0.0183032
    Epoch: 4200  error= 0.0206868
    Epoch: 4300  error= 0.0193751
    Epoch: 4400  error= 0.016807
    Epoch: 4500  error= 0.0158298
    Epoch: 4600  error= 0.0167773
    Epoch: 4700  error= 0.0147829
    Epoch: 4800  error= 0.0135377
    Epoch: 4900  error= 0.0133851
    Epoch: 5000  error= 0.0122205
    Epoch: 5100  error= 0.0127108
    Epoch: 5200  error= 0.0122772
    Epoch: 5300  error= 0.0118821
    Epoch: 5400  error= 0.0110264
    Epoch: 5500  error= 0.0103373
    Epoch: 5600  error= 0.0107211
    Epoch: 5700  error= 0.0119572
    Epoch: 5800  error= 0.010162
    Epoch: 5900  error= 0.0108409
    Epoch: 6000  error= 0.0106528
    Epoch: 6100  error= 0.00992237
    Epoch: 6200  error= 0.00943248
    Epoch: 6300  error= 0.00893717
    Epoch: 6400  error= 0.0119289
    Epoch: 6500  error= 0.00879048
    Epoch: 6600  error= 0.00794716
    Epoch: 6700  error= 0.00860705
    Epoch: 6800  error= 0.00746628
    Epoch: 6900  error= 0.00732391
    Epoch: 7000  error= 0.00805103
    Epoch: 7100  error= 0.00790451
    Epoch: 7200  error= 0.00731824
    Epoch: 7300  error= 0.00753699
    Epoch: 7400  error= 0.00681168
    Epoch: 7500  error= 0.00727462
    Epoch: 7600  error= 0.00632464
    Epoch: 7700  error= 0.00652351
    Epoch: 7800  error= 0.00827558
    Epoch: 7900  error= 0.00595297
    Epoch: 8000  error= 0.00593832
    Epoch: 8100  error= 0.00591887
    Epoch: 8200  error= 0.00669949
    Epoch: 8300  error= 0.00617826
    Epoch: 8400  error= 0.00634989
    Epoch: 8500  error= 0.0057334
    Epoch: 8600  error= 0.00591615
    Epoch: 8700  error= 0.00588457
    Epoch: 8800  error= 0.00569794
    Epoch: 8900  error= 0.00544708
    Epoch: 9000  error= 0.00512874
    Epoch: 9100  error= 0.00503869
    Epoch: 9200  error= 0.00550106
    Epoch: 9300  error= 0.00544836
    Epoch: 9400  error= 0.00591172
    Epoch: 9500  error= 0.00538685
    Epoch: 9600  error= 0.00553367
    Epoch: 9700  error= 0.00535416
    Epoch: 9800  error= 0.00494688
    Epoch: 9900  error= 0.0051567
    Epoch: 10000  error= 0.00466216
    Epoch: 10100  error= 0.00503215
    Epoch: 10200  error= 0.00520053
    Epoch: 10300  error= 0.00494094
    Epoch: 10400  error= 0.0052913
    Epoch: 10500  error= 0.00458573
    Epoch: 10600  error= 0.00488938
    Epoch: 10700  error= 0.00460864
    Epoch: 10800  error= 0.0045662
    Epoch: 10900  error= 0.00441212
    Epoch: 11000  error= 0.00478338
    Epoch: 11100  error= 0.00467129
    Epoch: 11200  error= 0.00394244
    Epoch: 11300  error= 0.00455772
    Epoch: 11400  error= 0.00487883
    Epoch: 11500  error= 0.00375408
    Epoch: 11600  error= 0.00400563
    Epoch: 11700  error= 0.00437783
    Epoch: 11800  error= 0.00414098
    Epoch: 11900  error= 0.00344148
    Epoch: 12000  error= 0.00382295
    Epoch: 12100  error= 0.00342054
    Epoch: 12200  error= 0.00364111
    Epoch: 12300  error= 0.00368368
    Epoch: 12400  error= 0.00415219
    Epoch: 12500  error= 0.00367242
    Epoch: 12600  error= 0.00338886
    Epoch: 12700  error= 0.00367757
    Epoch: 12800  error= 0.00414692
    Epoch: 12900  error= 0.00451318
    Epoch: 13000  error= 0.0045011
    Epoch: 13100  error= 0.003651
    Epoch: 13200  error= 0.00490979
    Epoch: 13300  error= 0.00406448
    Epoch: 13400  error= 0.00342392
    Epoch: 13500  error= 0.0037095
    Epoch: 13600  error= 0.00383414
    Epoch: 13700  error= 0.00300014
    Epoch: 13800  error= 0.00347293
    Epoch: 13900  error= 0.00379729
    Epoch: 14000  error= 0.00363394
    Epoch: 14100  error= 0.00358356
    Epoch: 14200  error= 0.003521
    Epoch: 14300  error= 0.00370079
    Epoch: 14400  error= 0.00359526
    Epoch: 14500  error= 0.00302048
    Epoch: 14600  error= 0.00329787
    Epoch: 14700  error= 0.00378161
    Epoch: 14800  error= 0.00339221
    Epoch: 14900  error= 0.00313892
    Epoch: 15000  error= 0.00351523
    Epoch: 15100  error= 0.00344298
    Epoch: 15200  error= 0.00296464
    Epoch: 15300  error= 0.00368842
    Epoch: 15400  error= 0.00318548
    Epoch: 15500  error= 0.00364832
    Epoch: 15600  error= 0.00355409
    Epoch: 15700  error= 0.00327498
    Epoch: 15800  error= 0.00319262
    Epoch: 15900  error= 0.00328918
    Epoch: 16000  error= 0.00229035
    Epoch: 16100  error= 0.00376924
    Epoch: 16200  error= 0.00255191
    Epoch: 16300  error= 0.00364323
    Epoch: 16400  error= 0.00285774
    Epoch: 16500  error= 0.00368444
    Epoch: 16600  error= 0.00325779
    Epoch: 16700  error= 0.00315436
    Epoch: 16800  error= 0.00347181
    Epoch: 16900  error= 0.00304173
    Epoch: 17000  error= 0.00294682
    Epoch: 17100  error= 0.00268271
    Epoch: 17200  error= 0.00351474
    Epoch: 17300  error= 0.00369607
    Epoch: 17400  error= 0.00299194
    Epoch: 17500  error= 0.00250255
    Epoch: 17600  error= 0.00284093
    Epoch: 17700  error= 0.00282319
    Epoch: 17800  error= 0.00303398
    Epoch: 17900  error= 0.00278201
    Epoch: 18000  error= 0.00253555
    Epoch: 18100  error= 0.0032777
    Epoch: 18200  error= 0.00285717
    Epoch: 18300  error= 0.00312494
    Epoch: 18400  error= 0.0034845
    Epoch: 18500  error= 0.00258098
    Epoch: 18600  error= 0.00251161
    Epoch: 18700  error= 0.00284433
    Epoch: 18800  error= 0.00251673
    Epoch: 18900  error= 0.00297082
    Epoch: 19000  error= 0.00292156
    Epoch: 19100  error= 0.00277245
    Epoch: 19200  error= 0.00263444
    Epoch: 19300  error= 0.0026663
    Epoch: 19400  error= 0.00256487
    Epoch: 19500  error= 0.0035729
    Epoch: 19600  error= 0.00252277
    Epoch: 19700  error= 0.00264953
    Epoch: 19800  error= 0.00307365
    Epoch: 19900  error= 0.00271378
    Epoch: 20000  error= 0.00276662
    Epoch: 20100  error= 0.00316601
    Epoch: 20200  error= 0.00259499
    Epoch: 20300  error= 0.00240301
    Epoch: 20400  error= 0.00274851
    Epoch: 20500  error= 0.00240132
    Epoch: 20600  error= 0.00260275
    Epoch: 20700  error= 0.00274409
    Epoch: 20800  error= 0.00231824
    Epoch: 20900  error= 0.00248893
    Epoch: 21000  error= 0.00237294
    Epoch: 21100  error= 0.00256437
    Epoch: 21200  error= 0.00275233
    Epoch: 21300  error= 0.00223032
    Epoch: 21400  error= 0.00292883
    Epoch: 21500  error= 0.00235254
    Epoch: 21600  error= 0.00263653
    Epoch: 21700  error= 0.00185133
    Epoch: 21800  error= 0.00246028
    Epoch: 21900  error= 0.00298453
    Epoch: 22000  error= 0.00272532
    Epoch: 22100  error= 0.00258676
    Epoch: 22200  error= 0.00228931
    Epoch: 22300  error= 0.00224871
    Epoch: 22400  error= 0.00227443
    Epoch: 22500  error= 0.00272287
    Epoch: 22600  error= 0.00193787
    Epoch: 22700  error= 0.00236013
    Epoch: 22800  error= 0.00223893
    Epoch: 22900  error= 0.00265806
    Epoch: 23000  error= 0.00225004
    Epoch: 23100  error= 0.00217133
    Epoch: 23200  error= 0.00227572
    Epoch: 23300  error= 0.00204432
    Epoch: 23400  error= 0.00269673
    Epoch: 23500  error= 0.00207937
    Epoch: 23600  error= 0.00224656
    Epoch: 23700  error= 0.00195812
    Epoch: 23800  error= 0.00175827
    Epoch: 23900  error= 0.00184753
    Epoch: 24000  error= 0.00255181
    Epoch: 24100  error= 0.00209719
    Epoch: 24200  error= 0.00220772
    Epoch: 24300  error= 0.00212949
    Epoch: 24400  error= 0.00229058
    Epoch: 24500  error= 0.00223896
    Epoch: 24600  error= 0.00202421
    Epoch: 24700  error= 0.00278314
    Epoch: 24800  error= 0.00243685
    Epoch: 24900  error= 0.00208523
    iw=  [[-0.13832457 -0.29666355 -0.09946577 ..., -0.18739632  0.12222607
      -0.00772054]
     [ 0.05490867 -0.43673196  0.01846625 ..., -0.12114334 -0.28511515
       0.17321134]]
    ib=  [[-0.18122701 -0.0427603  -0.06061502 ...,  0.14707933  0.46014479
       0.33063027]]
    ow=  [[-0.03856875]
     [-0.07272913]
     [ 0.12136854]
     ..., 
     [ 0.21358374]
     [-0.12555818]
     [-0.07738612]]
    ob=  [[ 0.06259894]]
    x= -1  y= -1  out= [[ 1.04383266]]
    x= -1  y= 0  out= [[ 0.1298247]]
    x= -1  y= 1  out= [[-1.02054608]]
    x= -1  y= 2  out= [[-1.99334359]]
    x= -1  y= 3  out= [[-2.9889729]]
    x= -1  y= 4  out= [[-3.97836089]]
    x= 0  y= -1  out= [[-0.25396276]]
    x= 0  y= 0  out= [[ 0.084814]]
    x= 0  y= 1  out= [[-0.13342309]]
    x= 0  y= 2  out= [[-0.03011919]]
    x= 0  y= 3  out= [[ 0.0012977]]
    x= 0  y= 4  out= [[ 0.02858233]]
    x= 1  y= -1  out= [[-0.9770658]]
    x= 1  y= 0  out= [[ 0.01874881]]
    x= 1  y= 1  out= [[ 1.09798074]]
    x= 1  y= 2  out= [[ 1.98264003]]
    x= 1  y= 3  out= [[ 3.00385547]]
    x= 1  y= 4  out= [[ 4.04721212]]
    x= 2  y= -1  out= [[-2.01477933]]
    x= 2  y= 0  out= [[-0.01421658]]
    x= 2  y= 1  out= [[ 1.95496106]]
    x= 2  y= 2  out= [[ 4.04379892]]
    x= 2  y= 3  out= [[ 6.02573061]]
    x= 2  y= 4  out= [[ 8.04373837]]
    x= 3  y= -1  out= [[-2.95737863]]
    x= 3  y= 0  out= [[ 0.01650881]]
    x= 3  y= 1  out= [[ 3.00640893]]
    x= 3  y= 2  out= [[ 6.03501272]]
    x= 3  y= 3  out= [[ 9.08405113]]
    x= 3  y= 4  out= [[ 12.02849197]]
    x= 4  y= -1  out= [[-3.96769929]]
    x= 4  y= 0  out= [[ 0.01334815]]
    x= 4  y= 1  out= [[ 4.00321579]]
    x= 4  y= 2  out= [[ 8.04080009]]
    x= 4  y= 3  out= [[ 11.99170494]]
    x= 4  y= 4  out= [[ 16.04471397]]



```python
# Regression result
```


```python

```


```python

```
