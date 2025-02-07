import time
import logging
import schedule
import warnings
import paho.mqtt.client as mqtt
from reset import reset_relay, reset_device, reset_all
from config import RESET_TIME, MQTT_ACTIVE, MQTT_BROKER, MQTT_PORT, MQTT_TOPIC, MQTT_USERNAME, MQTT_PASSWORD

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s', 
    handlers=[
        logging.FileHandler('/var/log/Relay-Reset.log'),
        logging.StreamHandler()
    ]
)

# Umlčování DeprecationWarning
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Schedule to run every day at RESET_TIME
schedule.every().day.at(RESET_TIME).do(reset_relay)

# Function to process the received message
def on_message(client, userdata, msg):
    payload = msg.payload.decode()

    if payload == "reset-relay":
        reset_relay()
    elif payload == "reset-device":
        reset_device()
    elif payload == "reset-all":
        reset_all()
    else:
        logging.error(f"Unknown command: {payload}")

# Initialize the MQTT client only if MQTT is active
if MQTT_ACTIVE:
    client = mqtt.Client(client_id="mqtt_client", protocol=mqtt.MQTTv5)

    # Add authentication (if needed)
    if MQTT_USERNAME and MQTT_PASSWORD:
        client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)

    client.on_message = on_message

    # Connection to the MQTT broker with retries on failure
    while True:
        try:
            client.connect(MQTT_BROKER, MQTT_PORT, 60)
            client.subscribe(MQTT_TOPIC)
            break  
        except Exception as e:
            logging.error(f"Error connecting to MQTT broker: {e}")
            time.sleep(5)

try:
    if MQTT_ACTIVE:
        client.loop_start()

    while True:
        schedule.run_pending()
        time.sleep(10)

except KeyboardInterrupt:
    print("Exiting the program...")

finally:
    if MQTT_ACTIVE:
        client.loop_stop()
