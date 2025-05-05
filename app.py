from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS to handle cross-origin requests
from predict import predict_document  # Import your prediction function

app = Flask(__name__)

# Allow all cross-origin requests
CORS(app)  # This will enable CORS for all routes

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Empty filename'}), 400

    result = predict_document(file)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
