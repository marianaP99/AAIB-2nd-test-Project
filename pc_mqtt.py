import paho.mqtt.client as mqtt
import recordsound as rs

def on_connect(client, userdata, flags, rc):
     logging.info("Connected flags"+str(flags)+"result code "\
     +str(rc)+"client1_id ")
     client.connected_flag=True

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("test.mosquitto.org", 1883, 600)

client.loop_forever()

def mqtt_pub():
    message = rs.record
    client.publish("AAIB/test", message)

button = mqtt_sub()

if button:
    mqtt_pub()