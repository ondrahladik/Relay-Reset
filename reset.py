import os
import time
import logging
import RPi.GPIO as GPIO
from config import RELAY_PIN, RELAY_DELAY

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s', 
    handlers=[
        logging.FileHandler('/var/log/Relay-Reset.log'),
        logging.StreamHandler()
    ]
)

# Function to reset the relay
def reset_relay():
    logging.info("Reset relay")  

    try:
        # Set the GPIO mode
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(RELAY_PIN, GPIO.OUT)
        GPIO.output(RELAY_PIN, GPIO.HIGH)  
        time.sleep(RELAY_DELAY)            
        GPIO.output(RELAY_PIN, GPIO.LOW)   
        logging.info("Reset relay complete.")
    except Exception as e:
        logging.error(f"Error resetting relay: {e}")
    finally:
        GPIO.cleanup()
        logging.info("GPIO cleanup complete.")

# Function to reset the device
def reset_device():
    logging.info("Rebooting device.")  
    try:
        os.system("sudo reboot")
    except Exception as e:
        logging.error(f"Error rebooting device: {e}")

# Function to reset all (relay and device)
def reset_all():
    logging.info("Reset device and relay.")  
    reset_relay()
    time.sleep(2)  
    reset_device()
