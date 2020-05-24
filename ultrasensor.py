import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
TRIG = 18
ECHO = 24
buzzer = 4
led = 2

print(" Distance Measurement in progress")

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(led,GPIO.OUT)
GPIO.setup(buzzer,GPIO.OUT)

p = GPIO.PWM(2,20)
q = GPIO.PWM(4,20)

while True:
    GPIO.output(TRIG, False)

    time.sleep(1)

    GPIO.output(TRIG, True)
    time.sleep(0.01)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:
        pulse_start=time.time()

    while GPIO.input(ECHO)==1:
        pulse_end=time.time()

    pulse_duration=pulse_end-pulse_start

    distance = pulse_duration*11150
    distance = round(distance,2)
    p.start(0)
    q.start(0)
    if 20 < distance < 100:
        p.ChangeDutyCycle(2.0)
	    q.ChangeDutyCycle(2.0)
       
        
    if distance < 20:
        p.ChangeDutyCycle(100.0)
        q.ChangeDutyCycle(80.0)
      
    if distance > 100: 
	p.stop()
	q.stop()




