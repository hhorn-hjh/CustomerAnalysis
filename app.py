from flask import Flask, render_template, json

from analysis_data import analysis_data

app = Flask(__name__)


@app.route('/')
def root_index():
	return render_template('index.html')


@app.route('/testnumber', methods=['GET', 'POST'])
def test_number():
	res = analysis_data.LRFMC()
	return json.dumps(res)


@app.route('/chart/radar.html')
def echarts5():
	return render_template('/chart/radar.html')


if __name__ == '__main__':
	app.run()
