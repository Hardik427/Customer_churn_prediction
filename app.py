import streamlit as st
import tensorflow
from tensorflow.keras.models import load_model
import pickle
import numpy as np
import pandas as pdc

model = load_model('model.h5')

##load encoder and scaler
with open('one_hot_encoder_geo.pkl', 'rb') as f:
    label_encoder_geo = pickle.load(f)
    
with open('label_encoder_gender.pkl', 'rb') as f:
    label_encoder_gender = pickle.load(f)
    
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)
    
    
st.title('Churn Prediction App')
st.write('This app predicts whether a customer will churn based on their profile.')
st.write('Please enter the customer details below:')
# Input fields for customer details
credit_score = st.number_input('Credit Score', min_value=300, max_value=850, value=700)
geography = st.selectbox('Geography', label_encoder_geo.categories_[0].tolist())
gender = st.selectbox('Gender', label_encoder_gender.classes_.tolist())
age = st.slider('Age', min_value=18, max_value=100, value=40)
tenure = st.slider('Tenure (Years)', min_value=0, max_value=10, value=3)
balance = st.number_input('Balance', min_value=0, value=60000)
num_of_products = st.slider('Number of Products', min_value=1, max_value=4, value=2)
has_cr_card = st.selectbox('Has Credit Card', [0,1])
is_active_member = st.selectbox('Is Active Member', [0, 1])
estimated_salary = st.number_input('Estimated Salary', min_value=0, value=50000)

input_data = {
    'CreditScore': credit_score,
    'Geography': geography,
    'Gender' : label_encoder_gender.transform([gender])[0],
    'Age': age,
    'Tenure': tenure,
    'Balance': balance,
    'NumOfProducts': num_of_products,
    'HasCrCard': has_cr_card,
    'IsActiveMember': is_active_member,
    'EstimatedSalary': estimated_salary
}
input_data = pd.DataFrame([input_data])

geo_encoder = label_encoder_geo.transform([input_data['Geography']]).toarray()
encoded_geo = pd.DataFrame(geo_encoder, columns=label_encoder_geo.get_feature_names_out(['Geography']))
input_data.drop(columns=['Geography'], inplace=True)
input_data = pd.concat([input_data, encoded_geo], axis=1)

input_data = scaler.transform(input_data)
predicted_value = model.predict(input_data)
st.write('### Prediction Result')
if predicted_value[0][0] > 0.5:
    st.write('The customer is likely to churn.')
else:
    st.write('The customer is likely to stay.')
st.write('Predicted Churn Probability:', predicted_value[0][0])

