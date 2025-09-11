import os
import re
from flask import Flask, render_template, Response, request, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/weather')
def weather():
    return render_template('weather.html')

@app.route('/design')
def design():
    return render_template('design.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/video')
def get_video():
    path = os.path.abspath("static/videos/home.mp4")  # 👈 update this path as needed
    range_header = request.headers.get('Range', None)
    if not range_header:
        return send_file(path)

    size = os.path.getsize(path)
    byte1, byte2 = 0, None

    m = re.search(r'bytes=(\d+)-(\d*)', range_header)
    if m:
        byte1 = int(m.group(1))
        if m.group(2):
            byte2 = int(m.group(2))

    byte2 = byte2 or size - 1
    length = byte2 - byte1 + 1

    with open(path, 'rb') as f:
        f.seek(byte1)
        data = f.read(length)

    rv = Response(data,
                  206,
                  mimetype='video/mp4',
                  content_type='video/mp4',
                  direct_passthrough=True)
    rv.headers.add('Content-Range', f'bytes {byte1}-{byte2}/{size}')
    rv.headers.add('Accept-Ranges', 'bytes')
    return rv

# Error Handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

if __name__ == '__main__':
    app.run(debug=True)  # Set to False in Production
