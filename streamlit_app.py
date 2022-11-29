import streamlit as st
import pandas as pd

""" 
# hang in there :') 
"""
import pandas as pd
import numpy as np

df = pd.read_csv("sonograme.csv", names = ['Tempo','Onda'])

st.line_chart(df['Onda'], width = max(df['Tempo']))
