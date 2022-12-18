import ssl
from paho import mqtt
import paho.mqtt.client as paho
import paho.mqtt.publish as publish
from helper import check_status, time_sleep

# create a set of 2 test messages that will be published at the same time
msgs = [{'topic': "call/", 'payload':"ok"}]
# use TLS for secure connection with HiveMQ Cloud
sslSettings = ssl.SSLContext(mqtt.client.ssl.PROTOCOL_TLS)
# put in your cluster credentials and hostname
auth = {'username': "lamtranmqtt", 'password': "Lamtran@123"}
while True:
    if (check_status() == True):
        print(check_status())