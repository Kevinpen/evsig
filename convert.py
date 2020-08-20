# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 11:47:15 2020

@author: pengg
"""
import pandas as pd

# Convert annoataion data to standard format
ann = pd.read_table("./hs_mCD_Zscores_go_annotated.csv", dtype="object")
data = pd.read_table("./sig_human_disopred3.csv")


cv = []
for i in range(ann.shape[0]):
  if (ann.iloc[i,0] not in data.iloc[:,0].values):
    cv.append(i)
if(pd.notnull(cv).all()):
  ann = ann.drop(ann.index[cv])
ann.reset_index(drop=True, inplace=True)


target = pd.DataFrame(columns=["idr_name","protein_name"],index=range(ann.shape[0]))
target.iloc[:,0] = ann.iloc[:,0]
target.iloc[:,1] = ann.iloc[:,1]

for  i in range(ann.shape[0]):
    for j in range(2,ann.shape[1]):
        if (pd.notnull(ann.iloc[i,j])):
            if ann.iloc[i,j] not in target.columns:
                target[ann.iloc[i,j]] = pd.Series()
            target.loc[i,ann.iloc[i,j]] = 1

target = target.fillna(0)
target.to_csv('./target.csv')

colsum = target.iloc[:,2:].sum(axis=0)
colsum.hist()
colsum[2:500].hist()
colsum[2:].sort_values(ascending=False)[0:20].index

top_target = pd.DataFrame(columns=["idr_name","protein_name"],index=range(ann.shape[0]))
top_target.iloc[:,0] = ann.iloc[:,0]
top_target.iloc[:,1] = ann.iloc[:,1]


top_target = top_target.join(target[colsum[2:].sort_values(ascending=False)[0:20].index])
top_target.to_csv('./top_target.csv')


# Create target file for SPOTd IDR dataset
target_copy = pd.read_csv("./target.csv")
data_SPOTd = pd.read_table("./sig_human_SPOTd.csv")
target_SPOTd = pd.DataFrame(columns=target_copy.columns)
data_SPOTd = data_SPOTd.rename(columns={"IDR name":"idr_name","Uniprot ID":"protein_name"})


for i in range(data_SPOTd.shape[0]):
    for j in range(target_copy.shape[0]):
        if ((data_SPOTd.iloc[i,0].split("_")[0] == target_copy.iloc[j,0].split("_")[0]) 
            and (data_SPOTd.iloc[i,0] not in target_SPOTd.iloc[:,0].to_string())):
            target_SPOTd = target_SPOTd.append(pd.concat([data_SPOTd.iloc[i,0:2],target_copy.iloc[j,2:1023]]),
                                               sort=False,ignore_index=True)



target_SPOTd.to_csv('./target_SPOTd.csv')
colsum_SPOTd = target_SPOTd.iloc[:,2:].sum(axis=0)
colsum_SPOTd[2:].sort_values(ascending=False)[0:20].index
top_SPOTd = pd.DataFrame(columns=["idr_name","protein_name"],index=range(target_SPOTd.shape[0]))
top_SPOTd.iloc[:,0] = target_SPOTd.iloc[:,0]
top_SPOTd.iloc[:,1] = target_SPOTd.iloc[:,1]


top_SPOTd = top_SPOTd.join(target_SPOTd[colsum_SPOTd[2:].sort_values(ascending=False)[0:20].index])
top_SPOTd.to_csv('./top_SPOTd.csv', index=False)

