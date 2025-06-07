# 🚗 Car Price Prediction App

Welcome to the **Car Price Prediction App**, a machine learning-powered web application that estimates the resale price of a used car based on its specifications. The app is built using **Python**, **Streamlit**, and **scikit-learn**, and provides a clean and interactive UI for users.

---

## 🌐 Live Demo

🔗 [Live App on Streamlit](https://your-streamlit-url.streamlit.app)  
*(Replace the link above after deployment to Streamlit Cloud)*

---

## 📁 Repository Contents

| File / Folder         | Description                                       |
|-----------------------|---------------------------------------------------|
| `Cardetails.csv`      | Cleaned dataset used for training the model       |
| `car_model.pkl`       | Pickled trained regression model                  |
| `price Predictor.ipynb` | Jupyter notebook for model training & EDA       |
| `site.py`             | Streamlit frontend app to interact with the model |
| `.ipynb_checkpoints/` | Auto-saved backup files by Jupyter                |

---

## 📊 Features

- Predicts resale price of a car based on:
  - Brand
  - Year
  - Driven kilometers
  - Fuel type
  - Seller type
  - Transmission
  - Owner history
  - Mileage
  - Engine power
  - Max power
  - Seating capacity
- Beautiful UI with background image
- CSV download for predicted results
- Real-time inference using trained model

---

## 🚀 Getting Started Locally

### 🔧 Requirements

- Python 3.7+
- Libraries:
  - `streamlit`
  - `pandas`
  - `numpy`
  - `scikit-learn`
  - `pickle`

### 🛠 Installation

Clone the repo and install dependencies:

```bash
git clone https://github.com/CARLOX62/Car-price-prediction.git
cd Car-price-prediction
pip install -r requirements.txt
```

Create `requirements.txt` with:

```
streamlit
pandas
numpy
scikit-learn
```

### ▶️ Run the App

```bash
streamlit run site.py
```

Make sure the following files are in the same directory:
- `site.py`
- `car_model.pkl`
- `Cardetails.csv`

---

## 📚 Model Training

Model training was done in `price Predictor.ipynb`, which includes:
- Data cleaning
- Feature engineering
- Label encoding
- Model training (e.g., Random Forest)
- Accuracy evaluation
- Saving model as `.pkl`

---

## 🧠 Sample Prediction Flow

1. User selects:
   - `Hyundai`, `2019`, `Petrol`, `Manual`, etc.
2. App processes input and transforms it
3. Model predicts: `₹4,75,000`
4. User downloads CSV with details

---


---

## ✨ Future Improvements

- Add authentication
- Upload new dataset via UI
- Train model interactively
- Deploy to Hugging Face or Heroku

---

## 👤 Author

**CARLOX62**  
🔗 [GitHub Profile](https://github.com/CARLOX62)

---



