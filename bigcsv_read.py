import pandas as pd
chunk_size = 300
batch_no = 1
for chunk in pd.read_csv('gdp.csv',chunksize = chunk_size):
    chunk.to_csv('gdp'+str(batch_no)+'.csv',index=False)
    batch_no +=1
