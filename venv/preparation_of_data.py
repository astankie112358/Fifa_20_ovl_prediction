import pandas as pd
import os
def get_data():
    data=pd.read_csv(os.path.join(os.path.dirname(__file__), "fut_bin20_players.csv"))
    return data
def get_pl_from_position(position:str):
    data=get_data()
    data=data[data['position']==position].reset_index()
    return data

def get_only_ovr(players:pd.DataFrame):
    ovr=players.iloc[:,7]
    return ovr

def getbasic_stats(players:pd.DataFrame):
    ovr = players.iloc[:, 18:53]
    return ovr
