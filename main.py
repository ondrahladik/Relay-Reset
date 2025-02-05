import RPi.GPIO as GPIO
import time

print("Starting the program...")

# GPIO pin pro relé
RELAY_PIN = 17  

# Nastavení GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY_PIN, GPIO.OUT)

# Relé je aktivní při LOW
GPIO.output(RELAY_PIN, GPIO.LOW)

def reset_device():
    print("Reset device")
    GPIO.output(RELAY_PIN, GPIO.HIGH)  # Sepnutí relé 
    time.sleep(1)  # Doba resetu
    GPIO.output(RELAY_PIN, GPIO.LOW)  # Vypnutí relé 
    print("Reset complete")

try:
    while True:
        time.sleep(30)  # Počkej 2 minuty
        reset_device()   # Proveď reset

except KeyboardInterrupt:
    print("Exiting the program...")
    GPIO.cleanup()  # Uvolnění GPIO pinů
