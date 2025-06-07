import pandas as pd
import numpy as np
import pickle as pk
import streamlit as st
import base64
import io

# === Load model and data ===
car_model = pk.load(open('car_model.pkl', 'rb'))
car = pd.read_csv('Cardetails.csv')

# === Extract car brand ===
def get_brand_name(car_name):
    return car_name.split(' ')[0].strip()

car['name'] = car['name'].apply(get_brand_name)

# === Set background image ===
def set_background(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded_string}");
            background-size: cover;
            background-position: center;
            color: #ffffff;
        }}
        h1, h2, h3, h4, h5, h6, .stSelectbox label, .stNumberInput label {{
            color: #ffffff !important;
        }}
        </style>
    """, unsafe_allow_html=True)

set_background("C:/Users/HP/Desktop/CODES/ML_Projects/Car Price Predictor/pexels-pixabay-164634.jpg")

# === Title ===
st.markdown("""
    <h1 style='text-align: center; font-size: 60px; color: #fdfdfd; 
               text-shadow: 2px 2px 4px rgba(0,0,0,0.8); 
               margin-top: -20px; margin-bottom: 40px;'>
        🚗 Car Price Prediction App
    </h1>
""", unsafe_allow_html=True)

# === Input Fields ===
col1, col2 = st.columns(2)

with col1:
    name = st.selectbox('Select Car Brand', sorted(car['name'].unique()))
    year = st.number_input('Car Manufactured Year', min_value=1994, max_value=2024, value=2020, step=1)
    km_driven = st.number_input('Kilometers Driven', min_value=11, max_value=200000, value=50000, step=100)
    fuel = st.selectbox('Fuel Type', car['fuel'].unique())
    seller_type = st.selectbox('Seller Type', car['seller_type'].unique())

with col2:
    transmission = st.selectbox('Transmission Type', car['transmission'].unique())
    owner = st.selectbox('Owner Type', car['owner'].unique())
    mileage = st.number_input('Car Mileage (km/l)', min_value=10.0, max_value=40.0, value=18.0, step=0.5)
    engine = st.number_input('Engine CC', min_value=700, max_value=5000, value=1500, step=100)
    max_power = st.number_input('Max Power (BHP)', min_value=0, max_value=200, value=70, step=5)
    seats = st.number_input('Number of Seats', min_value=5, max_value=10, value=5, step=1)

# === Predict Button ===
if st.button("🔍 Predict Price"):
    input_data = pd.DataFrame(
        [[name, year, km_driven, fuel, seller_type, transmission, owner, mileage, engine, max_power, seats]],
        columns=['name', 'year', 'km_driven', 'fuel', 'seller_type', 'transmission', 'owner',
                 'mileage', 'engine', 'max_power', 'seats']
    )

    # === Encode categorical data ===
    input_data['owner'].replace(['First Owner', 'Second Owner', 'Third Owner',
                                 'Fourth & Above Owner', 'Test Drive Car'], [1, 2, 3, 4, 5], inplace=True)
    input_data['fuel'].replace(['Diesel', 'Petrol', 'LPG', 'CNG'], [1, 2, 3, 4], inplace=True)
    input_data['seller_type'].replace(['Individual', 'Dealer', 'Trustmark Dealer'], [1, 2, 3], inplace=True)
    input_data['transmission'].replace(['Manual', 'Automatic'], [1, 2], inplace=True)
    input_data['name'].replace(
        ['Maruti', 'Skoda', 'Honda', 'Hyundai', 'Toyota', 'Ford', 'Renault', 'Mahindra', 'Tata',
         'Chevrolet', 'Datsun', 'Jeep', 'Mercedes-Benz', 'Mitsubishi', 'Audi', 'Volkswagen',
         'BMW', 'Nissan', 'Lexus', 'Jaguar', 'Land', 'MG', 'Volvo', 'Daewoo', 'Kia', 'Fiat',
         'Force', 'Ambassador', 'Ashok', 'Isuzu', 'Opel'], list(range(1, 32)), inplace=True
    )

    # === Predict ===
    predicted_price = car_model.predict(input_data)
    price_value = round(predicted_price[0], 2)

    st.success(f"💰 Estimated Car Price: ₹ {price_value:,.2f}")

    # === Show Input Summary ===
    st.markdown("### 📊 Input Summary:")
    display_data = input_data.copy()
    display_data['Predicted Price (₹)'] = price_value
    st.dataframe(display_data)

    # === Download Button ===
    csv_buffer = io.StringIO()
    display_data.to_csv(csv_buffer, index=False)
    st.download_button(
        label="📥 Download Prediction as CSV",
        data=csv_buffer.getvalue(),
        file_name='car_price_prediction.csv',
        mime='text/csv'
    )
 # type: ignore