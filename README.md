# 🏠 House Price Prediction

An end-to-end Machine Learning web application that predicts house prices based on property features.

The project combines a trained Machine Learning regression model with a **FastAPI backend** and a **React + TypeScript + Vite frontend** to provide an interactive house price prediction experience.

---

## 🚀 Live Demo

### Frontend

Run the frontend locally and open the URL provided by Vite, usually:

```text
http://localhost:5173
```

### Backend API

The backend is deployed on Railway:

https://house-price-prediction-production-83d3.up.railway.app

### API Documentation

FastAPI provides interactive API documentation:

https://house-price-prediction-production-83d3.up.railway.app/docs

---

## 📌 Project Overview

The goal of this project is to build a complete Machine Learning application capable of predicting house prices from property information.

The application follows this workflow:

```text
User
  ↓
React Frontend
  ↓
FastAPI REST API
  ↓
Data Processing
  ↓
Trained ML Model
  ↓
Predicted House Price
  ↓
Frontend Result
```

---

## ✨ Features

* 🏠 House price prediction
* 📊 Machine Learning regression model
* ⚛️ React + TypeScript frontend
* ⚡ Vite development environment
* 🐍 FastAPI backend
* 🔌 REST API integration
* 🤖 Trained `.pkl` Machine Learning model
* ☁️ Backend deployment using Railway
* 📖 Interactive Swagger API documentation
* 🔄 Frontend connected to the deployed backend

---

## 🛠️ Tech Stack

### Machine Learning

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib

### Backend

* FastAPI
* Uvicorn
* Python

### Frontend

* React
* TypeScript
* Vite

### Deployment

* GitHub
* Railway

---

# 📂 Project Structure

```text
House-Price-Prediction/
│
├── backend/
│   ├── main.py
│   ├── house_price_model.pkl
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── api/
│   │   │   └── predictionClient.ts
│   │   ├── components/
│   │   └── ...
│   │
│   ├── public/
│   ├── .env
│   ├── package.json
│   ├── package-lock.json
│   └── vite.config.ts
│
├── .gitignore
└── README.md
```

---

# ⚙️ Installation & Setup

There are two ways to run the project.

## Option 1 — Run the Frontend with the Online Backend

This is the easiest way to test the project.

### 1. Clone the repository

```bash
git clone https://github.com/Mohamedeita/House-Price-Prediction.git
```

Move into the project:

```bash
cd House-Price-Prediction
```

### 2. Open the frontend folder

```bash
cd frontend
```

### 3. Install dependencies

```bash
npm install
```

### 4. Configure the API URL

Create a `.env` file inside the `frontend` folder:

```env
VITE_API_BASE_URL=https://house-price-prediction-production-83d3.up.railway.app
```

### 5. Start the frontend

```bash
npm run dev
```

Vite will provide a local URL, usually:

```text
http://localhost:5173
```

Open the URL in your browser.

The frontend will communicate with the deployed Railway backend automatically.

---

# 🐍 Option 2 — Run the Backend Locally

If you want to run the complete application locally, you can also run the FastAPI backend.

### 1. Open a terminal

From the project root:

```bash
cd backend
```

### 2. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 3. Start FastAPI

```bash
uvicorn main:app --reload
```

The backend will normally run at:

```text
http://127.0.0.1:8000
```

### 4. Open the API documentation

Visit:

```text
http://127.0.0.1:8000/docs
```

You can use Swagger UI to test the API endpoints.

---

# 🔐 Environment Variables

The frontend uses an environment variable to determine which backend API it should communicate with.

Create:

```text
frontend/.env
```

and add:

```env
VITE_API_BASE_URL=https://house-price-prediction-production-83d3.up.railway.app
```

### Local Backend

If you want the frontend to communicate with your own local backend instead, change it to:

```env
VITE_API_BASE_URL=http://127.0.0.1:8000
```

After changing `.env`, restart the Vite development server.

---

# 🤖 Machine Learning Model

The application uses a trained regression model stored in:

```text
backend/house_price_model.pkl
```

The backend loads the trained model using Joblib and uses the submitted property features to generate a price prediction.

The prediction pipeline is:

```text
Input Features
      ↓
Preprocessing
      ↓
Feature Transformation
      ↓
Trained Regression Model
      ↓
Predicted Price
```

---

# 🔌 API

The backend is implemented using FastAPI.

### Production API

```text
https://house-price-prediction-production-83d3.up.railway.app
```

### Interactive Documentation

```text
https://house-price-prediction-production-83d3.up.railway.app/docs
```

Swagger UI can be used to inspect and test the available API endpoints.

---

# 🌐 Deployment

The backend is deployed using **Railway**.

Deployment architecture:

```text
GitHub Repository
       ↓
Railway
       ↓
FastAPI Backend
       ↓
Machine Learning Model
```

The frontend can communicate with the deployed API through:

```text
https://house-price-prediction-production-83d3.up.railway.app
```

---

# 🧪 Testing the Application

To test the application:

1. Start the frontend.
2. Open the Vite URL.
3. Enter the required house information.
4. Click **Predict**.
5. The frontend sends the data to the FastAPI backend.
6. The backend processes the input.
7. The trained model generates the prediction.
8. The predicted house price is displayed in the frontend.

---

# 📸 Demo

The application provides an interactive interface where users can enter property information and receive a predicted house price.

### Application Flow

```text
Enter Property Details
        ↓
      Predict
        ↓
API Request
        ↓
Machine Learning Model
        ↓
Predicted House Price
```

---

# 📈 Future Improvements

Possible future improvements include:

* Improve model accuracy through additional feature engineering.
* Experiment with different regression algorithms.
* Add model performance metrics to the frontend.
* Add prediction history.
* Add data visualization.
* Add authentication.
* Deploy the frontend publicly.
* Add automated testing.
* Add CI/CD deployment.

---

# 🎯 Learning Objectives

This project demonstrates practical experience with:

* Data preprocessing
* Feature engineering
* Regression
* Machine Learning model training
* Model serialization
* REST APIs
* FastAPI
* React
* TypeScript
* Environment variables
* API integration
* Git/GitHub
* Cloud deployment

---

# 👨‍💻 Author

**Mohamed Eita**

GitHub:

https://github.com/Mohamedeita

---

# ⭐ Support

If you find this project useful, feel free to ⭐ the repository.
