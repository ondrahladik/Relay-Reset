import warnings
import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt
from config import RELAY_PIN, MQTT_BROKER, MQTT_PORT, MQTT_TOPIC

# Umlčování DeprecationWarning
warnings.filterwarnings("ignore", category=DeprecationWarning)

def reset_device():
    print("Reset device")
    # Inicializace GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RELAY_PIN, GPIO.OUT)
    GPIO.output(RELAY_PIN, GPIO.HIGH)
    time.sleep(2)
    GPIO.cleanup() 
    print("Reset complete")

# Funkce pro zpracování přijaté zprávy
def on_message(client, userdata, msg):
    if msg.payload.decode() == "reset":
        reset_device()

# Inicializace MQTT klienta pro verzi 5
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
