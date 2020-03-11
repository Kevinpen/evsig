#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 17:13:47 2019

@author: kevin
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator)
import matplotlib.ticker as ticker
from mpl_toolkits.axes_grid.parasite_axes import SubplotHost

simidf = pd.read_csv("./sig/sim.csv", header=None)

  
sig = pd.read_csv("./sig/sigev.csv",low_memory=False)

        
mean_aa=["mean_calc_AA_A","mean_calc_AA_G","mean_calc_AA_H","mean_calc_AA_N",
              "mean_calc_AA_P","mean_calc_AA_Q","mean_calc_AA_S","mean_calc_AA_T"]
mean_charge=["mean_calc_kappa","mean_calc_omega","mean_calc_FCR","mean_calc_NCPR",
                      "mean_calc_net_charge","mean_calc_net_charge_P","mean_calc_SCD",
                      "mean_calc_RK_ratio", "mean_calc_ED_ratio"]
mean_motif=["mean_calc_TRG_NLS_MonoExtN_4", "mean_calc_LIG_PCNA_PIPBox_1",
                      "mean_calc_DOC_MAPK_HePTP_8","mean_calc_MOD_CDK_SPxK_1" ,
                      "mean_calc_DOC_PP1_RVXF_1", "mean_calc_DEG_APCC_TPR_1",
                      "mean_calc_DEG_APCC_KENBOX_2", "mean_calc_LIG_EH_1",
                      "mean_calc_DOC_PP2B_PxIxI_1", "mean_calc_LIG_CaM_IQ_9",
                      "mean_calc_TRG_ER_FFAT_1", "mean_calc_LIG_AP_GAE_1",
                      "mean_calc_LIG_SUMO_SIM_par_1", "mean_calc_LIG_LIR_Gen_1",
                      "mean_calc_LIG_GLEBS_BUB3_1",  "mean_calc_DOC_MAPK_gen_1",
                      "mean_calc_MOD_PRK1", "mean_calc_DOC_CKS1_1",
                      "mean_calc_TRG_MITOCHONDRIA",   "mean_calc_MOD_IPL1",
                      "mean_calc_DOC_MAPK_DCC_7",     "mean_calc_MOD_CKII",
                      "mean_calc_MOD_CDK_STP",        "mean_calc_MOD_MEC1",
                      "mean_calc_MOD_SUMO_for_1",     "mean_calc_MOD_ISOMERASE",
                      "mean_calc_LIG_APCC_Cbox_2",   "mean_calc_TRG_FG",
                      "mean_calc_MOD_LATS_1",         "mean_calc_TRG_ER_HDEL",
                      "mean_calc_DOC_PRO",           "mean_calc_TRG_Golgi_diPhe_1",
                      "mean_calc_MOD_PKA",           "mean_calc_INT_RGG",
                      "mean_calc_MOD_IME2",           "mean_calc_CLV_Separin_Fungi",
                      "mean_calc_LIG_eIF4E_1"]
mean_physic=["mean_calc_length", "mean_calc_aliphatic", "mean_calc_acidic",
                       "mean_calc_chain_expanding",  "mean_calc_aromatic",
                       "mean_calc_polar_fraction", "mean_calc_basic", "mean_calc_disorder_promoting",
                       "mean_calc_hydrophobicity", "mean_calc_Iso_point", "mean_calc_PPII_prop"]
mean_repeats=["mean_calc_REP_FG2", "mean_calc_REP_KAP2", "mean_calc_REP_PTS2",
                      "mean_calc_REP_QN2", "mean_calc_REP_RG2", "mean_calc_REP_SG2",
                      "mean_calc_REP_SR2", "mean_calc_REP_D2", "mean_calc_REP_E2",
                      "mean_calc_REP_G2", "mean_calc_REP_K2", "mean_calc_REP_N2",
                      "mean_calc_wf_complexity", "mean_calc_REP_P2", "mean_calc_REP_Q2",
                      "mean_calc_REP_R2", "mean_calc_REP_S2"]
    
log_var_aa=["log_var_calc_AA_A","log_var_calc_AA_G","log_var_calc_AA_H","log_var_calc_AA_N",
              "log_var_calc_AA_P","log_var_calc_AA_Q","log_var_calc_AA_S","log_var_calc_AA_T"]
log_var_charge=["log_var_calc_kappa","log_var_calc_omega","log_var_calc_FCR","log_var_calc_NCPR",
                      "log_var_calc_net_charge","log_var_calc_net_charge_P","log_var_calc_SCD",
                      "log_var_calc_RK_ratio", "log_var_calc_ED_ratio"]
log_var_motif=["log_var_calc_TRG_NLS_MonoExtN_4", "log_var_calc_LIG_PCNA_PIPBox_1",
                      "log_var_calc_DOC_MAPK_HePTP_8","log_var_calc_MOD_CDK_SPxK_1" ,
                      "log_var_calc_DOC_PP1_RVXF_1", "log_var_calc_DEG_APCC_TPR_1",
                      "log_var_calc_DEG_APCC_KENBOX_2", "log_var_calc_LIG_EH_1",
                      "log_var_calc_DOC_PP2B_PxIxI_1", "log_var_calc_LIG_CaM_IQ_9",
                      "log_var_calc_TRG_ER_FFAT_1", "log_var_calc_LIG_AP_GAE_1",
                      "log_var_calc_LIG_SUMO_SIM_par_1", "log_var_calc_LIG_LIR_Gen_1",
                      "log_var_calc_LIG_GLEBS_BUB3_1",  "log_var_calc_DOC_MAPK_gen_1",
                      "log_var_calc_MOD_PRK1", "log_var_calc_DOC_CKS1_1",
                      "log_var_calc_TRG_MITOCHONDRIA",   "log_var_calc_MOD_IPL1",
                      "log_var_calc_DOC_MAPK_DCC_7",     "log_var_calc_MOD_CKII",
                      "log_var_calc_MOD_CDK_STP",        "log_var_calc_MOD_MEC1",
                      "log_var_calc_MOD_SUMO_for_1",     "log_var_calc_MOD_ISOMERASE",
                      "log_var_calc_LIG_APCC_Cbox_2",   "log_var_calc_TRG_FG",
                      "log_var_calc_MOD_LATS_1",         "log_var_calc_TRG_ER_HDEL",
                      "log_var_calc_DOC_PRO",           "log_var_calc_TRG_Golgi_diPhe_1",
                      "log_var_calc_MOD_PKA",           "log_var_calc_INT_RGG",
                      "log_var_calc_MOD_IME2",           "log_var_calc_CLV_Separin_Fungi",
                      "log_var_calc_LIG_eIF4E_1"]
log_var_physic=["log_var_calc_length", "log_var_calc_aliphatic", "log_var_calc_acidic",
                       "log_var_calc_chain_expanding",  "log_var_calc_aromatic",
                       "log_var_calc_polar_fraction", "log_var_calc_basic", "log_var_calc_disorder_promoting",
                       "log_var_calc_hydrophobicity", "log_var_calc_Iso_point", "log_var_calc_PPII_prop"]
log_var_repeats=["log_var_calc_REP_FG2", "log_var_calc_REP_KAP2", "log_var_calc_REP_PTS2",
                      "log_var_calc_REP_QN2", "log_var_calc_REP_RG2", "log_var_calc_REP_SG2",
                      "log_var_calc_REP_SR2", "log_var_calc_REP_D2", "log_var_calc_REP_E2",
                      "log_var_calc_REP_G2", "log_var_calc_REP_K2", "log_var_calc_REP_N2",
                      "log_var_calc_wf_complexity", "log_var_calc_REP_P2", "log_var_calc_REP_Q2",
                      "log_var_calc_REP_R2", "log_var_calc_REP_S2"]


#Find index by idr name
def getindex_idr(name):
    test = sig['idr_name']==name
    if test.any()  == False:
        return -1
    else:
        return sig.index.values[sig['idr_name']==name][0]  

# Find index by protein common name
def getindex_cid(name):
    index = []
    for i in range(len(sig)):
        cid =  sig.iloc[i,2].split(";")[1].strip()  # in this table, third column is common name separated by ";"
        if cid == name:
            index.append(sig.iloc[i,1])
    return index

#Find index by systematic name
def getindex_sid(name):
    index = []
    for i in range(len(sig)):
        sid =  sig.iloc[i,2].split(";")[0].strip()
        if sid == name:
            index.append(sig.iloc[i,1])
    return index

def sigviz(IDR, Format="bar", Group=1):    
    i=IDR
    maa = sorted(pd.Series.tolist(sig[mean_aa].iloc[i]), key =abs, reverse=True)[0:8]
    maa_s=sig[mean_aa].iloc[i]
    maa_df=pd.DataFrame( {"name":list(maa_s.index.values),"value":maa_s.values})
    maa_name=maa_df['name'].iloc[abs(maa_df["value"]).argsort().tolist()]
    mch = sorted(pd.Series.tolist(sig[mean_charge].iloc[i]), key = abs, reverse=True)[0:9]
    mmo = sorted(pd.Series.tolist(sig[mean_motif].iloc[i]), key = abs, reverse=True)[0:10]
    mph = sorted(pd.Series.tolist(sig[mean_physic].iloc[i]), key=abs, reverse=True)[0:10]
    mrc = sorted(pd.Series.tolist(sig[mean_repeats].iloc[i]), key=abs, reverse=True)[0:10]
   
    maa_abs = sorted(pd.Series.tolist(abs(sig[mean_aa].iloc[i])), reverse=True)
    mch_abs = sorted(pd.Series.tolist(abs(sig[mean_charge].iloc[i])),  reverse=True)
    mmo_abs = sorted(pd.Series.tolist(abs(sig[mean_motif].iloc[i])), reverse=True)
    mph_abs = sorted(pd.Series.tolist(abs(sig[mean_physic].iloc[i])),  reverse=True)
    mrc_abs = sorted(pd.Series.tolist(abs(sig[mean_repeats].iloc[i])), reverse=True)
    
    vaa = sorted(pd.Series.tolist(sig[log_var_aa].iloc[i]), key =abs, reverse=True)[0:8]
    vch = sorted(pd.Series.tolist(sig[log_var_charge].iloc[i]), key = abs, reverse=True)[0:9]
    vmo = sorted(pd.Series.tolist(sig[log_var_motif].iloc[i]), key = abs, reverse=True)[0:10]
    vph = sorted(pd.Series.tolist(sig[log_var_physic].iloc[i]), key=abs, reverse=True)[0:10]
    vrc = sorted(pd.Series.tolist(sig[log_var_repeats].iloc[i]), key=abs, reverse=True)[0:10]
    
    vaa_abs = sorted(pd.Series.tolist(abs(sig[log_var_aa].iloc[i])), reverse=True)
    vch_abs = sorted(pd.Series.tolist(abs(sig[log_var_charge].iloc[i])),  reverse=True)
    vmo_abs = sorted(pd.Series.tolist(abs(sig[log_var_motif].iloc[i])), reverse=True)
    vph_abs = sorted(pd.Series.tolist(abs(sig[log_var_physic].iloc[i])),  reverse=True)
    vrc_abs = sorted(pd.Series.tolist(abs(sig[log_var_repeats].iloc[i])), reverse=True)
    
    if Format=="bar": #Draw bar plot
        barWidth = 1
         
        # set height of bar
        bars1 = maa_abs[0:5]
        bars2 = mch_abs[0:5]
        bars3 = mmo_abs[0:5]
        bars4 = mph_abs[0:5]
        bars5 = mrc_abs[0:5]
        bars6 = vaa_abs[0:5]
        bars7 = vch_abs[0:5]
        bars8 = vmo_abs[0:5]
        bars9 = vph_abs[0:5]
        bars10 = vrc_abs[0:5]
        # Set position of bar on X axis
        r1 = np.arange(len(bars1))
        r2 = len(bars1)+np.arange(len(bars2))
        r3 = 2*len(bars1)+np.arange(len(bars3))
        r4 = 3*len(bars1)+np.arange(len(bars4))
        r5 = 4*len(bars1)+np.arange(len(bars5))
        r6 = 5*len(bars1)+np.arange(len(bars6))
        r7 = 6*len(bars1)+np.arange(len(bars7))
        r8 = 7*len(bars1)+np.arange(len(bars8))
        r9 = 8*len(bars1)+np.arange(len(bars9))
        r10 = 9*len(bars1)+np.arange(len(bars10))
        
        fig1 = plt.figure()
        ax1 = SubplotHost(fig1, 111)
        fig1.add_subplot(ax1) 
        # Make the plot
        plt.bar(r1, bars1, color='#36072d', width=barWidth, edgecolor='white')
        plt.bar(r2, bars2, color='#910f3f', width=barWidth, edgecolor='white')
        plt.bar(r3, bars3, color='#9c0615', width=barWidth, edgecolor='white')
        plt.bar(r4, bars4, color='#d45a26', width=barWidth, edgecolor='white')
        plt.bar(r5, bars5, color='#edc92b', width=barWidth, edgecolor='white')       
        plt.bar(r6, bars6, color='#36072d', width=barWidth, edgecolor='white')          
        plt.bar(r7, bars7, color='#910f3f', width=barWidth, edgecolor='white')     
        plt.bar(r8, bars8, color='#9c0615', width=barWidth, edgecolor='white')  
        plt.bar(r9, bars9, color='#d45a26', width=barWidth, edgecolor='white')  
        plt.bar(r10, bars10, color='#edc92b', width=barWidth, edgecolor='white')  
        
                
        
        # Add xticks on the middle of the group bars
        #plt.xlabel('group', fontweight='bold')
        plt.ylabel('z-score', fontweight='bold')   
        
        ax1.xaxis.set_major_locator(MultipleLocator(5))
        labels = [item.get_text() for item in ax1.get_xticklabels()]
        labels[1:11] = '  aa','       charge','       motif','       physic','        repeat','       aa','       charge','       motif','       physic','        repeat'
        ax1.set_xticklabels(labels,fontsize=8)
 
        ax2 = ax1.twiny()
        offset = 0, -20 # Position of the second axis
        new_axisline = ax2.get_grid_helper().new_fixed_axis
        ax2.axis["bottom"] = new_axisline(loc="bottom", axes=ax2, offset=offset)
        ax2.axis["top"].set_visible(False)
        ax2.set_xticks([0.0, 0.5, 1.0])
        ax2.xaxis.set_major_formatter(ticker.NullFormatter())
        ax2.xaxis.set_minor_locator(ticker.FixedLocator([0.25,0.75]))
        ax2.xaxis.set_minor_formatter(ticker.FixedFormatter(['mean', 'log variance']))
    
        ax3 = ax1.twiny()
        offset = 0, -35
        new_axisline = ax3.get_grid_helper().new_fixed_axis
        ax3.axis["bottom"] = new_axisline(loc="bottom", axes=ax3, offset=offset)
        ax3.axis["top"].set_visible(False)

        ax3.set_xticks([0.0, 1.0])
        ax3.xaxis.set_major_formatter(ticker.NullFormatter())
        ax3.xaxis.set_minor_locator(ticker.FixedLocator([0.5]))
        ax3.xaxis.set_minor_formatter(ticker.FixedFormatter(['Molecular Features']))
    
        
        figbar = plt.gcf()
        figbar.subplots_adjust(bottom=0.22)
        figbar.set_size_inches(7, 3.5)
        figbar.savefig('./static/image/sigbar'+str(i)+'.png', dpi=100)
 
        return()
        
    if Format == "div": #Draw diversion plot
        if Group < 6 :
            mean_or_variance="Mean"
        else:
            mean_or_variance="Log Variance"
        group_name={1:"Amino Acid content", 2: "Charge properties",3:"Motifs",
                    4:"Physicochemical properties", 5:"Repeats and complexity",0:"Repeats and complexity"}[(Group) % 5]
        feature={1:mean_aa, 2:mean_charge,3:mean_motif,4:mean_physic,5:mean_repeats,
                 6:log_var_aa,7:log_var_charge,8:log_var_motif,9:log_var_physic,10:log_var_repeats}[Group]
        score_list={1:maa,2:mch,3:mmo,4:mph,5:mrc,6:vaa,7:vch,8:vmo,9:vph,10:vrc}[Group]
        score_list=[x for x in reversed(score_list) if ~np.isnan(x)]
        fvalue=sig[feature].iloc[i]
        feature_list=[None]*len(score_list)
        for x1 in range(len(score_list)):
            for j in range(len(fvalue)):
              if (score_list[x1]==fvalue[j]):
                  feature_list[x1]=fvalue.index[j]
                  feature_list[x1]=feature_list[x1].replace('mean_calc_','')
                  feature_list[x1]=feature_list[x1].replace('log_var_calc_','')
                  
        fig, yx = plt.subplots(constrained_layout=True)
        plt.title('Top {0} Z-scores in \n {1} Group '.format(mean_or_variance, group_name), 
                  fontdict={'size':10})
        plt.hlines(np.arange(len(score_list)), xmin=0, xmax=score_list)
        for x, y, tex in zip(score_list, np.arange(len(score_list)), score_list):
            plt.text(x, y, round(tex, 2), horizontalalignment='right' if x < 0 else 'left', 
                         verticalalignment='center', fontdict={'color':'red' if x < 0 else 'green', 'size':6})
        plt.yticks(np.arange(len(score_list)), feature_list, fontsize=6)
        plt.grid(linestyle='--', alpha=0.35)
        plt.gca().set(ylabel='$Molecular-features$', xlabel='$Z-scores$')
        
        figdiv = plt.gcf()
        figdiv.set_size_inches(5, 3.5)
        figdiv.savefig('./static/image/sigdiv'+str(i)+'g'+str(Group)+'.png', dpi=100)
        plt.clf()
        
        return()


#Draw profile plot
def sigpro(IDR):
    
    values = sig.iloc[IDR,3:]
    fig1 = plt.figure()
    fig1.set_size_inches(7, 3.5)
    plt.subplots_adjust(bottom=0.22)
    ax1 = SubplotHost(fig1, 111)
    fig1.add_subplot(ax1) 
    plt.ylabel("Z-Scores")
    
    ax1.stem(values, markerfmt=' ',use_line_collection=True,basefmt='k-')
    ax1.xaxis.set_major_locator(MultipleLocator(16.4))
    labels = [item.get_text() for item in ax1.get_xticklabels()]
    labels[1:11] = '      aa','          charge','          motif','          physic','           repeat','        aa','          charge','          motif','          physic','          repeat'
    ax1.set_xticklabels(labels,fontsize=8)
    plt.grid(axis='y')
    
    max=np.amax(values)
    max_x=np.argmax(np.array(values))
    max_annot=sig.columns[max_x+3].replace('mean_calc_','')
    max_annot=max_annot.replace('log_var_calc_','')
    min=np.amin(values)
    min_x=np.argmin(np.array(values))
    min_annot=sig.columns[min_x+3].replace('mean_calc_','')
    min_annot=min_annot.replace('log_var_calc_','')
    ax1.annotate(max_annot,fontsize=8,
            xy=(max_x, max), xycoords='data',bbox=dict(boxstyle="round", fc="0.8"),
            xytext=(15, 15), textcoords='offset points',
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="angle,angleA=0,angleB=90,rad=10"))

    ax1.annotate(min_annot,fontsize=8,xy=(min_x, min), xycoords='data',
            xytext=(15, 15), textcoords='offset points',
            bbox=dict(boxstyle="round", fc="0.8"),
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="angle,angleA=0,angleB=-90,rad=10"))
    for k in range(4, int(plt.ylim()[1])):
        ax1.axhspan(k, k+1, color='sandybrown', alpha=0.3)
    for k in range(int(plt.ylim()[0]),-4):
        ax1.axhspan(k, k+1, color='sandybrown', alpha=0.3)
 
    ax2 = ax1.twiny()
    offset = 0, -20 # Position of the second axis
    new_axisline = ax2.get_grid_helper().new_fixed_axis
    ax2.axis["bottom"] = new_axisline(loc="bottom", axes=ax2, offset=offset)
    ax2.axis["top"].set_visible(False)
    ax2.set_xticks([0.0, 0.5, 1.0])
    ax2.xaxis.set_major_formatter(ticker.NullFormatter())
    ax2.xaxis.set_minor_locator(ticker.FixedLocator([0.25,0.75]))
    ax2.xaxis.set_minor_formatter(ticker.FixedFormatter(['mean', 'log variance']))
    
    ax3 = ax1.twiny()
    offset = 0, -35
    new_axisline = ax3.get_grid_helper().new_fixed_axis
    ax3.axis["bottom"] = new_axisline(loc="bottom", axes=ax3, offset=offset)
    ax3.axis["top"].set_visible(False)

    ax3.set_xticks([0.0, 1.0])
    ax3.xaxis.set_major_formatter(ticker.NullFormatter())
    ax3.xaxis.set_minor_locator(ticker.FixedLocator([0.5]))
    ax3.xaxis.set_minor_formatter(ticker.FixedFormatter(['Molecular Features']))
    
    figpro = plt.gcf()
    figpro.set_size_inches(7, 3.5)
    figpro.savefig('./static/image/sigpro'+str(IDR)+'.png', dpi=100)
    plt.clf()


# Find the list of similar IDRs, the first item is the orginal IDR
def simi(IDR):
    return simidf.iloc[IDR,:].tolist()
# Find common name from index
def getname(index):
    return sig.iloc[index,2].split(";")[1].strip()






