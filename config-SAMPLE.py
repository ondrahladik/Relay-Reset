RELAY_PIN = 17 # GPIO pin number for relay
RELAY_DELAY = 2  # Activation delay for relay in seconds
RELAY_DELAY_DEVICE = 2  # Device reset delay after relay reset
RESET_TIME = "16:00" # Time of day to reset the device

MQTT_ACTIVE = False  # Enable MQTT
MQTT_BROKER = ""  # MQTT broker
MQTT_PORT = 1883  # MQTT port
MQTT_TOPIC = "relay"  # MQTT topic

# If you have MQTT authentication
MQTT_USERNAME = "" # MQTT username
MQTT_PASSWORD = "" # MQTT password