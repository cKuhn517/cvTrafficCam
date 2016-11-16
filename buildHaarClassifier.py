######################################################

##  buildHaarClassifier.py

##  Provides code and outlines manual steps required
##  for obtaining training material and training a
##  Haar classifier with OpenCV for python.

__version__   = "0.1"
__status__    = "Development"

######################################################

import urllib
import cv2
import numpy as np
import os

# Get positive and negative examples of the thing we want to identify
def store_raw_images(images_link, folder):
    # open the url from image-net.org with the list of image urls
    image_urls = urllib.urlopen(images_link).read().decode()

    # get the current image number in the directory
    pic_num = len(os.listdir(folder+'/')) + 1

    for i in image_urls.split('\n'):
        try:
            # For each image save it as gray scale and 100x100
            print(i)
            urllib.urlretrieve(i,folder+"/"+str(pic_num)+'.jpg')
            img = cv2.imread(folder+"/"+str(pic_num)+'.jpg', cv2.IMREAD_GRAYSCALE)
            resized_image = cv2.resize(img, (100,100))
            cv2.imwrite(folder+"/"+str(pic_num)+'.jpg', resized_image)
            pic_num += 1

        except Exception as e:
            print(str(e))

# The URLs can be obtained by searching for a desired item to train for at
# image-net.org and something else to use as negative examples.  Here I am
# training for cars with people as the negative examples.

#store_raw_images('http://image-net.org/api/text/imagenet.synset.geturls?wnid=n07942152',
#                 'neg')

#store_raw_images('http://image-net.org/api/text/imagenet.synset.geturls?wnid=n02958343',
#                 'pos')

# Get rid of flicker files that are the missing file image.
# Need to copy a sample into the uglies folder before running
def find_uglies():
    # Check bot neg and pos folders
    for file_type in ['neg', 'pos']:
        for img in os.listdir(file_type):
            for ugly in os.listdir('uglies'):
                try:
                    current_image_path = str(file_type)+'/'+str(img)
                    ugly = cv2.imread('uglies/'+str(ugly))
                    question = cv2.imread(current_image_path)

                    # not xor bitwise will be true if images are exactly the same, then delete
                    if not(np.bitwise_xor(ugly,question).any()):
                        print('Ugly found')
                        print(current_image_path)
                        os.remove(current_image_path)

                except Exception as e:
                    print(str(e))

#find_uglies()


def create_pos_n_neg():
    for file_type in ['neg', 'pos']:
        for img in os.listdir(file_type):
            
            if file_type == 'neg':
                # For each neg ex write a line with the filename
                line = file_type+'/'+img+'\n'
                with open('bg.txt','a') as f:
                    f.write(line)
                    
            elif file_type == 'pos':
                # For each pos ex write a line with filename, num obj,
                # x/y location of obj, and width/heigh of obj.
                # For simplicity I left it as 1 for all images and deleted
                # the ones that were too close/too far/had multiple cars
                line = file_type+'/'+img+' 1 15 15 70 70\n'
                with open('info.lst','a') as f:
                    f.write(line)

#create_pos_n_neg()

# In command line create vector file of positive samples with:
# opencv_createsamples -info info.lst -num 869 -w 20 -h 20 -vec positives.vec

# This takes the list of examples, count of them, width and height of samples, and the output name

# Now train the cascade with our samples and the vector file in the command line with:
# NOTE: This takes a long time on a pi.  I recommend something more powerful, then
#       you can increase the size used (the -w and -h) and get better results.

# opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 800 -numNeg 900 -numStages 10 -w 20 -h 20

# Insufficient memory on Pi, used the following to create a larger swap file:
# sudo dd if=/dev/zero of=/var/swap2 bs=1024 count=1572864
# sudo mkswap /var/swap2
# sudo swapon /var/swap2
