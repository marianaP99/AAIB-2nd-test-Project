import streamlit as st
import pandas as pd

""" 
# hang in there :') 
"""
import pandas as pd
import numpy as np

test = pd.read_csv("sonograme.csv", names = ['Tempo','Onda'])

st.line_chart(x=test['Tempo'],y=test['Onda'])
