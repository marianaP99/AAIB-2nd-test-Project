import streamlit as st
import pandas as pd

""" 
# hang in there :') 
"""
import pandas as pd
import numpy as np

test = pd.read_csv("sonograme2.csv", names = ['Tempo','Onda'])

chart_data =test

st.line_chart(chart_data)
