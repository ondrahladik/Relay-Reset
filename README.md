# Relay-Reset

## Install

```console
cd /opt
sudo apt update
sudo apt upgrade
sudo apt install python3-pip
sudo git clone https://github.com/ondrahladik/Relay-Reset.git  
cd Relay-Reset
sudo pip3 install -r requirements.txt
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
You can run the program and check if it works as it should:
```console
sudo python3 main.py
```
If everything is running, it would be better to set up a service so that the program runs in the background.

## Service config
Creating a service file:
```console
sudo nano /etc/systemd/system/Relay-Reset.service
```
Put these lines in the file:
```console
[Unit]
Description=Relay-Reset
After=network.target
Wants=network-online.target

[Service]
ExecStart=/usr/bin/python3 /opt/Relay-Reset/main.py
WorkingDirectory=/opt/Relay-Reset
StandardOutput=append:/var/log/Relay-Reset.log
StandardError=append:/var/log/Relay-Reset_error.log
Restart=always

[Install]
WantedBy=multi-user.target
```
```console
sudo chmod 666 /var/log/Relay-Reset.log
sudo chmod 666 /var/log/Relay-Reset_error.log
```
Starting the service:
```console
sudo systemctl daemon-reload
sudo systemctl enable Relay-Reset
sudo systemctl start Relay-Reset
```
Service management:
```console
sudo systemctl start Relay-Reset # Starting the service
sudo systemctl restart Relay-Reset # Restart the service
sudo systemctl stop Relay-Reset # Stop the service
sudo systemctl status Relay-Reset # Service status
tail -f /var/log/Relay-Reset.log # Tracking logs
```