import streamlit as st
import pandas as pd
import numpy as np
import time
import paho.mqtt.client as mqtt
import json

@st.cache
def on_connect(client, userdata, flags, rc):
    print("Connected")


def on_publish(client, userdata, mid):
    st.write('waiting for orter to start')   
   
client = mqtt.Client()
client.on_connect = on_connect
client.on_publish = on_publish

client.connect("broker.hivemq.com", 1883)

def mqtt_pub(ready):
    client.publish("AAIB/MP", payload = ready)

st.title("Projeto Substituto 2º Teste")
button = st.button("Iniciar Aquisição", on_click = mqtt_pub("start"))

sonogram = pd.read_csv("sonogram.csv")
    
