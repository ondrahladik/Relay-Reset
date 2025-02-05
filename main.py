import RPi.GPIO as GPIO
import time

print("Starting the program...")

# GPIO pin pro relé
RELAY_PIN = 17  

# Nastavení GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY_PIN, GPIO.OUT)

# Relé je LOW aktivní
GPIO.output(RELAY_PIN, GPIO.HIGH)

def reset_device():
    print("Reset device")
    GPIO.output(RELAY_PIN, GPIO.LOW)  # Sepnutí relé 
    time.sleep(1)  # Doba resetu
    GPIO.output(RELAY_PIN, GPIO.HIGH)  # Vypnutí relé 
    print("Reset complete")

try:
    while True:
        time.sleep(120)  # Počkej 2 minuty
        reset_device()   # Proveď reset

except KeyboardInterrupt:
    print("Exiting the program...")
    GPIO.cleanup()  # Uvolnění GPIO pinů
