# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 21:14:05 2020

@author: pengg
"""

import pandas as pd
import sys
if sys.version_info[0] < 3: 
    from StringIO import StringIO
else:
    from io import StringIO
    
import requests

BASE = 'http://www.uniprot.org'
KB_ENDPOINT = '/uniprot/'
query = pd.DataFrame(columns=['Entry', 'Entry name', 'Status', 'Protein names', 'Gene names','Organism', 'Length','GO'])
GO_list=['GO:0006974','GO:0035556',	'GO:0004672','GO:0030479', 'GO:0005618', 'GO:0005576','GO:0005643','GO:0010494','GO:0003729','GO:0042254','GO:0006364','GO:0000932','GO:0043565','GO:0005759','GO:0005743']

for go in GO_list:
    payload = {'query':  go +  ' AND organism :"Saccharomyces cerevisiae" AND reviewed:yes','format': 'tab'}
    result = requests.get(BASE + KB_ENDPOINT, params=payload)
    res = pd.DataFrame(pd.read_csv(StringIO(result.text), sep="\t"))
    res['GO'] = [go]*res.shape[0]
    query = query.append(res)

goterms = query.iloc[:,7].unique() 

data = pd.read_table('./data/sig_yeast_2020.csv')

pTarg_yeast = pd.DataFrame(columns=['IDRname', 'systematic name']+goterms.tolist())
pTarg_yeast['IDRname'] = data.iloc[:,0]
pTarg_yeast['systematic name'] = data.iloc[:,1]
pTarg_yeast.iloc[:,2:] = 0

# Get uniprot id for yeast protein from systematic name
yeast_ref = pd.read_table("./data/yeast_reference.csv")
def getuni(sys):
    for i in range(len(yeast_ref)):
        if yeast_ref.iloc[i,0] == sys:
            return yeast_ref.iloc[i,1]
    return None   

#For human data
for i in range(len(data)):
    if data.iloc[i,1] in query.iloc[:,0].values:
        idx = [index for index, value in enumerate(query.iloc[:,0].values) if value ==  data.iloc[i,1]]
        go = query.iloc[idx,7]
        go_col = pTarg_yeast.columns.get_loc(go.iloc[0])
        pTarg_yeast.iloc[i,go_col] = 1

#For yeast data
for i in range(len(data)):
    uni = getuni(data.iloc[i,1])
    if uni in query.iloc[:,0].values:
        idx = [index for index, value in enumerate(query.iloc[:,0].values) if value == uni]
        go = query.iloc[idx,7]
        go_col = pTarg_yeast.columns.get_loc(go.iloc[0])
        pTarg_yeast.iloc[i,go_col] = 1     


go_ann =[]

for go in GO_list:
    with open("../flaskweb/go.obo", "r") as f:
        for line in f:
            if line=='id: '+go +'\n':
                go_ann.append(go + ', ' + f.readline().rstrip())
        f.close()

pTarg_yeast.columns=['IDRname','systematic name'] + go_ann

pTarg_yeast.to_csv('./data/pTarg_yeast.csv', index=False)

pTarg_yeast.sum()
query.to_csv('./pquery_yeast.csv',index=False)

