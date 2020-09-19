from time import sleep
#import RPi.GPIO as GPIO

# initialize variables/board
# ledpin = 32
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(ledpin, GPIO.OUT)

# # create PWM instance with frequency
# # frequency may need to be changed to mirror waveform generator
# pi_pwm = GPIO.PWM(ledpin, 1000) 
# pi_pwm.start(0)

# for i in range(100):
#     for duty in range(0, 101, 1):
#         duty = 50 # duty cycle is abritrarily chosen
#         pi_pwm.ChangeDutyCycle(duty)
#         sleep(.01)

#     # allows logic 1 to stay on for a while
#     sleep(.5)
    
#     for duty in range(100, -1, -1):
#         duty = 0
#         pi_pwm.ChangeDutyCycle(duty)
#         sleep(0.01)
#     sleep(.5)



# GPIO.setmode(GPIO.BCM)
# GPIO.setup(24, GPIO.OUT)
# print("hi")

# for i in range(100):
#     GPIO.output(24, True)
#     time.sleep(2)
#     GPIO.output(24, False)
#     time.sleep(2)

# print("done")

for i in range(5, 0):
    print(i)