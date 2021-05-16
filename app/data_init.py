import pandas as pd

def load_data():
  datasets = pd.read_csv("./data/dataset_config.csv", sep='\t')
  datasets_name = datasets.iloc[:,0]
  examples = []
  for i in range(datasets.shape[0]):
     for j in range(4,7):
         examples.append(datasets.iloc[i,j])
  return datasets,datasets_name,examples