import streamlit as st
import numpy as np
import requests


st.title('Expected Points Added by Offensive Playcall')

st.title('Game Situation')

quarter = st.selectbox("Quarter", [1,2,3,4])
down = st.selectbox("Down", [1,2,3,4])
yardsToGo = st.slider("Yards to Go for 1st Down", 1, 30)
total_yardsToGo = st.slider("Yards to Go for TD", 0, 100)

off_team_sel = st.selectbox("Offensive Team", ['off_ARI', 'off_ATL', 'off_BAL',
       'off_BUF', 'off_CAR', 'off_CHI', 'off_CIN', 'off_CLE', 'off_DAL',
       'off_DEN', 'off_DET', 'off_GB', 'off_HOU', 'off_IND', 'off_JAX',
       'off_KC', 'off_LA', 'off_LAC', 'off_LV', 'off_MIA', 'off_MIN', 'off_NE',
       'off_NO', 'off_NYG', 'off_NYJ', 'off_PHI', 'off_PIT', 'off_SEA',
       'off_SF', 'off_TB', 'off_TEN', 'off_WAS'] )

ind = ['off_ARI', 'off_ATL', 'off_BAL',
       'off_BUF', 'off_CAR', 'off_CHI', 'off_CIN', 'off_CLE', 'off_DAL',
       'off_DEN', 'off_DET', 'off_GB', 'off_HOU', 'off_IND', 'off_JAX',
       'off_KC', 'off_LA', 'off_LAC', 'off_LV', 'off_MIA', 'off_MIN', 'off_NE',
       'off_NO', 'off_NYG', 'off_NYJ', 'off_PHI', 'off_PIT', 'off_SEA',
       'off_SF', 'off_TB', 'off_TEN', 'off_WAS'].index(off_team_sel)

off_team = np.zeros(32)
off_team[ind] = 1

def_team_sel = st.selectbox("Defensive Team", ['def_ARI', 'def_ATL',
       'def_BAL', 'def_BUF', 'def_CAR', 'def_CHI', 'def_CIN', 'def_CLE',
       'def_DAL', 'def_DEN', 'def_DET', 'def_GB', 'def_HOU', 'def_IND',
       'def_JAX', 'def_KC', 'def_LA', 'def_LAC', 'def_LV', 'def_MIA',
       'def_MIN', 'def_NE', 'def_NO', 'def_NYG', 'def_NYJ', 'def_PHI',
       'def_PIT', 'def_SEA', 'def_SF', 'def_TB', 'def_TEN', 'def_WAS'])

ind = ['def_ARI', 'def_ATL',
       'def_BAL', 'def_BUF', 'def_CAR', 'def_CHI', 'def_CIN', 'def_CLE',
       'def_DAL', 'def_DEN', 'def_DET', 'def_GB', 'def_HOU', 'def_IND',
       'def_JAX', 'def_KC', 'def_LA', 'def_LAC', 'def_LV', 'def_MIA',
       'def_MIN', 'def_NE', 'def_NO', 'def_NYG', 'def_NYJ', 'def_PHI',
       'def_PIT', 'def_SEA', 'def_SF', 'def_TB', 'def_TEN', 'def_WAS'].index(def_team_sel)

def_team = np.zeros(32)
def_team[ind] = 1

st.title('Play Call')

play_type = st.radio("Play Type", ['Run', 'Pass'])
if play_type == 'Run':
    run = 1
    passLength = 0
else:
    run = 0
    passLength = st.slider("Pass Length (Air Yards)", 0, 50)


formation_sel = st.selectbox("Offense Formation", ['I_FORM', 'JUMBO', 'PISTOL', 'SHOTGUN', 'SINGLEBACK',
       'WILDCAT'])

ind = ['I_FORM', 'JUMBO', 'PISTOL', 'SHOTGUN', 'SINGLEBACK','WILDCAT'].index(formation_sel)

formation = np.zeros(6)
formation[ind] = 1

defendersInTheBox = st.slider("Defenders in the box", 2, 10)

query_params = str(quarter) + ',' + str(down) + ',' + str(yardsToGo) + ',' + str(passLength) + ',' + \
str(defendersInTheBox) + ',' + str(run) + ',' + str(list(formation)) + ',' + str(total_yardsToGo) + ',' + \
str(list(off_team)) + ',' +  str(list(def_team) )

query_params = query_params.replace('[','').replace(']','')

#st.text(query_params)
url = f'https://e5183fpdfb.execute-api.us-east-1.amazonaws.com/default/434-final?data={query_params}'
#st.text(url)

if st.button("Get Prediction"):
    response = requests.get(url)
    epa = float(response.text)
    if epa > 0:
        st.title(f"Expected Points Added: :green[{epa}]")
    else:
        st.title(f"Expected Points Added: :red[{epa}]")
    
    


