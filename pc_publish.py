import paho.mqtt.client as mqtt
import sounddevice as sd
import pandas as pd
import matplotlib.pyplot as plt
import json

print('Recording...')

duration = 3 # seconds
audio = sd.rec(int(duration * 44100), samplerate=44100, channels=1, blocking = True)
sd.wait()
# t = [str(n/44100) for n in range(duration*fs)]
# sonogram = [str(audio[n][0]) for n in range(duration*44100)]
message = json.dumps(audio.tolist())

def on_publish(client, userdata, mid):
    print('Sending Audio')

client = mqtt.Client()
client.connect("broker.hivemq.com", 1883)
client.on_publish = on_publish
client.publish("AAIB/MP",message)

