import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected")

def on_message(client, userdata, msg):
    print(msg.payload)

def on_publish(client, userdata, mid):
    print('sent' + 'ready')

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish

client.connect("broker.hivemq.com", 1883)

client.loop_forever()
client.publish("AAIB/MP/READY", payload = 'start')
