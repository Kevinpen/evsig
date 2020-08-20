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
GO_list=['GO:0007093','GO:0007049',	'GO:0044770','GO:0022402', 'GO:0010564', 'GO:0051726', 'GO:0044843','GO:0044839','GO:0016607','GO:0010494','GO:0000932','GO:0043565']

for go in GO_list:
    payload = {'query':  go +  ' AND organism :"homo sapiens" AND reviewed:yes','format': 'tab'}
    result = requests.get(BASE + KB_ENDPOINT, params=payload)
    res = pd.DataFrame(pd.read_csv(StringIO(result.text), sep="\t"))
    res['GO'] = [go]*res.shape[0]
    query = query.append(res)

goterms = query.iloc[:,7].unique() 

data = pd.read_table('./data/sig_human_disopred3.csv')

ccTarg_disopred3 = pd.DataFrame(columns=['IDRname', 'Uniprot ID']+goterms.tolist())
ccTarg_disopred3['IDRname'] = data.iloc[:,0]
ccTarg_disopred3['Uniprot ID'] = data.iloc[:,1]
ccTarg_disopred3.iloc[:,2:] = 0


for i in range(len(data)):
    if data.iloc[i,1] in query.iloc[:,0].values:
        idx = [index for index, value in enumerate(query.iloc[:,0].values) if value ==  data.iloc[i,1]]
        go = query.iloc[idx,7]
        go_col = ccTarg_disopred3.columns.get_loc(go.iloc[0])
        ccTarg_disopred3.iloc[i,go_col] = 1
        


go_ann =[]

for go in GO_list:
    with open("./go.obo", "r") as f:
        for line in f:
            if line=='id: '+go +'\n':
                go_ann.append(go + ', ' + f.readline().rstrip())
        f.close()

ccTarg_disopred3.columns=['IDRname','Uniprot ID'] + go_ann

ccTarg_disopred3.to_csv('./data/moreTarg_disopred3.csv', index=False)

ccTarg_disopred3.sum()
query.to_csv('./query_more.csv',index=False)

