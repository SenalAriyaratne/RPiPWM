
# for this task I used a tutorial.
# Link of the tutorial : https://hackernoon.com/android-things-basics-measure-distance-with-ultrasonic-sensor-3196fe5d7d7c

import RPi.GPIO as io
import time


io.setmode(io.BCM)
io.setwarnings(False)

#set GPIO Pins
led = 4
trig = 21
ech = 20


io.setup(trig, io.OUT)
io.setup(ech, io.IN)
io.setup(led, io.OUT)

pwm = io.PWM(led,100)

pwm.start(0)


def distance():
    # set Trigger pin to HIGH
    io.output(trig, io.HIGH)
 
    # set Trigger pin to LOW
    time.sleep(0.00001)
    io.output(trig,io.LOW)
 

    
    while io.input(ech) == 0:
        Start = time.time()
 
    
    while io.input(ech) == 1:
        End = time.time()
 
    
    diff = End - Start # time difference 

    distance = (diff * 34300) / 2
 
    return distance

try:
    while True:
        dist = distance() # value from distance is stored in the variable dist
        print ("Distance = %.1f cm" % dist)
            
        if (dist<=25):
            pwm.ChangeDutyCycle((25-dist)*2)
            time.sleep(0.005)
                
        else:
            pwm.ChangeDutyCycle(0)
                
        time.sleep(1)

 
#when the user enters CTRL + C the prgram quits
except KeyboardInterrupt:
    print("Measurement stopped by User")
    pwm.stop()
    io.cleanup()
