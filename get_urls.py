import pandas as pd
import pytube

channel = pytube.Channel('https://www.youtube.com/user/canal13/')

video_urls = []
for url in channel.video_urls:
    video_urls.append(url)

len(video_urls)

df = pd.DataFrame({'canal': 'canal13', 'url': video_urls})

df.to_csv('data/videos_url.csv', index=False)
