# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 19:38:27 2017

@author: Tanilas
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 16:11:53 2017

@author: Tanilas
"""

import PIL
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

plt.close('all')
samp_jpg = "clef2.jpg" # Set the filename of the image
#samp_jpg = "probo.jpg" # Set the filename of the image
samp_img = Image.open(samp_jpg) # Load the image as an image object

I = np.asarray(samp_img)/255.0 # convert the image into numpy 3-D matrix. Divide by 255 to limit values from 0 to 1


hthr=0.70; lthr=0.0 # These are the uuper and lower threshold for the image, all the rest intensities are taken into account. Set them to 1 and 0 respectively to include all pixels (This is computationally heavy)
factor=3; minsi=3; # These are: the multiplier of the intensity for the size of the circle and the minimum size of the circle respectively
gap=5 # Taking every pixel takes a lot of time (depending on the size of the image), so take every gap-th pixel instead
I=I[::gap,::gap,:];
mI=np.mean(I,2);

inds=np.asmatrix(np.where( (np.logical_and(mI>lthr,mI<hthr)==1)))
sinds=inds.shape;
perminds=np.random.permutation(sinds[1])
inds=inds[:,perminds] #If you want the indices to be randomly chosen uncomment this. (This does not lead to images that appear like "flowing from upper left corner to bottom right")
for i in range(0,inds[0,:].size):
        print(i)
        xi=inds[0,i]
        yi=inds[1,i]
        col=np.squeeze(I[xi,yi,:])
        
        # As intensity we just take the mean of the color vector
        intensity=np.mean(col);
    
        # Make a circle in the location of the pixel, with color same as the pixel, and size proportional to the intensity of the pixel
        plt.plot(yi,-xi,'o',color=col, ms=(minsi+(1-intensity)*factor), mec="none") #
                
## Show and save the image (with bad resolution of 300 dpi)
plt.axis('off')
plt.axis('image')
plt.savefig(samp_jpg[0:(len(samp_jpg)-4)]+'_dotted.png',dpi=300, bbox_inches='tight',pad_inches = 0)