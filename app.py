from flask import Flask, request, jsonify
from predict import predict_document

app = Flask(__name__)

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
    app.run()
