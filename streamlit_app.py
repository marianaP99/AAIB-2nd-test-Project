import streamlit as st
import pandas as pd
import pandas as pd
import numpy as np
import time

st.write("hang in there :') or not :(")

button = st.button('Iniciar Aquisição')

if button :  
    my_bar = st.progress(0)
    t0 = time.time()
    while time.time()-t0 < 3:
        my_bar.progress((time.time()-t0)/3)

sound_df = pd.read_csv("sonograme.csv", names = ['Tempo','Onda'])

st.line_chart(sound_df['Onda'], width = max(sound_df['Tempo']))

# sound_df = pd.read_csv("features.csv")
# st.bar_chart(sound_df)




