# from paho.mqtt import client as mqtt   
# import ssl
# ########## You need only modify this section start ##########
# # You can generate the SAS with Device Explorer
# # Example SharedAccessSignature = "SharedAccessSignature sr=kevinsay.azure-devices.net%2fdevices%2fmygreatdevice&sig=ON2EYJR1hUC84rJSMe%2fCrBdb8lcIr7A%3d&se=15055292"
# SharedAccessSignature = "SharedAccessSignature sr=EdgeClientIOTHub.azure-devices.net%2Fdevices%2Fc4fa4ead-f0dc-46c2-9db3-7963267c9d98&sig=1xJ4cXYhPtRJiRNOAJrNdeX7p%2Fcd0r6v67Vt%2BZ0sNkQ%3D&se=1502015637"
# # download the cer from https://ssl-tools.net/certificates/d4de20d05e66fc53fe1a50882c78db2852cae474.pem
# BaltimoreCyberTrustRootCER = "baltimorebase64.cer"
# ########### You need only modify this section end ###########
# HubName = "EdgeClientIOTHub.azure-devices.net"       # extracting the Hub name from the SAS
# devicename = "c4fa4ead-f0dc-46c2-9db3-7963267c9d98"    # extracting the device name from the SAS
# def on_connect(client, userdata, flags, rc):
#     print ("Connected with result code: " + str(rc))
#     client.subscribe("devices/" + devicename + "/messages/devicebound/#")
#     client.publish("devices/" + devicename + "/messages/events/", "{deviceID=c4fa4ead-f0dc-46c2-9db3-7963267c9d98,temperature=10.2}", qos=0) 
# def on_disconnect(client, userdata, rc):
#     print ("Disconnected with result code: " + str(rc))
# def on_message(client, userdata, msg):
#     print (msg.topic+" "+str(msg.payload))
#     # Do this only if you want to send a reply message every time you receive one
#     client.publish("devices/" + devicename + "/messages/events/", "{deviceID=c4fa4ead-f0dc-46c2-9db3-7963267c9d98,temperature=10.2}", qos=0) 
# def on_publish(client, userdata, mid):
#     print ("Sent message")
# client = mqtt.Client(client_id=devicename, protocol=mqtt.MQTTv311)
# client.on_connect = on_connect
# client.on_disconnect = on_disconnect
# client.on_message = on_message
# client.on_publish = on_publish
# client.username_pw_set(username=HubName + "/" + devicename, password=SharedAccessSignature)
# client.tls_set(ca_certs=BaltimoreCyberTrustRootCER, certfile=None, keyfile=None, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1, ciphers=None)
# client.tls_insecure_set(False)
# client.connect(HubName, port=8883)



import threading
import paho.mqtt.client as mqtt

def publish_1(client,topic):
    message="{send_value : true}"
    print("publish data")
    client.publish(topic,message)
    publish_1(client,topic)


broker="131.163.162.182"
topic_pub='send_data_rasp1'
topic_sub='$SYS/#'

def on_connect(client, userdata, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(topic_sub)


def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, 1883, 60)
thread1=threading.Thread(target=publish_1,args=(client,topic_pub))
thread1.start()

client.loop_forever()