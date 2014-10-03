from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/engage', methods=['GET', 'POST'])
def engage():
    if request.method == 'POST':
        #update_engagement()
        return render_template('engage.html', {})
    else:
        #show_engage()
        return render_template('engage.html')


if __name__ == '__main__':
    app.run(debug=True)