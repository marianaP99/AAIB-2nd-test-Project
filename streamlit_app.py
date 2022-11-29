import streamlit as st
import pandas as pd

""" 
# hang in there :') 
"""
import pandas as pd
import numpy as np

sound_df = pd.read_csv("sonograme.csv")

st.line_chart(sound_df['Onda'], width = max(sound_df['Tempo']))

# sound_df = pd.read_csv("sonograme.csv", names = ['Tempo','Onda'])
# st.bar_chart(chart_data)
