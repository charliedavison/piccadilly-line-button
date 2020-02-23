import json, time
import requests
import RPi.GPIO as GPIO

BUTTON_DEBOUNCE_SECS = 10

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def send_notification():
	body = json.dumps({
		"notification": "Hello, I am a tube button",
		"accessCode": ""

	})
	requests.post(url = "https://api.notifymyecho.com/v1/NotifyMe", data = body)


while True:
	if GPIO.input(10) == GPIO.HIGH:
		send_notification()
		time.sleep(BUTTON_DEBOUNCE_SECS)
