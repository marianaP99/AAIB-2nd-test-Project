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

client.connect("test.mosquitto.org", 1883)

def mqtt_sub():
    ready = True
    sound = client.subscribe("AAIB/MP")

def mqtt_pub():
    message = 'start'
    client.publish("AAIB/MP", message)

client.loop_start()    

st.write("hang in there :') or not :(")

start = 0
def get_button():
    return 1

button = st.button('Iniciar Aquisição')

if button : 

    mqtt_pub()
    mqtt_sub()

    my_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.05)
        my_bar.progress(percent_complete)

    try:
        sonogram, features = gp.sound.split('||')
        # sonogram = '\n'.join([','.join([str(t[n]),str(sound[n])]) for n in range(len(t))])
        sound = [[t_sound.split(',')] for t_sound in sonogram.split('\n')]
        sound_df = pd.DataFrame(dound, columns=['Tempo','Onda'])
        st.line_chart(sound_df['Onda'], width = max(sound_df['Tempo']))

    except:
        st.write('waiting for data')


# sound_df = pd.read_csv("features.csv")
# st.bar_chart(sound_df)




