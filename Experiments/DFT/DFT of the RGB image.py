import numpy as np
import skimage.data as data
import skimage.io as io
import skimage.exposure as ex
import matplotlib.pyplot as plt

c = io.imread('U:\\4-1\\Digital Image Processing LAB\\Lab_Report_4_5_6_7_8\\Dataset\\misc\\4.2.07.tiff')


cf = np.fft.fft2(c)
cfs = np.fft.fftshift(cf)
cfsl = np.log(1+np.abs(cfs))

plt.subplot(1,2,1)
plt.axis('off')
plt.title('RGB image')
plt.imshow(c)

plt.subplot(1,2,2)
plt.axis('off')
plt.title('DFT of the RGB image')
plt.imshow(ex.rescale_intensity(cfsl,out_range=(0.0,1.0)))

plt.show()

