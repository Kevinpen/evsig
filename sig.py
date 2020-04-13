

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator)
import matplotlib.ticker as ticker
from mpl_toolkits.axes_grid.parasite_axes import SubplotHost


datasets = pd.read_csv("./sig/dataset_config.csv", sep='\t')

sigs = []
groups = []
sims = []
for i in range(datasets.shape[0]):
    sigs.append(pd.read_csv("./sig/"+datasets.iloc[i,1],low_memory=False,sep='\t'))
    groups.append(pd.read_csv("./sig/"+datasets.iloc[i,2],sep='\t'))
    sims.append(pd.read_csv("./sig/"+datasets.iloc[i,3],sep='\t', header=None))
    
for i in range(datasets.shape[0]):
    sigs[i].iloc[:,3:] = sigs[i].iloc[:,3:].fillna(0)
    
for i in range(datasets.shape[0]):
    sigs[i].iloc[:,1:3] = sigs[i].iloc[:,1:3].fillna("N/A")



#Get group 
def getgroup(dataset):
    return groups[dataset]

#Find index by idr name
def getindex_idr(name, dataset):
    test = sigs[dataset].iloc[:,0]==name
    if test.any()  == False:
        return -1
    else:
        return sigs[dataset].index.values[sigs[dataset].iloc[:,0]==name][0]  

# Find idrname by protein common name
def getindex_cid(name, dataset):
    index = []
    for i in range(len(sigs[dataset])):
        cid =  sigs[dataset].iloc[i,2]  # in this table, third column is common name separated by ";"
        if cid.lower() == name.lower():
            index.append(sigs[dataset].iloc[i,0])
    return index

#Find idrname by systematic name
def getindex_sid(name, dataset):
    index = []
    for i in range(len(sigs[dataset])):
        sid =  sigs[dataset].iloc[i,1]
        if sid.lower() == name.lower():
            index.append(sigs[dataset].iloc[i,0])
    return index

# Find the list of similar IDRs, the first item is the orginal IDR
def getsimi(IDR, dataset):
    return sims[dataset].iloc[IDR,:].tolist()

# Find common name from index
def getname(index, dataset):
    return sigs[dataset].iloc[index,2]

def get_dataset_name(index):
    return datasets.iloc[index,0]

# Data figures
def sigviz(IDR, Format="bar", Group=1, dataset=0):    
    i=IDR
    
    # ZScore Values of every group sorted by absolute value
    group_sort = [[None for _ in range(len(groups[dataset]))] for _ in range(datasets.shape[0])]
    for x in range(datasets.shape[0]):
      for y in range(len(groups[dataset])):
        group_sort[x][y] = sorted(pd.Series.tolist(sigs[dataset].iloc[i,groups[dataset].iloc[y,3]-1:groups[dataset].iloc[y,4]]), key =abs, reverse=True)
        
    # Sortd absolute ZScore values for features in every group
    group_abs = [[None for _ in range(len(groups[dataset]))] for _ in range(datasets.shape[0])]
    for x in range(datasets.shape[0]):
      for y in range(len(groups[dataset])):
        group_abs[x][y] = sorted(pd.Series.tolist(abs(sigs[dataset].iloc[i,groups[dataset].iloc[y,3]-1:groups[dataset].iloc[y,4]])), reverse=True)
    
    #Calculate number of features in every group
    group_len = [[groups[x].iloc[y,4] - groups[x].iloc[y,3] + 1 for y in range(len(groups[dataset]))] for x in range(datasets.shape[0])]
     
    #Group with maximum 5 feature length
    group_len_limited = [[min(group_len[x][y] ,5) for y in range(len(groups[dataset]))] for x in range(datasets.shape[0])]



    
    if Format=="bar": #Draw bar plot
        barWidth = 1
      
        fig1 = plt.figure()
        ax1 = SubplotHost(fig1, 111)
        fig1.add_subplot(ax1) 
        
        # Make the plot
        colors = ['#36072d', '#910f3f', '#9c0615', '#d45a26', '#edc92b', '#36072d', '#910f3f', '#9c0615', '#d45a26', '#edc92b'  ]
        for x in range(10):
            plt.bar(sum(len for len in group_len_limited[dataset][0:x]) + np.arange(min(group_len[dataset][x],5))+1, group_abs[dataset][x][0:5],
                    color=colors[x], width=barWidth, edgecolor='white')


     
        # Add xticks on the middle of the group bars
        #plt.xlabel('group', fontweight='bold')
        plt.ylabel('z-score', fontweight='bold')
        #plt.xticks(2+np.arange(50,step=5), ['mean_aa','mean_charge', 'mean_motif', 'mean_physic', 'mean_repeats',
                  #'var_aa','var_charge' ,'var_motif' , 'var_physic','var_repeats']
        #,fontsize=6)    
        
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
        mean_or_variance = groups[dataset].iloc[Group-1,0]
        group_name = groups[dataset].iloc[Group-1,2]
        colnames = sigs[dataset].columns.values
        feature = colnames[groups[dataset].iloc[Group-1,3]-1:groups[dataset].iloc[Group-1,4]]
        score_list = group_sort[dataset][Group-1][0:10]
        score_list=[x for x in reversed(score_list) if ~np.isnan(x)]
        fvalue=sigs[dataset][feature].iloc[i]
        feature_list=[None]*len(score_list)
        for x1 in range(len(score_list)):
            for j in range(len(fvalue)):
              if (score_list[x1]==fvalue[j]):
                  feature_list[x1]=fvalue.index[j]
                  
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
def sigpro(IDR, dataset):
    
    values = sigs[dataset].iloc[IDR,3:]
    fig1 = plt.figure()
    fig1.set_size_inches(7, 3.5)
    plt.subplots_adjust(bottom=0.22)
    ax1 = SubplotHost(fig1, 111)
    fig1.add_subplot(ax1) 
    plt.ylabel("Z-Scores")
    #xloc=[len(mean_aa),len(mean_motif),len(mean_charge),len(mean_physic),len(mean_repeats)]
    ax1.stem(values, markerfmt=' ',use_line_collection=True,basefmt='k-')
    ax1.xaxis.set_major_locator(MultipleLocator(16.4))
    labels = [item.get_text() for item in ax1.get_xticklabels()]
    labels[1:11] = 'aa','charge','motif','physic','repeat','aa','charge','motif','physic','repeat'
    ax1.set_xticklabels(labels, horizontalalignment="left",fontsize=8)
    plt.grid(axis='y')
    
    max=np.amax(values)
    max_x=np.argmax(np.array(values))
    min=np.amin(values)
    min_x=np.argmin(np.array(values))
    ax1.annotate(sigs[dataset].columns[max_x+3],fontsize=8,
            xy=(max_x, max), xycoords='data',bbox=dict(boxstyle="round", fc="0.8"),
            xytext=(15, 15), textcoords='offset points',
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="angle,angleA=0,angleB=90,rad=10"))

    ax1.annotate(sigs[dataset].columns[min_x+3],fontsize=8,xy=(min_x, min), xycoords='data',
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









