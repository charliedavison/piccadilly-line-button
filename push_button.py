import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

times_pressed = 1

while True:
	if GPIO.input(10) == GPIO.HIGH:
		print("Mind the gap! " + str(times_pressed))
		times_pressed += 1
