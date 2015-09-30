from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/<url>')
def index(url=None):
    if url == 'about.html':
        template = 'about.html'
    else:
        template = 'index.html'
    return render_template(template)


@app.route('/about/')
def abouts():
    return render_template('about.html')


@app.route('/about/<url>')
def about(url=None):
    if url == 'meweixin.html':
        template = 'meweixin.html'
    if url == 'working.html':
        template = 'working.html'
    if url == 'photos.html':
        template = 'photos.html'
    if url == 'about.html':
        template = 'about.html'
    return render_template(template)

@app.route('/meweixin.html')
def meweixin():
    return render_template('meweixin.html')

@app.route('/working/')
def work():
    return render_template('working.html')


@app.route('/working/<url>')
def working(url=None):
    if url == 'meweixin.html':
        template = 'meweixin.html'
    if url == 'about.html':
        template = 'about.html'
    if url == 'photos.html':
        template = 'photos.html'
    if url == 'working.html':
        template = 'working.html'
    return render_template(template)


@app.route('/photos/')
def photos():
    return render_template('photos.html')


@app.route('/photos/<url>')
def photosURL(url=None):
    if url == 'amuserment.html':
        template = 'amuserment.html'
    if url == 'college.html':
        template = 'college.html'
    if url == 'copper.html':
        template = 'copper.html'
    if url == 'cultural.html':
        template = 'cultural.html'
    if url == 'me.html':
        template = 'me.html'
    if url == 'school.html':
        template = 'school.html'
    if url == 'studio.html':
        template = 'studio.html'
    if url == 'beach.html':
        template = 'beach.html'
    if url == 'tianjin.html':
        template = 'tianjin.html'
    if url == 'zoo.html':
        template = 'zoo.html'
    if url == 'square.html':
        template = 'square.html'
    if url == 'beijin.html':
        template = 'beijin.html'
    if url == 'photos.html':
        template = 'photos.html'
    if url == 'working.html':
        template = 'working.html'
    if url == 'about.html':
        template = 'about.html'
    if url == 'meweixin.html':
        template = 'meweixin.html'
    return render_template(template)


if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0')
