# Relay-Reset

## Install

```console
sudo git clone https://github.com/ondrahladik/Relay-Reset.git  
cd Relay-Reset
sudo cp config-SAMPLE.py config.py
```

## Config
```console
sudo nano config.py
```

```python
RELAY_PIN = 17
RELAY_DELAY = 2  # Activation delay for relay in seconds
RESET_TIME = "" # Time of day to reset the device

MQTT_ACTIVE = False  # Enable MQTT
MQTT_BROKER = ""  # MQTT broker
MQTT_PORT = 1883  # MQTT port
MQTT_TOPIC = "relay"  # MQTT topic

# If you have MQTT authentication
MQTT_USERNAME = ""
MQTT_PASSWORD = ""
```