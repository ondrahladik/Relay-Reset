import warnings
import RPi.GPIO as GPIO
import time
import schedule
import paho.mqtt.client as mqtt
from reset import reset_device
from config import RESET_TIME, MQTT_BROKER, MQTT_PORT, MQTT_TOPIC, MQTT_USERNAME, MQTT_PASSWORD

# Umlčování DeprecationWarning
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Naplánování spuštění každý den v RESET_TIME
schedule.every().day.at(RESET_TIME).do(reset_device)

# Funkce pro zpracování přijaté zprávy
def on_message(client, userdata, msg):
    if msg.payload.decode() == "reset":
        reset_device()

# Inicializace MQTT klienta
client = mqtt.Client(client_id="mqtt_client", protocol=mqtt.MQTTv5)

# Přidání autentifikace (pokud je potřeba)
if MQTT_USERNAME and MQTT_PASSWORD:
    client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)

client.on_message = on_message

# Připojení k MQTT brokeru
try:
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.subscribe(MQTT_TOPIC)
except Exception as e:
    print(f"Chyba při připojování k MQTT brokeru: {e}")
    exit(1)

try:
    client.loop_start()

    while True:
        schedule.run_pending()
        time.sleep(10)

except KeyboardInterrupt:
    print("Exiting the program...")

finally:
    client.loop_stop()
    GPIO.cleanup()  
