#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 10:15:30 2019

@author: lokeshmishra
"""
# The aim of this program is to generate data for a ML/DL network to be trained upon.
# This program reads the images which have been sorted according to their terrain. 
# An image is generated by sewing together peices of different labelled imaged. The system will remember the labels as well. These will lated be used to test the accuracy of the prediction as well as the performance.
# Unused code always at the end.
# We will work with PILLOW for now and leave OpenCV for later.
# =============================================================================
# Standard imports
# =============================================================================
import os
import numpy as np
import pandas as pd
from PIL import Image
import glob
import fnmatch
#import cv2
# =============================================================================
# Reading the 'tiles' folder and creating a dictionary for labels
# =============================================================================
# Store project path
#Look at all possible terrains and make a list
#Store the above data for labelling purposes in a dictionary
projectpath = "/home/lokeshmishra/PaleBlueDot/BernPhD/Projects/Terrain_Classifier/terrain_classifier"
terrains = os.listdir(projectpath + "/tiles")
foldnames = os.listdir(projectpath + "/tiles/" + terrains[0])


dict_terrains={}
filepath = []

i = 0
while i < len(terrains) :
    dict_terrains[i] = str(terrains[i])
    i += 1
print('I am at the start.')



#filepath
i = j = 0
print('I am at the start.')
for i in dict_terrains :
    print('I am here i = ' + str(i) )
    for j in range(len(foldnames)) :
        print('I am in i = ' + str(i) + ' j = ' + str(j) +'.' )
        a = glob.glob(projectpath + '/tiles/' + dict_terrains[0] + '/' + foldnames[j] + '/*.jpg')

    
print('I am at the end.')


# =============================================================================
# Create a table (pandas dataframe) to store interesting information.
# =============================================================================
count = pd.DataFrame(np.random.randn(5,3), index=terrains, columns = foldnames)
print(count)


#img = cv2.imread(projectpath+"/tiles/water/test/0_0_8.jpg",1)
#img = Image.open(projectpath + "/tiles/water/test/0_0_8.jpg")

#directories = ['desert','water','polar_caps','mountains','forrest']
#directories_train = [ 'tiles/' + directories[i] + '/train/' for i in range(5)]
#directories_test = [ 'tiles/' + directories[i] + '/test/' for i in range(5)]
#directories_val = [ 'tiles/' + directories[i] + '/validation/' for i in range(5)]
#list_images_train = [fnmatch.filter(os.listdir(directories_train[i]), '*.jpg') for i in [0,1,2,3,4]]
#list_images_test = [fnmatch.filter(os.listdir(directories_test[i]), '*.jpg') for i in [0,1,2,3,4]]
#list_images_val = [fnmatch.filter(os.listdir(directories_val[i]), '*.jpg') for i in [0,1,2,3,4]]
#a = glob.glob(projectpath + '/tiles/' + dict_terrains[i] + '/' + foldnames[j] + '/*.jpg')
#print(len(a))