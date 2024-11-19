import streamlit as st 
import requests         
import pandas as pd  



# Add an image to your Streamlit app


# API URL
API_URL = "https://project-5-tbw3.onrender.com/predict"

# Load the cluster DataFrames
try:
    df_0 = pd.read_csv("df_0.csv")
    df_1 = pd.read_csv("df_1.csv")
    df_2 = pd.read_csv("df_2.csv")
    df_3 = pd.read_csv("df_3.csv")
except FileNotFoundError as e:
    st.error("Error: One or more CSV files could not be found.")
    st.write(e)
    st.stop()  # Stop execution if the files are not found

st.image("Card.png", use_container_width=True)


# Storage Type to encoded mapping
storage_type_mapping = {
    'M.2 NVMe PCIe 4.0 SSD': 4,
    'SSD': 13,
    'HDD + 256GB SSD M.2': 18
}

# Set up the Streamlit app
#st.title("Laptops Recommendation Prediction")
#st.subheader("Predict the Optimal Laptop")
#st.markdown("Enter the Laptop details in the sidebar and click 'Predict' to see the recommended Laptops !.")

# Sidebar inputs
#st.sidebar.image("Blue.png", caption="Your Caption Here", use_container_width=True)
st.sidebar.header("Input Parameters")
product_price = st.sidebar.number_input("Product Price", min_value=0, step=1, value=1000)
ram_gb = st.sidebar.number_input("RAM (GB)", min_value=0, max_value=128, step=1, value=16)
storage_capacity_options = [1024., 256., 512., 2048.]
storage_capacity_gb = st.sidebar.selectbox("Storage Capacity (GB)", options=storage_capacity_options)
storage_type = st.sidebar.selectbox("Storage Type", options=list(storage_type_mapping.keys()))

# Button to make the prediction
if st.button("Predict"):
    storage_type_encoded = storage_type_mapping[storage_type]
    payload = {
        "Product_Price": product_price,
        "RAMGB": ram_gb,
        "Storage_Capacity_GB": storage_capacity_gb,
        "Storage_Type_encoded": storage_type_encoded,
    }

    try:
        response = requests.post(API_URL, json=payload)
        response.raise_for_status()
        if "pred" in response.json():
            prediction = response.json()["pred"]
            st.success("Predicted Data:")
            st.balloons()

            # Display the appropriate DataFrame based on the prediction
            if prediction == 0:
               # st.subheader("Cluster 0 Data")
                st.dataframe(df_0)
            elif prediction == 1:
               # st.subheader("Cluster 1 Data")
                st.dataframe(df_1)
            elif prediction == 2:
               # st.subheader("Cluster 2 Data")
                st.dataframe(df_2)
            elif prediction == 3:
               # st.subheader("Cluster 3 Data")
                st.dataframe(df_3)
            else:
                st.error("Invalid cluster index received from the API.")
        else:
            st.warning("The API response did not contain a prediction.")
    except requests.exceptions.RequestException as e:
        st.error("Error connecting to the API. Please check your internet connection or the API URL.")
        st.write(e)

st.markdown("---")
st.markdown("**Note**: This tool is powered by a K-means clustering model.")
