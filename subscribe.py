import streamlit as st
import pandas as pd
import numpy as np
import paho.mqtt.client as mqtt
import json

received = False

def on_connect(client, userdata, flags, rc):
    print("Connected")

def on_message(client, userdata, msg):
    print('message')
    message = str(msg.payload.decode("utf-8"))
    sonogram = json.loads(message)
    sound_df = pd.DataFrame(sonogram, columns=['Tempo','Onda'])
    sound_df.to_csv("sonogram.csv")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.hivemq.com", 1883)

while not received:
    client.loop_start() 
    client.subscribe("AAIB/MP")

