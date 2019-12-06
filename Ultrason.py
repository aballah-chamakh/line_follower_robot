import time
import RPi.GPIO as GPIO

class Ultrason :
    def __init__(self,GPIO_TRIGGER,GPIO_ECHO):
        self.GPIO_TRIGGER = GPIO_TRIGGER
        self.GPIO_ECHO = GPIO_ECHO
        GPIO.setup(self.GPIO_TRIGGER, GPIO.OUT)
        GPIO.setup(self.GPIO_ECHO, GPIO.IN)

    def distance():
    # set Trigger to HIGH
        GPIO.output(self.GPIO_TRIGGER, True)

    # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(self.GPIO_TRIGGER, False)

        StartTime = time.time()
        StopTime = time.time()

    # save StartTime
        while GPIO.input(self.GPIO_ECHO) == 0:
            StartTime = time.time()

    # save time of arrival
        while GPIO.input(self.GPIO_ECHO) == 1:
            StopTime = time.time()

    # time difference between start and arrival
        TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2

        return int(distance)
