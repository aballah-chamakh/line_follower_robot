import time
import RPi.GPIO as GPIO
import Ultrason from Ultrason

class Robot:
    def __init__(self,name):
        GPIO.setmode(GPIO.BOARD)
        self.name = name
        self.motorL1  = 6
        self.motorL2  = 13
        self.motorR1  = 19
        self.motorR2  = 26
        print("robot {name} is created now".format(name=name))


        # set up GPIO pins
        GPIO.setup(self.motorL1, GPIO.OUT) # Connected to PWMA
        GPIO.setup(self.motorL2, GPIO.OUT) # Connected to AIN2
        GPIO.setup(self.motorR1, GPIO.OUT) # Connected to AIN1
        GPIO.setup(self.motorR2, GPIO.OUT) # Connected to STBY

        GPIO_TRIGGER_1 = 18
        GPIO_ECHO_1    = 19
        GPIO_TRIGGER_2 = 10
        GPIO_ECHO_2    = 11

        ultrason_forward  = Ultrason(GPIO_TRIGGER,GPIO_ECHO)
        us_obj_rigth    = Ultrason(GPIO_TRIGGER,GPIO_ECHO)

    def left(self):
        print("{name} turning left".format(name=self.name))
        GPIO.output(motorR1, GPIO.HIGH)
        GPIO.output(motorR2, GPIO.LOW)

    def right(self):
        print("{name} turning right".format(name=self.name))
        GPIO.output(motorL1, GPIO.HIGH)
        GPIO.output(motorL2, GPIO.LOW)

    def forward(self):
        print("{name} going forward".format(name=self.name))

        GPIO.output(motorR1, GPIO.HIGH)
        GPIO.output(motorR2, GPIO.LOW)

        GPIO.output(motorL1, GPIO.HIGH)
        GPIO.output(motorL2, GPIO.LOW)

    def backward(self):
        print("{name} going backward".format(name=self.name))
        GPIO.output(motorL1, GPIO.LOW)
        GPIO.output(motorL2, GPIO.HIGH)
        GPIO.output(motorL1, GPIO.LOW)
        GPIO.output(motorL2, GPIO.HIGH)

    def stop(self):
        print("{name} stopped".format(name=self.name))
        GPIO.output(motorL1, GPIO.LOW)
        GPIO.output(motorL2, GPIO.LOW)
        GPIO.output(motorL1, GPIO.LOW)
        GPIO.output(motorL2, GPIO.LOW)

    def rotate_360(self):
        print("{name} rotating 360".format(name=self.name))
        GPIO.output(motorL1, GPIO.HIGH)
        GPIO.output(motorL2, GPIO.LOW)
        GPIO.output(motorL1, GPIO.LOW)
        GPIO.output(motorL2, GPIO.HIGH)
        time.sleep(2)
        self.stop()
        time.sleep(1)
