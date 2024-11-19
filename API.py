from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# Initialize the FastAPI app
app = FastAPI()

# Load model and scaler
model = joblib.load('kmeans_model.joblib')
scaler = joblib.load('scaler.joblib')

@app.get("/")
def root():
    return "Welcome To my work"

# Define the Pydantic model for input validation
class InputFeatures(BaseModel):
    Product_Price: int
    RAMGB: int
    Storage_Capacity_GB: float
    Storage_Type_encoded: int

# Define the preprocessing function outside the class
def preprocessing(input_features: InputFeatures):
    dict_f = {
        'Product_Price': input_features.Product_Price,
        'RAMGB': input_features.RAMGB,
        'Storage_Capacity_GB': input_features.Storage_Capacity_GB,
        'Storage_Type_encoded': input_features.Storage_Type_encoded,
    }
    print(f"dict_f: {dict_f}")  # Debug log
    features_list = [dict_f[key] for key in sorted(dict_f)]
    print(f"features_list: {features_list}")
    scaled_features = scaler.transform([features_list])
    return scaled_features

@app.post("/predict")
async def predict(input_features: InputFeatures):
    data = preprocessing(input_features)
    y_pred = model.predict(data)
    return {"pred": y_pred.tolist()[0]}
