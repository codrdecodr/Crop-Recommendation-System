
# Crop Recommendation System
This project predicts the best crop to grow based on soil conditions using a machine learning model.

## Installation & Setup

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/YOUR_USERNAME/Crop-Recommendation-System.git
   cd Crop-Recommendation-System
   ```
2. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the App**  
   ```bash
   streamlit run app.py
   ```
   The app will open in your browser at `http://localhost:8501/`.


## Deployment on Streamlit Cloud

1. Push your code to GitHub.  
2. Go to [Streamlit Cloud](https://share.streamlit.io/).  
3. Connect your repository and deploy.

## Train the Model (Optional)

If you want to retrain the model:  
```bash
python train_model.py
```

## Project Files
- `app.py` - Streamlit app  
- `train_model.py` - Script to train and save ML model  
- `crop_recommendation_model.pkl` - Saved model  
- `Crop-recommendation.csv` - Dataset  
- `requirements.txt` - Dependencies  

