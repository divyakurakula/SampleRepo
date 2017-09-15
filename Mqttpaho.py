#!/usr/bin/python

import paho.mqtt.publish as publish
import paho.mqtt.subscribe as subscribe
import paho.mqtt.client as mqtt
#import ssl

auth = {
  'username':"EdgeClientIOTHub.azure-devices.net/c4fa4ead-f0dc-46c2-9db3-7963267c9d98/api-version=2016-11-14",
  'password':"SharedAccessSignature sr=EdgeClientIOTHub.azure-devices.net%2Fdevices%2Fc4fa4ead-f0dc-46c2-9db3-7963267c9d98&sig=1xJ4cXYhPtRJiRNOAJrNdeX7p%2Fcd0r6v67Vt%2BZ0sNkQ%3D&se=1502015637"
}


tls = {
  'ca_certs':"baltimorebase64.pem",
  'tls_version':ssl.PROTOCOL_TLSv1_1
}

print("ssl version" + ssl.PROTOCOL_TLSv1_1);

publish.single("devices/c4fa4ead-f0dc-46c2-9db3-7963267c9d98/messages/events/",
  payload='{"deviceID":"c4fa4ead-f0dc-46c2-9db3-7963267c9d98","temperature":10.2}',
  hostname="EdgeClientIOTHub.azure-devices.net",
  client_id="c4fa4ead-f0dc-46c2-9db3-7963267c9d98",
  auth=auth,
  tls=tls,
  port=8883,
  protocol=mqtt.MQTTv311)
print("hello");
