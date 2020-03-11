#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 17:07:07 2020

@author: kevin
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sigh = pd.read_csv("./sig/humanZscore.csv", low_memory=False)
simih = pd.read_csv("./sig/simh.csv", header=None)

mean_charge=list(range(3,6))
mean_aa=list(range(6,14))
mean_motif=list(range(14,59))
mean_repeats=list(range(59,75))
mean_phasesep=list(range(75,77))
mean_physchem=list(range(77,86))
var_charge=list(range(86,88))
var_aa=list(range(88,96))
var_motif=list(range(96,141))
var_physchem=list(range(141,149))


def sighpro(IDR):
	values2 = sigh.iloc[IDR,3:]
	plt.stem(values2, markerfmt=' ',use_line_collection=True)
	plt.grid(axis="y")
	figpro=plt.gcf()
	figpro.set_size_inches(4, 2.5)
	figpro.savefig('./static/image/sighpro'+str(IDR)+'.png', dpi=100)
	plt.clf()
    

def sighviz(IDR, Format="bar", Group=1):    
    i=IDR
    maa = sorted(pd.Series.tolist(sigh.iloc[i,mean_aa]), key =abs, reverse=True)[0:8]
    mch = sorted(pd.Series.tolist(sigh.iloc[i,mean_charge]), key = abs, reverse=True)[0:3]
    mmo = sorted(pd.Series.tolist(sigh.iloc[i,mean_motif]), key = abs, reverse=True)[0:10]
    mph = sorted(pd.Series.tolist(sigh.iloc[i,mean_physchem]), key=abs, reverse=True)[0:9]
    mrc = sorted(pd.Series.tolist(sigh.iloc[i,mean_repeats]), key=abs, reverse=True)[0:10]
    mps = sorted(pd.Series.tolist(sigh.iloc[i,mean_phasesep]), key=abs, reverse=True)[0:2]
    
    maa_abs = sorted(pd.Series.tolist(abs(sigh.iloc[i,mean_aa])), reverse=True)
    mch_abs = sorted(pd.Series.tolist(abs(sigh.iloc[i,mean_charge])), reverse=True)
    mmo_abs = sorted(pd.Series.tolist(abs(sigh.iloc[i,mean_motif])), reverse=True)
    mph_abs = sorted(pd.Series.tolist(abs(sigh.iloc[i,mean_physchem])),  reverse=True)
    mrc_abs = sorted(pd.Series.tolist(abs(sigh.iloc[i,mean_repeats])), reverse=True)
    mps_abs = sorted(pd.Series.tolist(abs(sigh.iloc[i,mean_phasesep])), reverse=True)
    
    vaa = sorted(pd.Series.tolist(sigh.iloc[i,var_aa]), key =abs, reverse=True)[0:8]
    vch = sorted(pd.Series.tolist(sigh.iloc[i,var_charge]), key = abs, reverse=True)[0:2]
    vmo = sorted(pd.Series.tolist(sigh.iloc[i,var_motif]), key = abs, reverse=True)[0:10]
    vph = sorted(pd.Series.tolist(sigh.iloc[i,var_physchem]), key=abs, reverse=True)[0:8]

    vaa_abs = sorted(pd.Series.tolist(abs(sigh.iloc[i,var_aa])), reverse=True)
    vch_abs = sorted(pd.Series.tolist(abs(sigh.iloc[i,var_charge])),  reverse=True)
    vmo_abs = sorted(pd.Series.tolist(abs(sigh.iloc[i,var_motif])), reverse=True)
    vph_abs = sorted(pd.Series.tolist(abs(sigh.iloc[i,var_physchem])),  reverse=True)

    
    if Format=="bar":
        barWidth = 1
         
        # set height of bar
        bars1 = mch_abs[0:3]
        bars2 = maa_abs[0:5]
        bars3 = mmo_abs[0:5]
        bars4 = mrc_abs[0:5]
        bars5 = mps_abs[0:2]
        bars6 = mph_abs[0:5]
        bars7 = vch_abs[0:2]
        bars8 = vaa_abs[0:5]
        bars9 = vmo_abs[0:5]
        bars10 = vph_abs[0:5]

        # Set position of bar on X axis
        r1 = np.arange(len(bars1))
        r2 = len(bars1)+np.arange(len(bars2))
        r3 = len(bars1)+len(bars2)+np.arange(len(bars3))
        r4 = len(bars1)+len(bars2)+len(bars3)+np.arange(len(bars4))
        r5 = len(bars1)+len(bars2)+len(bars3)+len(bars4)+np.arange(len(bars5))
        r6 = len(bars1)+len(bars2)+len(bars3)+len(bars4)+len(bars5)+np.arange(len(bars6))
        r7 = len(bars1)+len(bars2)+len(bars3)+len(bars4)+len(bars5)+len(bars6)+np.arange(len(bars7))
        r8 = len(bars1)+len(bars2)+len(bars3)+len(bars4)+len(bars5)+len(bars6)+len(bars7)+np.arange(len(bars8))
        r9 = len(bars1)+len(bars2)+len(bars3)+len(bars4)+len(bars5)+len(bars6)+len(bars7)+len(bars8)+np.arange(len(bars9))
        r10 =len(bars1)+len(bars2)+len(bars3)+len(bars4)+len(bars5)+len(bars6)+len(bars7)+len(bars8)+len(bars9)+np.arange(len(bars10))

        
        # Make the plot
        plt.bar(r1, bars1, color='#36072d', width=barWidth, edgecolor='white')
        plt.bar(r2, bars2, color='#910f3f', width=barWidth, edgecolor='white')
        plt.bar(r3, bars3, color='#9c0615', width=barWidth, edgecolor='white')
        plt.bar(r4, bars4, color='#d45a26', width=barWidth, edgecolor='white')
        plt.bar(r5, bars5, color='#edc92b', width=barWidth, edgecolor='white') 
        plt.bar(r6, bars6, color='#f7f294', width=barWidth, edgecolor='white')        
        plt.bar(r7, bars7, color='#36072d', width=barWidth, edgecolor='white')          
        plt.bar(r8, bars8, color='#910f3f', width=barWidth, edgecolor='white')     
        plt.bar(r9, bars9, color='#9c0615', width=barWidth, edgecolor='white')  
        plt.bar(r10, bars10, color='#f7f294', width=barWidth, edgecolor='white')  

        # Add xticks on the middle of the group bars
        plt.xlabel('group', fontweight='bold')
        plt.ylabel('z-score', fontweight='bold')
        plt.xticks(2+np.arange(50,step=5), ['mean_charge','mean_aa', 'mean_motif', 'mean_repeats','mean_phasesep',
                   'mean_physichem', 'var_charge','var_aa' ,'var_motif' , 'var_physichem']
        ,fontsize=6)    
        
        figbar=plt.gcf()
        figbar.set_size_inches(6.5, 3)
        figbar.savefig('./static/image/sighbar'+str(i)+'.png', dpi=100)
 
        return()
        
    
    if Format == "div":
        if Group < 7 :
            mean_or_variance="Mean"
        else:
            mean_or_variance="Log Variance"
        group_name={2:"Amino Acid Fraction", 1: "Charge properties",3:"Motifs",
                    6:"Physicochemical properties", 4:"Repeats",5:"Phase Separation",0:"Physicochemical properties"}[(Group) % 6]
        feature={2:mean_aa, 1:mean_charge,3:mean_motif,6:mean_physchem,5:mean_repeats,4:mean_phasesep,
                 8:var_aa,7:var_charge,9:var_motif,12:var_physchem}[Group]
        score_list={2:maa,1:mch,3:mmo,6:mph,4:mrc,5:mps,7:vch,8:vaa,9:vmo,12:vph}[Group]
        score_list=[x for x in reversed(score_list) if ~np.isnan(x)]

        
        fig, yx = plt.subplots(constrained_layout=True)
        plt.title('Top {0} Z-scores in \n {1} Group '.format(mean_or_variance, group_name), 
                  fontdict={'size':10})
        plt.hlines(np.arange(len(score_list)), xmin=0, xmax=score_list)
        for x, y, tex in zip(score_list, np.arange(len(score_list)), score_list):
            plt.text(x, y, round(tex, 2), horizontalalignment='right' if x < 0 else 'left', 
                         verticalalignment='center', fontdict={'color':'red' if x < 0 else 'green', 'size':6})
        plt.yticks(np.arange(len(score_list)), feature, fontsize=6)
        plt.grid(linestyle='--', alpha=0.35)
        
        plt.xlim(min(score_list)-1.5, max(score_list)+1.5)
        plt.gca().set(ylabel='$Molecular-features$', xlabel='$Z-scores$')
        
        figdiv = plt.gcf()
        figdiv.set_size_inches(4, 3)
        figdiv.savefig('./static/image/sighdiv'+str(i)+'g'+str(Group)+'.png', dpi=100)
        plt.clf()
        
        return()   
    
# Find the list of similar IDRs
#def simi(IDR):
#    return simidf.iloc[IDR,:].tolist()

def getname(index):
    return sigh.iloc[index,2].split("_")[2].strip()


def getindex_idr(name):
    test = sigh['MFA']==name
    if test.any()  == False:
        return -1
    else:
        return sigh.index.values[sigh['MFA']==name][0]  

# Find by protein common name
def getindex_cid(name):
    index = []
    for i in range(len(sigh)):
        cid =  sigh.iloc[i,2].split("_")[2].strip()  # in this table, third column is common name separated by "_"
        if cid == name:
            index.append(sigh.iloc[i,1])
    return index

def getindex_sid(name):
    index = []
    for i in range(len(sigh)):
        sid =  sigh.iloc[i,2].split("_")[1].strip()
        if sid == name:
            index.append(sigh.iloc[i,1])
    return index
    
# Find the list of similar IDRs, the first item is the orginal IDR
def simi(IDR):
    return simih.iloc[IDR,:].tolist()
# Find common name from index





