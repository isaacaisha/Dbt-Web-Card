from flask import Flask, render_template

import main

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    # Your code here
    return render_template('index.html')


@app.route('/style/<name>')
def style(name=None):
    return app.send_static_file(name)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
