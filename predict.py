import cv2
import numpy as np
import joblib
import os
import tempfile

# Load model
model_path = 'random_forest_model.pkl'
clf = joblib.load(model_path)

# Extract features
def extract_features(image_path):
    image = cv2.imread(image_path, 0)
    if image is None:
        return None
    image = cv2.resize(image, (100, 100))
    return image.flatten()

# Predict function
def predict_document(file):
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as temp:
            file.save(temp.name)
            features = extract_features(temp.name)
            os.unlink(temp.name)

        if features is None:
            return 'Invalid Image'

        prediction = clf.predict([features])[0]
        return 'Real Document' if prediction == 1 else 'Fake Document'

    except Exception as e:
        return f'Error: {str(e)}'
