from flask import Flask, render_template
import requests
import csv

app = Flask(__name__)


@app.route('/engage')
def engage():
    data_url = 'https://raw.githubusercontent.com/jenlindner/two-way-street/master/engagement.csv'
    data = requests.get(data_url)
    print data.content

    return render_template('engage.html', data=data.content)


if __name__ == '__main__':
    app.run(debug=True)