import RPi.GPIO as GPIO
import time
import logging
from config import RELAY_PIN, RELAY_DELAY

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s', 
    handlers=[
        logging.FileHandler('/var/log/Relay-Reset.log'),
        logging.StreamHandler()
    ]
)

def reset_device():
    logging.info("Reset device")  

    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(RELAY_PIN, GPIO.OUT)
        GPIO.output(RELAY_PIN, GPIO.HIGH)
        time.sleep(RELAY_DELAY)
    except Exception as e:
        logging.error(f"Chyba při resetování: {e}")
    finally:
        GPIO.cleanup()
        logging.info("Reset complete")  
