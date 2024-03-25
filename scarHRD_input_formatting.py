import pandas as pd
import numpy as np
import glob
file = glob.glob('*segments.txt')[0]

df = pd.read_table(file,comment='#',index_col=False, header=None)

#df = pd.read_table('C:/Users/sombuddharoy.bhowmic/Desktop/Trial/KH-22RS98-FT_S8.segments.txt', comment='#',index_col=False, header=None)
df.columns=["SampleID","Chromosome","Start_position", "End_position","A_cn","B_cn"]

df = df.iloc[1:, :]
df.insert(4, "total_cn", "")

df['total_cn'] = df['A_cn'].astype(int) + df['B_cn'].astype(int)

df_1 = pd.read_table('Ploidy.txt', comment='#',index_col=False, header=None)
df_1.columns=["Ploidy"]
df_1 = df_1.iloc[1:, :]

df.insert(7, "ploidy", "")

df_B = df.assign(ploidy=df_1['Ploidy'])
df_B['ploidy']= df_B['ploidy'].fillna(df_B['ploidy'].iloc[0])

df_B.to_csv(r'scarHRD_Input.txt', header=True, index=None, sep='\t')


