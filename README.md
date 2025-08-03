# SYSTEMTRON-IPLWinningTeamPredictor-Streamlit-App
 🏏 IPL Winning Team Predictor – Streamlit Web App

This project is a complete Machine Learning pipeline with a **Streamlit web app** that predicts the winner of an IPL match based on historical data such as team performance and average scores.

## 🚀 Features
- Predicts match winner between two selected IPL teams
- Calculates average team scores from historical data
- Fully interactive **Streamlit** web interface
- Model trained using **Random Forest Classifier**

## 📁 Files Included
- `matches.csv` – Historical match data
- `deliveries.csv` – Ball-by-ball delivery data
- `teamscores.csv` – Calculated team-wise average scores
- `ipl_model.pkl` – Trained ML model (Random Forest)
- `encoders.pkl` – Label encoders for team and winner
- `app.py` – Final Streamlit web application script

## 💻 How to Run the App
1. 📦 Install required packages:
pip install pandas scikit-learn streamlit



2. ▶️ Run the Streamlit app:
streamlit run app.py


3. 🌐 Open the local server link (usually `http://localhost:8501`) to use the web app.

## 🧠 Model Details
- Algorithm: Random Forest Classifier
- Input Features:
- Team 1 (encoded)
- Team 2 (encoded)
- Team 1 average score
- Team 2 average score
- Output: Predicted Winning Team
- Model Accuracy: ~92%

## 📊 Dataset Source
- IPL dataset from Kaggle
- `matches.csv`
- `deliveries.csv`

## 👨‍💻 Author

Developed by
**Syeda Alia Samia**  
GitHub:[Syeda Alia Samia](https://github.com/your-github-username)


---

