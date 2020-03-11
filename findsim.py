#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 22:49:48 2019

@author: kevin
"""
import pandas as pd
import numpy as np

from scipy.stats import pearsonr  

sig = pd.read_csv("./sig/sigev.csv",low_memory=False)
sig2= np.loadtxt("./sig/sigev.csv")
data = np.genfromtxt("./sig/sig.csv", delimiter=',')
data[0]=np.asarray(data[0])
data[1]=np.asarray(data[1])
np.corrcoef(data[10],data[1])
pearsonr((1.290378, -2.522433, 1.353242), (0.850382, -1.779442, -0.50165))
type(sig.iloc[2,3:])
type(data[0])
data[0].shape
ss=[[12,22],[22,34]]
arr2=np.array(data)
arr2.shape
data[0]*data[1]

for x in range(0,100):

    corr= [0]*4646
    for i in range(4646):
        corr[i]=data[x]*data[i]


sig.fillna(0, inplace=True)

sim=pd.DataFrame()


for x in range(3501,4646):

    corr= [0]*4646
    for i in range(4646):
        corr[i]=pearsonr(sig.iloc[x,3:], sig.iloc[i,3:])[0]
    
    corr2=corr.copy()
    
    top=[0]*11
    for i in range(11):
        top[i]=max(corr2, key=abs)
        corr2.remove(top[i])   
    

    top=top[1:11]
    
    top_index=[0]*10
    top_index=[corr.index(top[i]) for i in range(10)]
    top_name=sig.iloc[top_index,1].tolist()

    top_name=[sig.iloc[x,1]]+(top_name)+top
    
    sim=sim.append(pd.Series(top_name),ignore_index=True)



sim.to_csv("output.csv", index=False, header=False)
sim
