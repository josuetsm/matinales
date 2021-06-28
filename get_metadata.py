import grequests
import pandas as pd
from pyquery import PyQuery
from tqdm import tqdm

df_urls = pd.read_csv('data/videos_url.csv')

urls = df_urls['url'].tolist()

df_columns = ['name', 'description', 'paid', 'channelId', 'videoId', 'duration',
              'unlisted', 'width', 'height', 'playerType', 'width', 'height',
              'isFamilyFriendly', 'regionsAllowed', 'interactionCount', 'datePublished',
              'uploadDate', 'genre']

df_list = []

for k in tqdm(range(33)):
    rs = (grequests.get(u) for u in urls[k*1000:(k+1)*1000])
    response = grequests.map(rs)

    itemprops = []
    for resp in response:
        pq = PyQuery(resp.text)
        itemprops.append([PyQuery(item).attr('content') for item in pq('meta[itemprop]')[:18]])

    df_list.append(pd.DataFrame(itemprops, columns=df_columns))


df = pd.concat(df_list, ignore_index=True)

df['url'] = 'https://www.youtube.com/watch?v=' + df['videoId']

df_urls = df_urls.join(df.set_index('url'), on='url')

df_urls.to_csv('data/videos_metadata.csv', index=False)
