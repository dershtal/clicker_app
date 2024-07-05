from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Хранилище данных игры (может быть заменено на базу данных)
user_data = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/click', methods=['POST'])
def click():
    data = request.get_json()
    user_id = data.get('user_id')
    
    if user_id not in user_data:
        user_data[user_id] = 0

    user_data[user_id] += 1
    return jsonify(score=user_data[user_id])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
