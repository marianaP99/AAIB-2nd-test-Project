import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

""" 
# Hello World!! 
"""
arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.plt.plot(fig)
