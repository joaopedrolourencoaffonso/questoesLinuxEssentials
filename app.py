from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route('/')
def hello_moon():
    return render_template('index.html')

@app.route('/data')
def json_data():
    with open('static\\questoes.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
