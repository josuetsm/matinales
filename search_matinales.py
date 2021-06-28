import pandas as pd
import re

df = pd.read_csv('data/videos_metadata.csv')
df = df.sort_values('uploadDate').reset_index(drop=True)


df['duration'].apply(lambda s: s[-3:-1])

df['duration'].apply(lambda s: s.split('M')[-1][:-1])

df['seconds'] = df['duration'].apply(lambda s: int(s.split('M')[-1][:-1]))
df['minutes'] = df['duration'].apply(lambda s: int(s.split('M')[-2][2:]))

bienvenidos = df[['name', 'uploadDate', 'minutes']][df['name'].apply(lambda s: bool(re.match('bienvenidos', s.lower()))) &
                                                  (df['minutes'] > 60)]



