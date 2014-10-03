from flask import Flask, render_template
import requests
import csv
import StringIO

app = Flask(__name__)


@app.route('/engage')
def engage():
    data_url = 'https://raw.githubusercontent.com/jenlindner/two-way-street/master/engagement.csv'

    response = requests.get(data_url)
    data = StringIO.StringIO(response.text)
    context = {
      'data_dict': [],
    }
    
    for row in csv.DictReader(data):
      context['data_dict'].append(row)

    return render_template('engage.html', **context)


if __name__ == '__main__':
    app.run(debug=True)