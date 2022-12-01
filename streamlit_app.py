import streamlit as st
import pandas as pd
import pandas as pd
import numpy as np
import time
import gitpod_mqtt as gp

st.write("hang in there :') or not :(")

button = st.button('Iniciar Aquisição')
ready = gp.ready

if button :  
    my_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.05)
        my_bar.progress(percent_complete)

if ready:
    [sonogram, features] = gp.sound.split('||')
    # sonogram = '\n'.join([','.join([str(t[n]),str(sound[n])]) for n in range(len(t))])
    sound = [[t_sound.split(',')] for t_sound in sonogram.split('\n')]
    sound_df = pd.DataFrame(dound, columns=['Tempo','Onda'])
    st.line_chart(sound_df['Onda'], width = max(sound_df['Tempo']))

# sound_df = pd.read_csv("features.csv")
# st.bar_chart(sound_df)




