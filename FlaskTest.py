from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    qiniuurl = url_for_qiniu()
    return render_template('index.html', url=qiniuurl)

@app.route('/<url>')
def index(url=None):
    if url == 'about.html':
        template = 'about.html'
    else:
        template = 'index.html'
    qiniuurl = url_for_qiniu()
    return render_template(template, url=qiniuurl)


@app.route('/about/')
def abouts():
    qiniuurl = url_for_qiniu()
    return render_template('about.html', url=qiniuurl)


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
    qiniuurl = url_for_qiniu()
    return render_template(template, url=qiniuurl)

@app.route('/meweixin.html')
def meweixin():
    qiniuurl = url_for_qiniu()
    return render_template('meweixin.html', url=qiniuurl)

@app.route('/working/')
def work():
    qiniuurl = url_for_qiniu()
    return render_template('working.html', url=qiniuurl)


@app.route('/working/<url>')
def working(url=None):
    if url == 'meweixin.html':
        template = 'meweixin.html'
    if url == 'about.html':
        template = 'about.html'
    if url == 'photos.html':
        template = 'photos.html'
    qiniuurl = url_for_qiniu()
    return render_template(template, url=qiniuurl)


@app.route('/photos/')
def photos():
    qiniuurl = url_for_qiniu()
    return render_template('photos.html', url=qiniuurl)


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
    qiniuurl = url_for_qiniu()
    return render_template(template, url=qiniuurl)


def url_for_qiniu():
    return 'http://7xih5z.com1.z0.glb.clouddn.com'

if __name__ == '__main__':
    app.debug = True
    app.run()
