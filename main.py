from flask import Flask, jsonify, render_template, request

from api.start import make_image

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/create', methods=['POST'])
def create():
    data = request.json
    # 在这里处理提交的数据
    # 假设你想要返回处理后的数据
    title = data.get('title')
    words = data.get('words')

    base64_img = make_image(title, words)

    processed_data = {'base64_img': base64_img}
    return jsonify(processed_data)


@app.route('/test')
def test():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
