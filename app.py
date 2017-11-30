import twitter_data
import model
import plots
from flask import Flask, render_template, request, redirect, url_for


N = 3


app = Flask(__name__)
app.config.from_object(__name__)

def processing(name):
	df = twitter_data.get_all_tweets(name)
	model.clustering(df, N)
	plots.timestamp_graph(df)
	plots.word_cloud(df, N)

@app.route('/')
def index():
    return render_template('input.html')

@app.route('/clustering', methods = ['GET', 'POST'])
def clustering():
	if request.form['name'] is not None:
		name = request.form['name']
		print name
		processing(name)

	return render_template('output.html')

	
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8003, debug=True)