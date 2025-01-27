import os
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle
from visualizations import create_visualizations

app = Flask(__name__)

# Load pre-trained model
MODEL_PATH = "ml_model.pkl"
model = pickle.load(open(MODEL_PATH, "rb"))

# Load sample dataset
DATA_PATH = "data/marketing_campaigns.csv"
data = pd.read_csv(DATA_PATH)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    input_data = request.json
    features = pd.DataFrame([input_data])
    prediction = model.predict(features)
    return jsonify({"predicted_roi": prediction[0]})

@app.route("/visualize")
def visualize():
    charts = create_visualizations(data)
    return jsonify(charts)

if __name__ == "__main__":
    app.run(debug=True)
