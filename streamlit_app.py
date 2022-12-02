import streamlit as st
import pandas as pd
import pandas as pd
import numpy as np
import time
import paho.mqtt.client as mqtt
import json

ready = False

def on_connect(client, userdata, flags, rc):
    print("Connected flags"+str(flags)+"result code " +str(rc)+"client1_id ")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def on_publish():
    print('sent' + ready)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish

client.connect("broker.hivemq.com", 1883)
client.loop_start()

def mqtt_sub():
    message = client.subscribe("AAIB/MP/SOUND")

def mqtt_pub(ready):
    print(ready)
    client.publish("AAIB/MP/READY", payload = ready)

st.write("hang in there :') v99")

button = st.button('Iniciar Aquisição')
st.write(button)

if button :  
    client.publish("AAIB/MP/READY", payload = 'start')
    mqtt_pub('start')
    st.write(message)

    # my_bar = st.progress(0)
    # for percent_complete in range(100):
    #     time.sleep(0.05)
    #     my_bar.progress(percent_complete)

    try:
        sound = json.loads(message)
        sonogram = sound[0]
        features = sound[1]
        sound_df = pd.DataFrame(sonogram, columns=['Tempo','Onda'])
        st.line_chart(sound_df['Onda'], width = max(sound_df['Tempo']))
        #st.write(features)

    except:
        print(':(')
    
# sound_df = pd.read_csv("features.csv")
# st.bar_chart(sound_df)