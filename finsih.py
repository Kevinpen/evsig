#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 22:49:48 2019

@author: kevin
"""
import pandas as pd


from scipy.stats import pearsonr  

sig = pd.read_csv("./sig/humanZscore.csv",low_memory=False)


sig.fillna(0, inplace=True)

sim=pd.DataFrame()


for x in range(300,500):

    corr= [0]*15272
    for i in range(15272):
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

