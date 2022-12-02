import paho.mqtt.client as mqtt

message = " "

def on_connect(client, userdata, flags, rc):
    print("Connected")

def on_message(client, userdata, msg):
    message = str(msg.payload.decode("utf-8"))
    print(msg.topic+" "+ message)
    print('Message Received')
    
    if message == "start":
        exec(open("pc_publish.py").read())

client = mqtt.Client()
client.on_message = on_message
client.connect("broker.hivemq.com", 1883)

while message != "start":
    client.loop_start()
    client.subscribe("AAIB/MP")
client.loop_stop()
