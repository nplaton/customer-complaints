import twitter_data
import model
import plots
from flask import Flask, render_template, request, redirect, url_for


N = 3


app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def index():
    return render_template('templates/input.html')

@app.route('/clustering')
def clustering():
	screen_name = 'iberia'
	df = twitter_data.get_all_tweets(screen_name)
	model.clustering(df, N)
	plots.timestamp_graph(df)
	plots.word_cloud(df, N)

	
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8003, debug=True)