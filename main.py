import warnings
import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt
from reset import reset_device
from config import MQTT_BROKER, MQTT_PORT, MQTT_TOPIC

# Umlčování DeprecationWarning
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Funkce pro zpracování přijaté zprávy
def on_message(client, userdata, msg):
    if msg.payload.decode() == "reset":
        reset_device()

# Inicializace MQTT klienta
client = mqtt.Client(client_id="mqtt_client", protocol=mqtt.MQTTv5)
client.on_message = on_message

# Připojení k MQTT brokeru
client.connect(MQTT_BROKER, MQTT_PORT, 60)

# Přihlášení k topicu
client.subscribe(MQTT_TOPIC)

try:
    # Start MQTT klienta v samostatném vlákně
    client.loop_start()

    while True:
        time.sleep(60)
        reset_device()

except KeyboardInterrupt:
    print("Exiting the program...")
    client.loop_stop()
