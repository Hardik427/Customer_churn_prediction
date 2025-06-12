
# 💼 Customer Churn Prediction Web App

A Streamlit-based machine learning web app that predicts whether a bank customer will **churn** (leave the bank) or **stay**, based on their profile information. It uses a pre-trained TensorFlow/Keras model with proper data preprocessing.

---

## 📌 Features

- 🔹 Clean UI for inputting customer data.
- 🔹 Real-time prediction with probability score.
- 🔹 Handles both numerical and categorical features.
- 🔹 Uses saved encoders and scaler for consistent preprocessing.
- 🔹 Based on a trained deep learning model (`model.h5`).

---

## 🧰 Tech Stack

| Component    | Technology         |
|--------------|--------------------|
| Frontend     | Streamlit          |
| ML Framework | TensorFlow / Keras |
| Data Prep    | Scikit-learn       |
| Data Handling| Pandas, NumPy      |
| Serialization| Pickle             |

---

## 🧠 Model Inputs & Output

### 🔢 Input Features

- Credit Score
- Geography (France, Germany, Spain)
- Gender (Male, Female)
- Age
- Tenure (Years with bank)
- Balance
- Number of Products
- Has Credit Card (0 or 1)
- Is Active Member (0 or 1)
- Estimated Salary

### 🎯 Output

- Churn probability between `0` and `1`.
- If probability > 0.5 → Likely to churn  
- If probability ≤ 0.5 → Likely to stay

---

## 🚀 How to Run Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/churn-prediction-app.git
cd churn-prediction-app
```

### 2️⃣ Create Virtual Environment (Optional)

```bash
python -m venv venv
# Activate:
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3️⃣ Install Requirements

Create a `requirements.txt` (if not already provided):

```txt
streamlit
tensorflow
scikit-learn
pandas
numpy
```

Then run:

```bash
pip install -r requirements.txt
```

### 4️⃣ Add Required Files

Ensure the following files are in the root folder:

- `app.py` – main Streamlit application file
- `model.h5` – trained Keras model
- `scaler.pkl` – fitted `StandardScaler`
- `label_encoder_gender.pkl` – fitted LabelEncoder for gender
- `one_hot_encoder_geo.pkl` – fitted OneHotEncoder for geography

### 5️⃣ Run the App

```bash
streamlit run app.py
```

Now open your browser to:  
📍 `http://localhost:8501`

---

## 📁 Project Structure

```
churn-prediction-app/
│
├── app.py                      # Streamlit App
├── model.h5                    # Trained Keras model
├── scaler.pkl                  # Scikit-learn StandardScaler
├── label_encoder_gender.pkl    # LabelEncoder for Gender
├── one_hot_encoder_geo.pkl     # OneHotEncoder for Geography
├── requirements.txt            # Required packages
└── README.md                   # Project documentation
```

---

## 🧪 Sample Prediction

**Input:**
- Geography: France  
- Gender: Male  
- Age: 40  
- Credit Score: 700  
- Tenure: 3  
- Balance: 60,000  
- Products: 2  
- Has Credit Card: Yes  
- Active Member: Yes  
- Estimated Salary: 50,000

**Output:**
```
Prediction: The customer is likely to stay.
Churn Probability: 0.12
```

---

## 📸 Optional Screenshot

*(Insert screenshot of app UI here if available)*  
![Screenshot](path/to/screenshot.png)

---

## 👨‍💻 Author

- **Your Name**  
- GitHub: [@yourusername](https://github.com/yourusername)  
- Email: your.email@example.com

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 📦 To-Do / Improvements

- [ ] Add SHAP explanations for predictions.
- [ ] Dockerize the application.
- [ ] Deploy on Streamlit Cloud or Hugging Face Spaces.

---

## ⭐️ Show some love

If you found this helpful, feel free to ⭐️ the repo or fork it for future reference.
