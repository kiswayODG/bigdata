# Airbnb Amenity Detection Project

This project implements a machine learning model for detecting amenities in Airbnb listings. The model is designed to help users identify the presence of various amenities based on listing descriptions and other relevant features.

## Project Structure

```
airbnb-amenity-detection
├── app.py                     # Main Streamlit application
├── models                     # Directory containing the trained model
│   └── amenity_detection_model.pkl  # Trained model for amenity detection
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/airbnb-amenity-detection.git
   cd airbnb-amenity-detection
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage Guidelines

1. **Run the Streamlit application:**
   ```bash
   streamlit run app.py
   ```

2. **Access the application:**
   Open your web browser and go to `http://localhost:8501` to interact with the application.

## Model Overview

The amenity detection model is trained to identify various amenities based on input data. It utilizes machine learning techniques to analyze the features of Airbnb listings and predict the presence of amenities such as Wi-Fi, parking, pool, etc.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.