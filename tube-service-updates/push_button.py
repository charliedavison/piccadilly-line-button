import time
import RPi.GPIO as GPIO
from TFL import read_service_status

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

BUTTON_DEBOUNCE_SECS = 1.5

while True:
    if GPIO.input(10) == GPIO.HIGH:
        print("Reading service status")
        read_service_status()
        time.sleep(BUTTON_DEBOUNCE_SECS)