from tensorflow.keras.layers import Conv2D, Input, Conv2DTranspose,Activation, BatchNormalization, ReLU, Concatenate, UpSampling2D
from tensorflow.keras.models import Model, load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from skimage.color import rgb2lab, lab2rgb, rgb2gray, gray2rgb
from skimage.transform import resize
import cv2
from skimage.io import imsave
import numpy as np

def conv_block(x, filters, kernel_size, strides=2):
   x = Conv2D(filters=filters,
              kernel_size=kernel_size,
              strides=strides,
              padding='same')(x)
   x = BatchNormalization()(x)
   x = ReLU()(x)
   return x

def deconv_block(x, filters, kernel_size):
   x = Conv2DTranspose(filters=filters,
                       kernel_size=kernel_size,
                       strides=2,
                       padding='same')(x)
   x = BatchNormalization()(x)
   x = ReLU()(x)
   return x

def denoising_autoencoder():
   dae_inputs = Input(shape=(32, 32, 3), name='dae_input')
   conv_block1 = conv_block(dae_inputs, 32, 3)
   conv_block2 = conv_block(conv_block1, 64, 3)
   conv_block3 = conv_block(conv_block2, 128, 3)
   conv_block4 = conv_block(conv_block3, 256, 3)
   conv_block5 = conv_block(conv_block4, 256, 3, 1)

   deconv_block1 = deconv_block(conv_block5, 256, 3)
   merge1 = Concatenate()([deconv_block1, conv_block3])
   deconv_block2 = deconv_block(merge1, 128, 3)
   merge2 = Concatenate()([deconv_block2, conv_block2])
   deconv_block3 = deconv_block(merge2, 64, 3)
   merge3 = Concatenate()([deconv_block3, conv_block1])
   deconv_block4 = deconv_block(merge3, 32, 3)

   final_deconv = Conv2DTranspose(filters=3,
                       kernel_size=3,
                       padding='same')(deconv_block4)

   dae_outputs = Activation('sigmoid', name='dae_output')(final_deconv)
  
   return Model(dae_inputs, dae_outputs, name='dae')
def vgg():
   encoder_input = Input(shape=(7, 7, 512,))
   #Decoder
   decoder_output = Conv2D(256, (3,3), activation='relu', padding='same')(encoder_input)
   decoder_output = Conv2D(128, (3,3), activation='relu', padding='same')(decoder_output)
   decoder_output = UpSampling2D((2, 2))(decoder_output)
   decoder_output = Conv2D(64, (3,3), activation='relu', padding='same')(decoder_output)
   decoder_output = UpSampling2D((2, 2))(decoder_output)
   decoder_output = Conv2D(32, (3,3), activation='relu', padding='same')(decoder_output)
   decoder_output = UpSampling2D((2, 2))(decoder_output)
   decoder_output = Conv2D(16, (3,3), activation='relu', padding='same')(decoder_output)
   decoder_output = UpSampling2D((2, 2))(decoder_output)
   decoder_output = Conv2D(2, (3, 3), activation='tanh', padding='same')(decoder_output)
   decoder_output = UpSampling2D((2, 2))(decoder_output)
   model = Model(inputs=encoder_input, outputs=decoder_output)
   model.save()
   return model

class Denoise:
   def __init__(self):
      self.dae = denoising_autoencoder()
      self.dae.load_weights('denoise.h5')

   def deNoise(self, file):
      test_data_noisy = file
      test_data_noisy = test_data_noisy.reshape((1,*test_data_noisy.shape))/255
      img=self.dae.predict(test_data_noisy)
      cv2.imwrite("restored.jpg",img[0]*255)

class Colorize:
   def __init__(self):
      self.vgg = load_model("vgg.h5")
      self.model = load_model("colorize.h5")
   
   def colorize(self,file):
      test = img_to_array(load_img(file))
      test = resize(test, (224,224), anti_aliasing=True)
      test*= 1.0/255
      lab = rgb2lab(test)
      l = lab[:,:,0]
      L = gray2rgb(l)
      L = L.reshape((1,224,224,3))
      #print(L.shape)
      vggpred = self.vgg.predict(L)
      ab = self.model.predict(vggpred)
      #print(ab.shape)
      ab = ab*128
      cur = np.zeros((224, 224, 3))
      cur[:,:,0] = l
      cur[:,:,1:] = ab
      imsave("restored.jpg",lab2rgb(cur))

