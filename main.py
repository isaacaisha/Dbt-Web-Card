from flask import Flask, render_template
from datetime import datetime
import time

app = Flask(__name__)


@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('images/favicon.ico')


@app.route('/')
def home():
    time_sec = time.localtime()
    current_year = time_sec.tm_year
    # getting the current date and time
    current_datetime = datetime.now()
    # getting the time from the current date and time in the given format
    current_time = current_datetime.strftime("%a/%d/%B")
    return render_template('index.html', date=current_time, year=current_year)
    # return 'Siisi Chacal, Once Again👌🏿🙃💪🏿'


@app.route('/index.html', methods=['POST'])
def home_():
    time_sec = time.localtime()
    current_year = time_sec.tm_year
    # getting the current date and time
    current_datetime = datetime.now()
    # getting the time from the current date and time in the given format
    current_time = current_datetime.strftime("%a/%d/%B")
    return render_template('index.html', date=current_time, year=current_year)
    # return 'Siisi Chacal, Once Again👌🏿🙃💪🏿'


@app.route('/style/<name>')
def style(name=None):
    return render_template('style.css', name=name)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
