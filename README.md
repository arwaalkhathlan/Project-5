# Laptop Recommendation System

This project is a web-based application built using Streamlit to recommend optimal laptops based on user-defined input parameters. The application leverages a K-means clustering model to group laptops into different clusters, helping users find their perfect laptop match based on their preferences.

---

## Project Overview

The **Laptop Recommendation System** uses machine learning to categorize laptops into clusters. Users can input details such as product price, RAM size, storage capacity, and storage type, and the app will predict the optimal laptop cluster for their needs. The goal is to simplify the laptop selection process for users by providing personalized recommendations.

---

## Features

- **Interactive User Interface**: The app is built using Streamlit, providing a simple and user-friendly experience.
- **Dynamic Input Parameters**: Users can input specific requirements in the sidebar, including:
  - Product Price
  - RAM (GB)
  - Storage Capacity (GB)
  - Storage Type
- **Machine Learning Model**: Utilizes a K-means clustering algorithm to classify laptops into clusters based on specifications.
- **Laptop Clusters**: The app displays the recommended laptops from the cluster that best matches the user's input.

---

## Data Collection

### Web Scraping
The data for this project was collected from two major retail websites, **Jarir** and **Golden**, using web scraping techniques. The scraping process involved extracting laptop specifications such as:

- Product Name
- Product Price
- Warranty Period
- Processor Type
- Screen Size
- Operating System
- Color
- RAM Size
- Touch Display
- Display Resolution
- Battery Type
- Storage Type
- Storage Capacity
- Screen Resolution (Width and Height)

### Tools Used for Web Scraping
- **Python Libraries**: BeautifulSoup, Requests, and Pandas were used to collect and clean the data.

---

## Application Workflow

1. **User Input**: The user enters details in the sidebar, such as the desired price, RAM, storage capacity, and storage type.
2. **Model Prediction**: The app sends the input data to a deployed API, which uses the K-means clustering model to predict the optimal laptop cluster.
3. **Results Displayed**: The recommended laptops from the corresponding cluster are displayed in a data table.
