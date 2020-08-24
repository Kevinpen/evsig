# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 10:08:31 2020

@author: pengg
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

datasets2 = pd.read_csv("./data/dataset_config2.csv")

data = []
anns = []
tstats = []
for i in range(datasets2.shape[0]):
    data.append(pd.read_csv("./data/"+datasets2.iloc[i,1],low_memory=False,sep='\t'))
    anns.append(pd.read_csv("./data/"+datasets2.iloc[i,2]))
    tstats.append(pd.read_csv("./data/"+datasets2.iloc[i,3]))


#Find index by idr name
def getindex_idr(name,dataset=0):
    test = data[dataset].iloc[:,0]==name
    if test.any()  == False:
        return -1
    else:
        return data[dataset].index.values[data[dataset].iloc[:,0]==name][0]  

# Find idrname by protein common name
def getindex_cid(name, dataset=0):
    index = []
    for i in range(len(data[dataset])):
        cid =  data[dataset].iloc[i,2]  # in this table, third column is common name separated by ";"
        if  name.lower() == cid.lower():
            index.append(i)
    return index



#Find idrname by systematic name
def getindex_sid(name, dataset=0):
    index = []
    for i in range(len(data[dataset])):
        sid =  data[dataset].iloc[i,1]
        if sid.lower() == name.lower():
            index.append(i)
    return index

#Get Zscores of an IDR by list of molecular features
def get_zscore(IDR, flist, dataset=0):
    zscores=[]
    for feature in flist:
        zscores.append(data[dataset][feature][IDR]) 
    return zscores

# FInd GO terms annotated to this IDR
def get_ann(IDR, dataset=0):
    annotated = [i+2 for i, e in enumerate(anns[dataset].iloc[IDR,2:]) if e !=0]
    annotation = list(anns[dataset].columns.values[annotated])
    return annotation

# FInd GO terms not annotated to this IDR
def get_non_ann(IDR, dataset=0):
    annotated_id = [i for i, e in enumerate(anns[dataset].iloc[IDR,2:]) if e !=0]
    non_ann = np.delete(anns[dataset].columns.values[2:], annotated_id)
    return non_ann


def get_features(col, dataset=0):
    idx = tstats[dataset].iloc[:,col][tstats[dataset].iloc[:,col].notnull()].index
    features= tstats[dataset].iloc[idx,0]
    return features

def get_tstats(col,dataset=0):
    idx = tstats[dataset].iloc[:,col][tstats[dataset].iloc[:,col].notnull()].index
    tstats_values = tstats[dataset].iloc[idx,col]
    return tstats_values

def get_columnIndex(ann,dataset=0):
    return anns[dataset].columns.get_loc(ann)

def get_tstats_col(ann_col, dataset=0):
    ann = anns[dataset].columns.values[ann_col]
    return tstats[dataset].columns.get_loc(ann)


def plot_scatter(col, IDR, dataset=0):
    features = get_features(col, dataset)
    tstats_values = get_tstats(col, dataset)        
    zscores = get_zscore(IDR,features, dataset)
    plt.style.use('default')
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    plt.suptitle(f'ZFplot of {data[dataset].iloc[IDR,0]} for annotation: \n{tstats[dataset].columns[col]}',fontsize="medium")

    # Move left y-axis and bottim x-axis to centre, passing through (0,0)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    # Eliminate upper and right axes
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    # Show ticks in the left and lower axes only
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    
    ax.set_xlim(-max(abs(tstats_values))-1,max(abs(tstats_values))+1)
    ax.set_ylim(-max(abs(pd.Series(zscores)))-1,max(abs(pd.Series(zscores)))+1)
    
    for v in range(2, int(plt.ylim()[1])):
        ax.axhspan(v, v+2, color='PowderBlue', alpha=0.2)
    for v in range(int(plt.ylim()[0]),-2):
        ax.axhspan(v, v+2, color='PowderBlue', alpha=0.2)
    for h in range(2, int(plt.xlim()[1])):
        ax.axvspan(h, h+2, color='PowderBlue', alpha=0.2)
    for h in range(int(plt.xlim()[0]),-2):
        ax.axvspan(h, h+2, color='PowderBlue', alpha=0.2)
    
    
    ax.xaxis.set_label_coords(1.06, 0.49)
    ax.yaxis.set_label_coords(0.5, 1)
    ax.xaxis.label.set_color('orange')
    ax.yaxis.label.set_color('orange')
    y_label = ax.set_ylabel('Z-score')
    y_label.set_rotation(0)
    ax.set_xlabel('F-score')
    
    plt.scatter(tstats_values, zscores)
    for i, txt in enumerate(features):
        ax.annotate(txt, (tstats_values.iloc[i]+0.2, zscores[i]),fontsize=7)
    #plt.show()

    figzf = plt.gcf()
    figzf.set_size_inches(5, 5)
    figzf.savefig('./static/image/zf'+str(col)+'for'+str(IDR)+'.png', dpi=100)
    plt.clf()
    plt.style.use('default')


    
if __name__ == '__main__':
    print(getindex_idr('HUMAN12627_451to512'))
    idx1= getindex_cid('NDUS3')
    print(idx1)
    idx2=getindex_sid('O15399')
    print(idx2)
    print(get_zscore(0,['FCR','AA_P']))
 
    plot_scatter(5,idx1[0])
    







