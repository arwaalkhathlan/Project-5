import streamlit as st
import requests

# API URL
API_URL = "https://project-5-tbw3.onrender.com/predict"

# Storage Type to encoded mapping
storage_type_mapping = {
    'M.2 NVMe PCIe 4.0 SSD': 4,
    'SSD': 13,
    'M.2 NVMe PCIe 3.0 SSD': 3,
    'PCIe Gen4': 10,
    'NVMe M.2 SSD': 6,
    'PCIe Gen 4 NVMe M.2 SSD': 9,
    'PCIe NVMe M.2 SSD': 11,
    '': 0,
    'NVMe PCIe Gen 4×4 SSD': 7,
    'PCIe 3.0 NVMe M.2 SSD': 8,
    'PCIe NVMe M.3 SSD': 12,
    'M.2 PCIe NVMe 4.0 SSD': 5,
    'SSD M.2': 14,
    'SSD M.2 + 16GB Intel Optane Memory': 16,
    'SSD M.2 + 32GB Intel Optane Memory': 1,
    'HDD': 17,
    'SSD M.2 2280 PCIe 4.0x4 NVMe': 2,
    'eMMC': 15,
    'HDD + 256GB SSD M.2': 18
}

# Processor Type to encoded mapping




st.title("Product Recommendation Prediction")

# Input fields for the features
product_price = st.number_input("Product Price", min_value=0, step=1, value=1000)

# Dropdown for RAM (max 128 GB)
ram_gb = st.number_input("RAM (GB)", min_value=0, max_value=128, step=1, value=16)

# Dropdown for Storage Capacity
storage_capacity_options = [1024., 256., 512., 2048.]
storage_capacity_gb = st.selectbox("Storage Capacity (GB)", options=storage_capacity_options)

# Dropdown for Storage Type
storage_type = st.selectbox("Storage Type", options=list(storage_type_mapping.keys()))


# Button to make the prediction
if st.button("Predict"):
    # Encode the selected storage type and processor type
    storage_type_encoded = storage_type_mapping[storage_type]

    # JSON payload for the API
    payload = {
        "Product_Price": product_price,
        "RAMGB": ram_gb,
        "Storage_Capacity_GB": storage_capacity_gb,
        "Storage_Type_encoded": storage_type_encoded,
    }

    # Make a POST request to the FastAPI
    try:
        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            prediction = response.json().get("pred")
            st.success(f"Predicted Cluster: {prediction}")
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        st.error(f"Error connecting to the API: {e}")
