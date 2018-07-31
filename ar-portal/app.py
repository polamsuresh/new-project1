import logging
import os

from flask import Flask, request, jsonify, render_template, url_for, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.logger.setLevel(logging.INFO)

models = os.listdir("./images/model")

items = os.listdir("./images/product")
items = sorted(items)

@app.route('/')
def home():
	slice=items[:100]
	return render_template('single.html', items=slice[:10], c_items=[slice[i:i + 9] for i in range(0, len(slice), 9)], models=models[:10])

@app.route('/login')
def login():
    return render_template('login.html', items=items[:3], models=models[:3])


@app.route('/checkout')
def checkout():
    return render_template('checkout.html', items=items[:3], models=models[:3])


@app.route('/registered')
def registered():
    return render_template('registered.html', items=items[:3], models=models[:3])


@app.route('/api/models', methods=['GET'])
def get_models():
    model_response = []
    for i in models:
        item = {
            'name': "model " + i,
            'image_url': url_for('asset', item="model/" + i)
        }
        model_response.append(item)
    response = {
        'code': 0,
        'models': model_response
    }
    return jsonify(response)


@app.route('/api/items', methods=['GET'])
def api_items():
    items_response = []
    for i in items:
        item = {
            'name': "item " + i,
            'image_url': url_for('asset', item="product/" + i)
        }
        items_response.append(item)
    response = {
        'code': 1,
        'items': items_response
    }
    return jsonify(response)


@app.route('/items', methods=['POST'])
def api_items_post():
    if request.headers.get('Content-Type') == 'application/json':
        return jsonify(request.json)
    else:
        app.logger.info('invalid content')
        response = {
            'code': 1,
            'message': 'unsupported protocol'
        }
        return jsonify(response)


@app.route('/assets/<path:item>')
def asset(item):
    if not item:
        return ''
    else:
        return send_from_directory('images', item)


@app.route('/<path:item>')
def asset_static(item):
    file_path = os.path.join(app.static_folder, item)
    print("file_path", file_path)
    if os.path.isfile(file_path):
        return send_from_directory(app.static_folder, item)
    else:
        return '', 404


if __name__ == '__main__':
    app.run(host='0.0.0.0')
