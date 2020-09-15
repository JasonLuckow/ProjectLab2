from time import sleep
import RPi.GPIO as GPIO

ledpin = 32				# PWM pin connected to LED
GPIO.setwarnings(False)			#disable warnings
GPIO.setmode(GPIO.BOARD)		#set pin numbering system
GPIO.setup(ledpin,GPIO.OUT)
pi_pwm = GPIO.PWM(ledpin,1000)		#create PWM instance with frequency
pi_pwm.start(0)				#start PWM of required Duty Cycle 
for i in range(100):
    for duty in range(0,101,1):
        duty = 50
        pi_pwm.ChangeDutyCycle(duty) #provide duty cycle in the range 0-100
        sleep(0.01)
    sleep(0.5)
    
    for duty in range(100,-1,-1):
        duty = 0
        pi_pwm.ChangeDutyCycle(duty)
        sleep(0.01)
    sleep(.5)

print("done")

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(24, GPIO.OUT)
# print("hi")

# for i in range(100):
#     GPIO.output(24, True)
#     time.sleep(2)
#     GPIO.output(24, False)
#     time.sleep(2)

# Create a PWM instance
