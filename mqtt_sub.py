import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
     logging.info("Connected flags"+str(flags)+"result code "\
     +str(rc)+"client1_id ")
     client.connected_flag=True
      
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("test.mosquitto.org", 1883, 60)
client.loop_forever()
