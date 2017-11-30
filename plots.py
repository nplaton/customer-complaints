from nltk.corpus import stopwords
from wordcloud import WordCloud
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def timestamp_graph(df):
	df['time_stamp'] = pd.to_datetime(df["time_stamp"], format="%Y-%m-%d")
	df['day'] = df['time_stamp'].apply(lambda x: x.date())
	tweets = df.groupby('day').agg({'time_stamp': np.size})
	plot = tweets.plot(figsize=(15,10))
	fig = plot.get_figure()
	fig.savefig("images/daily_tweets.png")

def aggregate_text(series):
    return " ".join(series.tolist())

def generate_cloud(text, i):
    wordcloud = WordCloud(background_color='white').generate(text)
    plt.figure(figsize=(20, 20))
    plt.imshow(wordcloud)
    plt.axis("off");
    plt.savefig("images/cluster_" + str(i))

def word_cloud(df, n):
	for i in range(n):
	    text =  aggregate_text(df[df["cluster"] == i]["tweets"])
	    generate_cloud(text, i)