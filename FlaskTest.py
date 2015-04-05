from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/photos/')
def photos():
    return render_template('photos.html')

@app.route('/photos/amuserment.html')
def amuserment():
    return render_template('amuserment.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
