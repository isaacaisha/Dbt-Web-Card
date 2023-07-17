from flask import Flask, render_template
import random
import time

app = Flask(__name__)


@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('images/favicon.ico')


@app.route('/', methods=['GET', 'POST'])
def home():
    time_sec = time.localtime()
    current_year = time_sec.tm_year
    random_number = random.randint(1, 9)
    return render_template('index.html', num=random_number, year=current_year)
    # return 'Siisi Chacal, Once Again👌🏿🙃💪🏿'


@app.route('/style/<name>')
def style(name=None):
    return render_template('style.css', name=name)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
