import streamlit as st
import pandas as pd
import pandas as pd
import numpy as np
import time
import paho.mqtt.client as mqtt
import json

def graphs(message):
    try:
        sound = json.loads(message)
        sonogram = sound[0]
        features = sound[1]
        sound_df = pd.DataFrame(sonogram, columns=['Tempo','Onda'])
        st.line_chart(sound_df['Onda'], width = max(sound_df['Tempo']))
        #st.write(features)

    except:
        st.write("ups! something went worg :(")

def on_connect(client, userdata, flags, rc):
    print("Connected")

def on_message(client, userdata, msg):
    st.write("receiving data")
    message = msg.payload.decode("utf-8")
    client.loop_stop()

def on_publish(client, userdata, mid):
    st.write('waiting for orter to start')

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish

client.connect("broker.hivemq.com", 1883)

def mqtt_pub(ready):
    st.write(ready)
    client.publish("AAIB/MP/READY", payload = ready)

st.write("hang in there :')")

button = st.button("Iniciar Aquisição")
st.write(button)

if button :  
    mqtt_pub("start")

while button:   
    client.loop_start()
    client.subscribe("AAIB/MP/SOUND")
    print(button)

# my_bar = st.progress(0)
# for percent_complete in range(100):
#     time.sleep(0.05)
#     my_bar.progress(percent_complete)

# sound_df = pd.read_csv("features.csv")
# st.bar_chart(sound_df)