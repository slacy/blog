

```python
import scipy.io
import scipy.misc
import tensorflow as tf
import numpy as np
import time
from IPython.display import Image
```


```python
content_file_name = 'UNIST.jpg'
style_file_name = 'rain princess.jpg'
```


```python
data = scipy.io.loadmat('./imagenet-vgg-verydeep-19.mat')

image_content = scipy.misc.imread('./images/'+content_file_name)
image_content = image_content.astype('float32')
image_content = np.ndarray.reshape(image_content,((1,) + image_content.shape)) # 1 means batch_size
#image_content = np.ndarray.reshape(image_content.shape + (1,)) it is needed to handle gray scale image 

image_style = scipy.misc.imread('./images/'+style_file_name)
image_style = image_style.astype('float32')
image_style = np.ndarray.reshape(image_style,((1,) + image_style.shape)) # 1 means batch_size
#image_style = np.ndarray.reshape(image_style.shape + (1,)) it is needed to handle gray scale image 
```


```python
# content image
Image(filename = './images/'+content_file_name)
```




![jpeg](neural_style_files/neural_style_3_0.jpeg)




```python
# style image
Image(filename = './images/'+style_file_name)
```




![jpeg](neural_style_files/neural_style_4_0.jpeg)




```python
def _conv_layer(input, weights, bias):
    conv = tf.nn.conv2d(input, tf.constant(weights), strides=(1, 1, 1, 1),
            padding='SAME')
    return tf.nn.bias_add(conv, bias)

def _pool_layer(input):
    return tf.nn.max_pool(input, ksize=(1, 2, 2, 1), strides=(1, 2, 2, 1),
            padding='SAME')

def preprocess(image, mean_pixel):
    return (image - mean_pixel).astype('float32')

def unprocess(image, mean_pixel):
    return (image + mean_pixel).astype('float32')
```


```python
def net(input_image):
    layers = (
        'conv1_1', 'relu1_1', 'conv1_2', 'relu1_2', 'pool1',

        'conv2_1', 'relu2_1', 'conv2_2', 'relu2_2', 'pool2',

        'conv3_1', 'relu3_1', 'conv3_2', 'relu3_2', 'conv3_3',
        'relu3_3', 'conv3_4', 'relu3_4', 'pool3',

        'conv4_1', 'relu4_1', 'conv4_2', 'relu4_2', 'conv4_3',
        'relu4_3', 'conv4_4', 'relu4_4', 'pool4',

        'conv5_1', 'relu5_1', 'conv5_2', 'relu5_2', 'conv5_3',
        'relu5_3', 'conv5_4', 'relu5_4'
    )
    weight = data['layers'][0]
    net = {}
    current = input_image
    for i, name in enumerate(layers):
        kind = name[:4]
        if kind == 'conv':
            kernels, bias = weight[i][0][0][0][0]
            # matconvnet: weights are [width, height, in_channels, out_channels]
            # tensorflow: weights are [height, width, in_channels, out_channels]
            kernels = np.transpose(kernels, (1, 0, 2, 3))
            bias = bias.reshape(-1)
            current = _conv_layer(current, kernels, bias)
        elif kind == 'relu':
            current = tf.nn.relu(current)
        elif kind == 'pool':
            current = _pool_layer(current)
        net[name] = current

    assert len(net) == len(layers)
    return net#, mean_pixel
```


```python
mean = data['normalization'][0][0][0]
mean_pixel = np.mean(mean, axis=(0, 1))
```


```python
# CONTENT_LAYER = 'relu4_2'
# content_features = {}

# with tf.Session() as sess:
#     content_pre = preprocess(image_content, mean_pixel)
#     content_net = net(np.squeeze(data['layers']), content_pre)
#     content_features[CONTENT_LAYER] = content_net[CONTENT_LAYER].eval()

CONTENT_LAYERS = ('conv1_1', 'conv2_1', 'conv4_1', 'conv4_2')
content_features = {}

with tf.Session() as sess:
    content_pre = preprocess(image_content, mean_pixel)
    content_net = net(content_pre)
    for layer in CONTENT_LAYERS:
        content_features[layer] = content_net[layer].eval()
```


```python
STYLE_LAYERS = ('conv3_1','conv5_1')
style_features = {}

with tf.Session() as sess:
    style_pre = preprocess(image_style, mean_pixel)
    style_net = net(style_pre)
    for layer in STYLE_LAYERS:
        features = style_net[layer].eval()
        features = np.reshape(features, (-1, features.shape[3]))
        gram = np.matmul(features.T, features) / features.size
        style_features[layer] = gram
```


```python
# make stylized image using backpropogation
initial = None
#initial = scipy.misc.imread('./images/cat.jpg')
if initial is None:
    noise = np.random.normal(size=image_content.shape, scale=np.std(image_content) * 0.1)
    initial = tf.random_normal(image_content.shape) * 0.256
else:
    initial = np.array([preprocess(initial, mean_pixel)])
    initial = initial.astype('float32')
```


```python
image = tf.Variable(initial)
image_net = net(image)
```


```python
content_weight = 5e0
style_weight = 1e4
tv_weight = 1e3
learning_rate = 1e0
iterations =  10000
checkpoint_iterations = 1000
print_iterations = 500
```


```python
# content loss
# content_loss = content_weight * (2 * tf.nn.l2_loss(
#         image_net[CONTENT_LAYER] - content_features[CONTENT_LAYER]) / 
#         content_features[CONTENT_LAYER].size)
content_loss = 0
content_losses = []
for content_layer in CONTENT_LAYERS:
    content_losses.append(2 * tf.nn.l2_loss(
                          image_net[content_layer] - content_features[content_layer]) / 
                          content_features[content_layer].size)
content_loss += content_weight * reduce(tf.add, content_losses)
```


```python
# style loss
style_loss = 0
style_losses = []
for style_layer in STYLE_LAYERS:
    layer = image_net[style_layer]
    _, height, width, number = map(lambda i: i.value, layer.get_shape())
    size = height * width * number
    feats = tf.reshape(layer, (-1, number))
    gram = tf.matmul(tf.transpose(feats), feats) / size
    style_gram = style_features[style_layer]
    style_losses.append(2 * tf.nn.l2_loss(gram - style_gram) / style_gram.size)
style_loss += style_weight * reduce(tf.add, style_losses)
```


```python
def _tensor_size(tensor):
    from operator import mul
    return reduce(mul, (d.value for d in tensor.get_shape()), 1)
```


```python
# total variation denoising
tv_y_size = _tensor_size(image[:,1:,:,:])
tv_x_size = _tensor_size(image[:,:,1:,:])
tv_loss = tv_weight * 2 * (
        (tf.nn.l2_loss(image[:,1:,:,:] - image[:,:image_content.shape[1]-1,:,:]) /
            tv_y_size) +
        (tf.nn.l2_loss(image[:,:,1:,:] - image[:,:,:image_content.shape[2]-1,:]) /
            tv_x_size))
```


```python
# overall loss
loss = content_loss + style_loss + tv_loss
```


```python
# optimizer setup
train_step = tf.train.AdamOptimizer(learning_rate).minimize(loss)
```


```python
def imsave(path, img):
    img = np.clip(img, 0, 255).astype(np.uint8)
    scipy.misc.imsave(path, img)
```


```python
# optimization
best_loss = float('inf')
best = None

with tf.Session() as sess:
    sess.run(tf.initialize_all_variables())
    for i in range(iterations):
        train_step.run()
        
        if i % checkpoint_iterations == 0 or i == iterations - 1:
            this_loss = loss.eval()
            if this_loss < best_loss:
                best_loss = this_loss
                best = image.eval()
            # save a check point
            import os
            try:
                os.makedirs('./checks/'+str.split(content_file_name,'.')[0])
            except OSError:
                pass
            timestr = time.strftime("%Y%m%d_%H%M%S")
            filename_cp = './checks/'+str.split(content_file_name,'.')[0]+'/'+timestr+'.jpg'
            cp = unprocess(best.reshape(image_content.shape[1:]), mean_pixel)
            imsave(filename_cp, cp)
        
        if i % print_iterations == 0 or i == iterations - 1:
            print('Iteration %d/%d' % (i + 1, iterations))
            print('  content loss: %g' % content_loss.eval())
            print('    style loss: %g' % style_loss.eval())
            print('       tv loss: %g' % tv_loss.eval())
            print('    total loss: %g' % loss.eval())

    output = unprocess(best.reshape(image_content.shape[1:]), mean_pixel)
```

    Iteration 1/10000
      content loss: 1.66586e+07
        style loss: 3.20725e+09
           tv loss: 2616.06
        total loss: 3.22391e+09
    Iteration 501/10000
      content loss: 2.66645e+07
        style loss: 1.27424e+07
           tv loss: 1.49095e+06
        total loss: 4.08979e+07
    Iteration 1001/10000
      content loss: 2.08549e+07
        style loss: 5.76224e+06
           tv loss: 1.3835e+06
        total loss: 2.80006e+07
    Iteration 1501/10000
      content loss: 1.80303e+07
        style loss: 4.06823e+06
           tv loss: 1.26077e+06
        total loss: 2.33593e+07
    Iteration 2001/10000
      content loss: 1.62877e+07
        style loss: 3.32573e+06
           tv loss: 1.16051e+06
        total loss: 2.07739e+07
    Iteration 2501/10000
      content loss: 1.50814e+07
        style loss: 2.893e+06
           tv loss: 1.08805e+06
        total loss: 1.90624e+07
    Iteration 3001/10000
      content loss: 1.42127e+07
        style loss: 2.63487e+06
           tv loss: 1.03354e+06
        total loss: 1.78812e+07
    Iteration 3501/10000
      content loss: 1.35826e+07
        style loss: 2.46563e+06
           tv loss: 994200
        total loss: 1.70425e+07
    Iteration 4001/10000
      content loss: 1.30854e+07
        style loss: 2.35163e+06
           tv loss: 968024
        total loss: 1.6405e+07
    Iteration 4501/10000
      content loss: 1.27158e+07
        style loss: 2.30957e+06
           tv loss: 950897
        total loss: 1.59763e+07
    Iteration 5001/10000
      content loss: 1.23816e+07
        style loss: 2.23516e+06
           tv loss: 938277
        total loss: 1.5555e+07
    Iteration 5501/10000
      content loss: 1.21122e+07
        style loss: 2.18655e+06
           tv loss: 928268
        total loss: 1.5227e+07
    Iteration 6001/10000
      content loss: 1.18902e+07
        style loss: 2.24536e+06
           tv loss: 920364
        total loss: 1.50559e+07
    Iteration 6501/10000
      content loss: 1.17574e+07
        style loss: 2.12474e+06
           tv loss: 914559
        total loss: 1.47967e+07
    Iteration 7001/10000
      content loss: 1.16008e+07
        style loss: 2.17217e+06
           tv loss: 908664
        total loss: 1.46817e+07
    Iteration 7501/10000
      content loss: 1.15296e+07
        style loss: 2.10719e+06
           tv loss: 905120
        total loss: 1.45419e+07
    Iteration 8001/10000
      content loss: 1.14505e+07
        style loss: 2.09468e+06
           tv loss: 901509
        total loss: 1.44467e+07
    Iteration 8501/10000
      content loss: 1.13611e+07
        style loss: 2.07426e+06
           tv loss: 898829
        total loss: 1.43342e+07
    Iteration 9001/10000
      content loss: 1.12966e+07
        style loss: 2.06561e+06
           tv loss: 895955
        total loss: 1.42582e+07
    Iteration 9501/10000
      content loss: 1.12327e+07
        style loss: 2.10122e+06
           tv loss: 894315
        total loss: 1.42282e+07
    Iteration 10000/10000
      content loss: 1.12485e+07
        style loss: 2.09316e+06
           tv loss: 891898
        total loss: 1.42335e+07



```python
imsave('./images/output_'+content_file_name, output)
```


```python
Image(filename = './images/output_'+content_file_name)
```




![jpeg](neural_style_files/neural_style_22_0.jpeg)


