import streamlit as st
import pickle
import pandas as pd

# Load model
with open('ipl_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Load encoders
with open('encoders.pkl', 'rb') as f:
    le_team, le_winner = pickle.load(f)

# Calculate team average scores from deliveries.csv
deliveries = pd.read_csv('ipldatasets/deliveries.csv')
team_avg_scores = deliveries.groupby('batting_team')['total_runs'].mean().reset_index()
team_avg_scores.columns = ['team', 'avg_score']

# UI
st.title("🏏 IPL Winning Team Predictor")

teams = list(le_team.classes_)
team1 = st.selectbox("Select Team 1", teams)
team2 = st.selectbox("Select Team 2", [t for t in teams if t != team1])

if st.button("Predict Winner"):
    # Encode teams
    team1_enc = le_team.transform([team1])[0]
    team2_enc = le_team.transform([team2])[0]

    # Get average scores
    team1_avg = team_avg_scores[team_avg_scores['team'] == team1]['avg_score'].values
    team2_avg = team_avg_scores[team_avg_scores['team'] == team2]['avg_score'].values

    if len(team1_avg) == 0 or len(team2_avg) == 0:
        st.error("One of the teams has no historical data.")
    else:
        input_df = pd.DataFrame([[team1_enc, team2_enc, team1_avg[0], team2_avg[0]]],
                                columns=['team1_enc', 'team2_enc', 'team1_avg', 'team2_avg'])

        prediction = model.predict(input_df)[0]
        winner = le_winner.inverse_transform([prediction])[0]

        st.success(f"🏆 Predicted Winner: {winner}")
