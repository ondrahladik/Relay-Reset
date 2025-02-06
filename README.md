# Relay-Reset

## Install

```console
sudo git clone https://github.com/ondrahladik/Relay-Reset.git  
cd Relay-Reset
sudo cp config config-SAMPLE.py config.py
```

## Config
```console
sudo nano config.py
```

```python
RELAY_PIN = 17
MQTT_BROKER = ""  # MQTT broker
MQTT_PORT = 1883  # MQTT port
MQTT_TOPIC = "relay"  # MQTT topic
```