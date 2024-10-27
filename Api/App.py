from flask import Flask, request, jsonify
from flask_cors import CORS
from modelling import get_response  # Make sure this path is correct

app = Flask(__name__)
CORS(app)

@app.route('/api/process', methods=['POST'])
def process_input():
    data = request.get_json()
    user_query = data.get("userInput", "")
    answer = get_response(user_query)
    return jsonify(result=answer)

# Vercel requires this handler to use the app in a serverless function
def handler(event, context):
    return app(event, context)
print("Working")