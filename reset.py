import RPi.GPIO as GPIO
import time
from config import RELAY_PIN, RELAY_DELAY

def reset_device():
    print("Reset device")
    # Inicializace GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RELAY_PIN, GPIO.OUT)
    GPIO.output(RELAY_PIN, GPIO.HIGH)
    time.sleep(RELAY_DELAY)
    GPIO.cleanup() 
    print("Reset complete")