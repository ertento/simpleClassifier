from pandas import read_csv

data1=read_csv('hotspotUrbanMobility-1.csv')
print(data1.shape)
data2=read_csv('hotspotUrbanMobility-2.csv')
print(data2.shape)
data1=data1.append(data2, ignore_index=True)
print(data1.shape)
data1.to_csv('completeDataset.csv', index=False)
