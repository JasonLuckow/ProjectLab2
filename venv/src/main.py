import RPi.GPIO as GPIO

for i in range(10):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(24, GPIO.OUT)
    GPIO.output(24, True)
    time.sleep(1)
    GPIO.output(24, False)
    time.sleep(1)