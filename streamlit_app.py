import streamlit as st
import pandas as pd
import pandas as pd
import numpy as np
import time
import paho.mqtt.client as mqtt

ready = False

def on_connect(client, userdata, flags, rc):
     print("Connected flags"+str(flags)+"result code " +str(rc)+"client1_id ")

def on_message(client, userdata, msg):
     print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.hivemq.com", 1883)

def mqtt_sub():
    message = client.subscribe("AAIB/MP")

def mqtt_pub():
    message = 'start'
    print(message)
    client.publish("AAIB/MP", message)

st.write("hang in there :') v1")

button = st.button('Iniciar Aquisição')

if button : 
    client.loop_start() 
    mqtt_pub()
    mqtt_sub()
    client.loop_stop()

    my_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.05)
        my_bar.progress(percent_complete)

    st.write(sonogram)
    try:
        sonogram, features = message.split('||')
        # sonogram = '\n'.join([','.join([str(t[n]),str(sound[n])]) for n in range(len(t))])
        sound = [[t_sound.split(',')] for t_sound in sonogram.split('\n')]
        sound_df = pd.DataFrame(dound, columns=['Tempo','Onda'])
        st.line_chart(sound_df['Onda'], width = max(sound_df['Tempo']))
    except:
        print(':(')
# sound_df = pd.read_csv("features.csv")
# st.bar_chart(sound_df)