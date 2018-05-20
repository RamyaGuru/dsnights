#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 17 09:51:39 2018

@author: guru

Kmeans clustering on hate crime data from FiveThiryEight
"""
import numpy as np
from sklearn.cluster import KMeans
from sklearn import preprocessing as pp


# Read in data from csv file
datafile= "hate_crimes.csv"
#Get header
with open(datafile, 'r') as f:
    header = f.readline().split(",")
    ncols = len(header)

#Load data into an array
#CHANGE which features get used in the clustering algorithm by manipulating "features"
features = list(range(1,ncols))

#Features used in model
print('Features used in model:')
featnames = [header[f] for f in features]
print(featnames)

hc_all = np.genfromtxt(datafile, dtype='float', skip_header=1, usecols=features, filling_values = np.nan, delimiter = ",")
states = np.genfromtxt(datafile, dtype='str', skip_header=1, usecols=0, delimiter = ",")



#Fill in missing values with the column means
missing = np.isnan(hc_all)
colmeans = np.nanmean(hc_all, 0)
hc_full = np.where(missing, colmeans, hc_all)

#Preprocessing: Center (zero mean) and Scale (unit variance)
hc_scale = pp.scale(hc_full)

#KMeans clustering
K = 5; #CHANGE the number of clusters generated
kmeans = KMeans(n_clusters=K).fit(hc_full) #CHANGE to hc_scale to see what happens!
lbl = kmeans.labels_
centers = kmeans.cluster_centers_

for k in range(K): #For each generated cluster
    pos= [n for (n,m) in enumerate(lbl) if m==k] #Get the indices in the labels vector which point ot that cluster
    stateGrp = states[pos]
    print('Generated State Group #{}'.format(k+1))
    print(stateGrp)
    print('mean feature values of the group:')
    print(centers[k])
    print('\n')
    
   
    
    