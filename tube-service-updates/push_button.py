import pyttsx3
import requests
import os, time
import RPi.GPIO as GPIO

speach_engine = pyttsx3.init()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

BUTTON_DEBOUNCE_SECS = 1.5

def get_lines():
    response = requests.get(url = "https://api.tfl.gov.uk/line/mode/tube/status")
    if response.status_code == 200:
        return response.json()
    else:
        print("An error occurred. Status code: " + str(response.status_code))


def build_line_service_string(line):
    severityDescription = line['lineStatuses'][0]['statusSeverityDescription']
    return "The" + line['name'] + " line has a " + severityDescription

def get_service_status():
    lines = get_lines()
    line_service = []

    for line in lines:
        line_service.append(build_line_service_string(line))

    return line_service
    
def read_service_status():
    service_status = get_service_status()

    for line_status in service_status:
        speach_engine.say(line_status)
        speach_engine.runAndWait()

while True:
    if GPIO.input(10) == GPIO.HIGH:
        if speach_engine.isBusy() == True:
            speach_engine.stop()
        else:
            read_service_status()

        time.sleep(BUTTON_DEBOUNCE_SECS)