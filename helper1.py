# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 10:30:20 2021

@author: PC
"""

import pickle
import pandas as pd
import numpy as np


# =============================================================================
# WKP_OVRL = pd.read_pickle('wkp.p')
# BP_OVRL = pd.read_pickle('bp.p')
# AST_OVRL = pd.read_pickle('ast.p')
# DFP_OVRL = pd.read_pickle('dfp.p')
# AVGP_OVRL = pd.read_pickle('avgp.p')
# =============================================================================

WKP_OVRL = pickle.load(open('wkp.p', 'rb'))
BP_OVRL = pickle.load(open('bp.p', 'rb'))
AST_OVRL = pickle.load(open('ast.p', 'rb'))
DFP_OVRL = pickle.load(open('dfp.p', 'rb'))
AVGP_OVRL = pickle.load(open('avgp.p', 'rb'))

def choice1():
    Weaker_Players = WKP_OVRL[['Player', 'FG%', '3P%', 'FT%', 'ORB', 'DRB', 'SPG', 'BPG', 'APG', 'PPG']].sample(3)
    Best_Players = BP_OVRL[['Player', 'FG%', '3P%', 'FT%', 'ORB', 'DRB', 'SPG', 'BPG', 'APG', 'PPG']].sample(2)
    Assist_Players = AST_OVRL[['Player', 'FG%', '3P%', 'FT%', 'ORB', 'DRB', 'SPG', 'BPG', 'APG', 'PPG']].sample(2)
    Defensive_Players = DFP_OVRL[['Player', 'FG%', '3P%', 'FT%', 'ORB', 'DRB', 'SPG', 'BPG', 'APG', 'PPG']].sample(2)
    Average_Players = AVGP_OVRL[['Player', 'FG%', '3P%', 'FT%', 'ORB', 'DRB', 'SPG', 'BPG', 'APG', 'PPG']].sample(2)
    
    return pd.concat([Weaker_Players,Best_Players,Assist_Players,Defensive_Players, Average_Players])

df = choice1()
print(df)
h1 = df[df['Player']== 'James Harden'].sum(axis=1)
print(h1)