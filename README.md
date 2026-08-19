# House Price Prediction

An end-to-end Machine Learning web application that predicts house prices based on property characteristics such as location, area, furnishing, bathrooms, parking, floors, and other property features.

The project combines **Data Analysis, Data Cleaning, Machine Learning, FastAPI, and React** into a complete prediction system.

---

## 📌 Overview

The goal of this project is to build a machine learning system capable of estimating the price of a house from its property details.

The project follows a complete ML workflow:

```text
Raw Dataset
     ↓
Data Exploration (EDA)
     ↓
Data Cleaning & Transformation
     ↓
Feature Engineering
     ↓
Model Training
     ↓
Model Evaluation & Tuning
     ↓
Best Model
     ↓
FastAPI Backend
     ↓
React Frontend
     ↓
Predicted House Price
```

The final application allows the user to enter property information through a web form and receive an estimated house price.

---

# 🏗️ Architecture

```text
                    ┌──────────────────────┐
                    │      React UI        │
                    │    Frontend :5173    │
                    └──────────┬───────────┘
                               │
                               │ HTTP POST /predict
                               ↓
                    ┌──────────────────────┐
                    │      FastAPI         │
                    │    Backend :8000     │
                    └──────────┬───────────┘
                               │
                               ↓
                    ┌──────────────────────┐
                    │  ML Preprocessing    │
                    │      Pipeline        │
                    └──────────┬───────────┘
                               │
                               ↓
                    ┌──────────────────────┐
                    │ Random Forest Model  │
                    │ house_price_model    │
                    └──────────┬───────────┘
                               │
                               ↓
                    ┌──────────────────────┐
                    │ Predicted Price      │
                    │       INR / USD      │
                    └──────────────────────┘
```

---

# 🛠️ Tech Stack

### Machine Learning

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Joblib
* Jupyter Notebook

### Backend

* FastAPI
* Uvicorn
* Pydantic
* Pandas
* Scikit-learn
* Joblib

### Frontend

* React
* TypeScript
* Vite
* React Router
* CSS

### Development Tools

* Git
* GitHub
* Git LFS

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
│   ├── public/
│   │   └── locations.json
│   │
│   ├── src/
│   │   ├── api/
│   │   │   └── predictionClient.ts
│   │   │
│   │   ├── components/
│   │   │   └── PredictionForm.tsx
│   │   │
│   │   ├── pages/
│   │   │   ├── HomePage.tsx
│   │   │   ├── ResultPage.tsx
│   │   │   └── NotFoundPage.tsx
│   │   │
│   │   ├── types/
│   │   │   └── prediction.ts
│   │   │
│   │   ├── App.tsx
│   │   ├── main.tsx
│   │   └── index.css
│   │
│   ├── .env.example
│   ├── package.json
│   └── package-lock.json
│
├── notebooks/
│   ├── 01_Data_Cleaning.ipynb
│   ├── 02_EDA.ipynb
│   └── 03_Model_Training.ipynb
│
├── screenshots/
│   ├── home.png
│   ├── result.png
│   └── swagger.png
│
├── cleaned_house_prices.csv
├── .gitignore
└── README.md
```

> Notebook filenames may differ slightly depending on the final repository structure.

---

# 📊 Dataset

The project uses an Indian residential real-estate dataset containing approximately **188K property records** and 21 original columns.

The dataset contains information such as:

* Property location
* Price
* Carpet Area
* Super Area
* Property status
* Transaction type
* Furnishing
* Facing
* Bathrooms
* Balcony
* Car Parking
* Ownership
* Society
* Floor information

### Dataset Source

The dataset is available on Hugging Face:

[House Prediction Dataset](https://huggingface.co/datasets/bryium/house_prediction?utm_source=chatgpt.com)

The dataset corresponds to the original 187,531-row / 21-column structure used in this project.

### Download Dataset

You can download the dataset from the dataset page above.

For local development, place the downloaded CSV in the project root:

```text
House-Price-Prediction/
└── house_prices.csv
```

The raw dataset is intentionally **not committed to GitHub** because of its large file size.

The processed dataset used for analysis is provided separately as:

```text
cleaned_house_prices.csv
```

---

# 🧹 Data Preprocessing

The original dataset contains mixed formats, missing values, categorical features, and inconsistent area representations.

The preprocessing pipeline includes:

1. Handling missing values.
2. Converting property prices into numeric INR values.
3. Converting area measurements into square feet.
4. Extracting current floor and total floors.
5. Converting car parking information into a numeric feature.
6. Creating binary property features.
7. Encoding categorical variables.
8. Handling location information.
9. Creating `Society_Frequency`.
10. Removing invalid/extreme records where appropriate.

### Engineered Features

The final model uses features including:

```text
location
Status
Transaction
Furnishing
facing
Ownership
Bathroom
Balcony
Carpet_Area_sqft
Super_Area_sqft
Car_Parking_Count
Current_Floor
Total_Floors
Has_Main_Road
Has_Garden_Park
Has_Pool
Society_Frequency
```

---

# 🤖 Machine Learning Model

The final selected model is:

**Random Forest Regressor**

The model is used as a regression model because the target variable is a continuous house price.

The complete preprocessing and model are stored together inside a Scikit-learn Pipeline and exported using Joblib.

```text
house_price_model.pkl
```

This allows the FastAPI backend to directly load the complete trained pipeline and make predictions on new property data.

---

# 📈 Model Performance

The selected Random Forest model achieved the following results on the test set:

| Metric |         Result |
| ------ | -------------: |
| MAE    |   ~898,791 INR |
| RMSE   | ~2,963,331 INR |
| R²     |        ~0.9366 |

### Metric Interpretation

**MAE — Mean Absolute Error**

The average absolute difference between the actual and predicted prices is approximately:

```text
898,791 INR
```

**RMSE — Root Mean Squared Error**

RMSE gives more weight to larger prediction errors:

```text
2,963,331 INR
```

**R² — R-squared**

The model achieved:

```text
0.9366
```

which indicates that the model explains approximately **93.66% of the variance** in the target variable on the test set.

---

# ⚙️ Backend Setup

## 1. Clone the Repository

```bash
git clone https://github.com/Mohamdeita/House-Price-Prediction.git
cd House-Price-Prediction
```

> If the repository owner/name changes, use the repository's current GitHub clone URL.

## 2. Create a Virtual Environment

Windows:

```powershell
python -m venv venv
```

Activate it:

```powershell
venv\Scripts\activate
```

## 3. Install Backend Dependencies

```powershell
cd backend
pip install -r requirements.txt
```

## 4. Run FastAPI

```powershell
python -m uvicorn main:app --reload --port 8000
```

The backend will be available at:

```text
http://127.0.0.1:8000
```

Swagger API documentation:

```text
http://127.0.0.1:8000/docs
```

---

# 🌐 Frontend Setup

Open another terminal.

From the project root:

```powershell
cd frontend
```

Install dependencies:

```powershell
npm install
```

Create a `.env` file:

```env
VITE_API_BASE_URL=http://localhost:8000
```

Then start the development server:

```powershell
npm run dev
```

The frontend will normally be available at:

```text
http://localhost:5173
```

Open that address in your browser.

---

# 🔐 Environment Variables

## Backend

The backend currently does not require any secret environment variables.

| Variable | Required | Description                      |
| -------- | -------- | -------------------------------- |
| —        | No       | Backend uses local configuration |

## Frontend

| Variable            | Required | Example                 | Description         |
| ------------------- | -------- | ----------------------- | ------------------- |
| `VITE_API_BASE_URL` | Yes      | `http://localhost:8000` | FastAPI backend URL |

Example:

```env
VITE_API_BASE_URL=http://localhost:8000
```

---

# 🔌 API Reference

## GET `/`

Checks whether the API is running.

### Example Response

```json
{
  "message": "House Price Prediction API is running"
}
```

---

## POST `/predict`

Predicts the price of a house from its property information.

### Request Body

```json
{
  "location": "bangalore",
  "Status": "Ready to Move",
  "Transaction": "Resale",
  "Furnishing": "Semi-Furnished",
  "facing": "East",
  "Ownership": "Freehold",
  "Bathroom": 2,
  "Balcony": 1,
  "Carpet_Area_sqft": 1100,
  "Super_Area_sqft": 1300,
  "Car_Parking_Count": 1,
  "Current_Floor": 2,
  "Total_Floors": 5,
  "Has_Main_Road": 1,
  "Has_Garden_Park": 0,
  "Has_Pool": 0,
  "Society_Frequency": 100
}
```

### Example Response

```json
{
  "predicted_price": 6921825.79
}
```

The prediction is returned in **Indian Rupees (INR)**.

---

# 🧪 cURL Example

With the FastAPI server running:

```bash
curl -X POST "http://127.0.0.1:8000/predict" ^
  -H "Content-Type: application/json" ^
  -d "{\"location\":\"bangalore\",\"Status\":\"Ready to Move\",\"Transaction\":\"Resale\",\"Furnishing\":\"Semi-Furnished\",\"facing\":\"East\",\"Ownership\":\"Freehold\",\"Bathroom\":2,\"Balcony\":1,\"Carpet_Area_sqft\":1100,\"Super_Area_sqft\":1300,\"Car_Parking_Count\":1,\"Current_Floor\":2,\"Total_Floors\":5,\"Has_Main_Road\":1,\"Has_Garden_Park\":0,\"Has_Pool\":0,\"Society_Frequency\":100}"
```

Expected response format:

```json
{
  "predicted_price": 6921825.79
}
```

---

# 🖥️ Screenshots

## Home Page

The React frontend provides a form where users enter property details.

![Home Page](screenshots/home.png)

---

## Prediction Result

After submitting the form, the application displays the predicted house price.

![Prediction Result](screenshots/result.png)

---

## FastAPI Swagger Documentation

The backend provides interactive API documentation through FastAPI Swagger UI.

![Swagger API](screenshots/swagger.png)

---

# 🔄 End-to-End Workflow

The complete application works as follows:

```text
User
  ↓
React Form
  ↓
POST /predict
  ↓
FastAPI
  ↓
Pydantic Validation
  ↓
Pandas DataFrame
  ↓
Preprocessing Pipeline
  ↓
Random Forest Regressor
  ↓
Predicted Price
  ↓
FastAPI JSON Response
  ↓
React Result Page
```

---

# ▶️ Run the Complete Project

You need two terminals.

### Terminal 1 — Backend

```powershell
cd House-Price-Prediction\backend
venv\Scripts\activate
python -m uvicorn main:app --reload --port 8000
```

### Terminal 2 — Frontend

```powershell
cd House-Price-Prediction\frontend
npm install
npm run dev
```

Then open:

```text
http://localhost:5173
```

Enter the property information and click the prediction button.

The application sends the data to FastAPI, the trained model generates a prediction, and the result is displayed on the result page.

---

# 🧪 Reproducing the Machine Learning Workflow

The notebooks contain the main machine learning workflow:

```text
Load Dataset
     ↓
Data Inspection
     ↓
EDA
     ↓
Data Cleaning
     ↓
Feature Engineering
     ↓
Train/Test Split
     ↓
Preprocessing
     ↓
Model Training
     ↓
Model Evaluation
     ↓
Hyperparameter Tuning
     ↓
Final Model
     ↓
Model Export
```

The exported model is:

```text
backend/house_price_model.pkl
```

---

# 📌 Important Notes

* The raw dataset is not stored in the repository because of its large size.
* The trained model is stored using **Git LFS** because of its large file size.
* The model predicts prices in Indian Rupees.
* The frontend converts the displayed prediction to USD for presentation purposes.
* The exchange rate used by the frontend is for display only and does not affect model predictions.
* The trained model and preprocessing pipeline must remain compatible with the versions used to train them.

---

# 👨‍💻 Author

**Mohamed Eita**

Machine Learning / AI Project

[LinkedIn](https://www.linkedin.com/in/mohamed-eita-581187371)

---

# 📄 License

This project is intended for educational and portfolio purposes.
