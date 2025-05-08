from flask import Flask, request, render_template, jsonify
from chatbot_handler import get_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_query = data.get("message")
    response = get_response(user_query)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)