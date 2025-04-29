import streamlit as st
import pickle
import numpy as np

'''
# Load the trained model
model_path = 'models/amenity_detection_model.pkl'
with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)
    
'''

# Set up the Streamlit interface
st.title("🏠 Airbnb Amenity Detection")
st.markdown(
    """
    Welcome to the **Airbnb Amenity Detection App**!  
    Use this tool to predict the amenities available in an Airbnb listing based on its features.
    """
)

# Input section
st.markdown("### 📋 Enter Property Details")
st.write("Fill in the details below to get a prediction of the amenities:")

col1, col2 = st.columns(2)

with col1:
    num_bedrooms = st.number_input("🛏️ Number of Bedrooms", min_value=0, max_value=10, value=1)
    property_type = st.selectbox("🏢 Property Type", ["Apartment", "House", "Condo", "Villa"])

with col2:
    num_bathrooms = st.number_input("🛁 Number of Bathrooms", min_value=0, max_value=10, value=1)
    location = st.text_input("📍 Location", "Enter the location of the property")

# Prediction button
st.markdown("---")
if st.button("🔍 Predict Amenities"):
    # Prepare input data for the model
    input_data = np.array([[num_bedrooms, num_bathrooms, property_type, location]])
    
    # Make prediction
    prediction = model.predict(input_data)
    
    # Display the result
    st.markdown("### 🛠️ Predicted Amenities:")
    st.success(prediction)
else:
    st.info("Click the button above to predict amenities.")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")