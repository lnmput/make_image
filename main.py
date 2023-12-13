from flask import Flask, jsonify, render_template

from api.start import make_image

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/create')
def create():
    base64_image = make_image()
    return jsonify({'image': base64_image})


@app.route('/test')
def test():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
