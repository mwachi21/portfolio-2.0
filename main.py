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

@app.route('/faqs')
def faqs():
    return render_template('FAQs.html')

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')

@app.route('/video')
def get_video():
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'static', 'videos', 'home.mp4'))
    if not os.path.exists(path):
        return "Not Found", 404

    size = os.path.getsize(path)
    range_header = request.headers.get('Range', None)

    # If no Range header, let send_file handle full response (sets Content-Length)
    if not range_header:
        return send_file(path, mimetype='video/mp4', conditional=True)

    # Parse Range header (supports suffix and open-ended ranges)
    m = re.search(r'bytes=(\d*)-(\d*)', range_header)
    if not m:
        return "Invalid Range", 400

    start_str, end_str = m.group(1), m.group(2)
    if start_str == '':
        # suffix range: last N bytes
        suffix_len = int(end_str) if end_str else 0
        byte1 = max(0, size - suffix_len)
        byte2 = size - 1
    else:
        byte1 = int(start_str)
        byte2 = int(end_str) if end_str else size - 1

    if byte1 >= size or byte1 > byte2:
        return ("Requested Range Not Satisfiable", 416, {'Content-Range': f'bytes */{size}'})

    length = byte2 - byte1 + 1

    with open(path, 'rb') as f:
        f.seek(byte1)
        data = f.read(length)

    rv = Response(data, status=206, mimetype='video/mp4', direct_passthrough=True)
    rv.headers['Content-Range'] = f'bytes {byte1}-{byte2}/{size}'
    rv.headers['Accept-Ranges'] = 'bytes'
    rv.headers['Content-Length'] = str(length)
    return rv

# Error Handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

if __name__ == '__main__':
    app.run(debug=True)  # Set to False in Production
