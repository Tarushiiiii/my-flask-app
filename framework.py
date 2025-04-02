from flask import Flask, request, jsonify 
import joblib 
import numpy as np

app = Flask(__name__) 

# Load model and preprocessing steps 
model = joblib.load('model.pkl') 
scaler = joblib.load('scaler.pkl') 

@app.route("/")
def home():
    return "Hello, Flask is running inside Docker!"

@app.route('/predict', methods=['POST']) 
def predict(): 
    data = request.json  # Assuming JSON input 
    # Preprocess data (if needed) 
    # Example: Scale input features 
    scaled_data = scaler.transform(np.array(data["features"]).reshape(1, -1))

    # Make prediction 
    prediction = model.predict(scaled_data) 
    return jsonify({'prediction': prediction.tolist()}) 

if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=5000, debug=True)