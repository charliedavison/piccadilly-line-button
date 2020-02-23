import os, random, time
import RPi.GPIO as GPIO
import pygame

BUTTON_DEBOUNCE_SECS = 1.5

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

pygame.mixer.init()

while True:
	if GPIO.input(10) == GPIO.HIGH:
		if pygame.mixer.music.get_busy() == True:
			print("Stopping")
			pygame.mixer.music.stop()
			time.sleep(BUTTON_DEBOUNCE_SECS)
		else:
			random_audio = random.choice(os.listdir('audio'))
			print("Playing " + str(random_audio))
			pygame.mixer.music.load('audio/' + random_audio)
			pygame.mixer.music.play()
			time.sleep(BUTTON_DEBOUNCE_SECS) 
