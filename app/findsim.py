
import pandas as pd
import numpy as np
#from numpy import *
from scipy.stats import pearsonr  

data = np.genfromtxt("./templates/sig_human_new.csv", delimiter='\t',skip_header=1)
sig = pd.read_csv("./templates/sig_human_new.csv",delimiter='\t',low_memory=False)

data[np.isnan(data)] = 0
sim=pd.DataFrame()


for x in range(10000, np.size(data,0)):
    corr= [0]*np.size(data,0)
    for i in range(np.size(data,0)):
        corr[i]=pearsonr(data[x,3:],data[i,3:])[0]

    corr2=corr.copy()
    top=[0]*11
    for i in range(11):
        top[i]=max(corr2, key=abs)
        corr2.remove(top[i])   
    top=top[1:11]
    
    top_index=[0]*10
    top_index=[corr.index(top[i]) for i in range(10)]
    top_name=sig.iloc[top_index,0].tolist() 
    top_name=[sig.iloc[x,0]]+(top_name)+top    
    sim=sim.append(pd.Series(top_name),ignore_index=True)

sim.to_csv("output.csv", index=False, header=False)




