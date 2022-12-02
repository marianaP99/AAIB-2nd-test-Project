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

def mqtt_ready():
    return ready

client.loop_forever()

sound = client.subscribe("AAIB/MP")
print(sound)
