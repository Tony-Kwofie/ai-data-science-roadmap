import streamlit as st
from sklearn.linear_model import LinearRegression

# Training data
X = [[1, 1], [2, 2], [3, 2], [4, 3], [5, 4]]
y = [120, 240, 300, 420, 520]

# Train model
model = LinearRegression()
model.fit(X, y)

# Streamlit UI
st.title("Airbnb Price Predictor")
nights = st.slider("Number of nights", 1, 10, 3)
guests = st.slider("Number of guests", 1, 10, 2)

# Predict price
prediction = model.predict([[nights, guests]])
st.success(f"Predicted price: ${prediction[0]:.2f}")
