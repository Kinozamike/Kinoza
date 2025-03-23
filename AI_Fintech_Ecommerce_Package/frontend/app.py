# AI E-Commerce Dashboard
import streamlit as st
import requests

st.title("AI-Powered E-Commerce Dashboard")

st.subheader("📈 Sales Forecasting")
current_sales = st.number_input("Enter Current Sales", min_value=0)
if st.button("Predict Sales"):
    response = requests.post("http://localhost:5000/api/sales_forecast", json={"current_sales": current_sales})
    st.write(f"📊 Predicted Sales: {response.json()['predicted_sales']}")
