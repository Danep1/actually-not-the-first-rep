import RPi.GPIO as GPIO
import time as t
from math import log2


GPIO.setmode(GPIO.BCM)
leds = [21, 20, 16, 12, 7, 8, 25, 24]
config = [0 for _ in range(8)]
GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, config)


def decToBinList(decNumber):
    return list(map(int, bin(decNumber)[2:].rjust(8, str(0))))

def lightUp(ledNumber, period=1):
    GPIO.output(leds[ledNumber], 1)
    t.sleep(period)
    GPIO.output(leds[ledNumber], 0)


def lightDown(ledNumber, period=1):
    GPIO.output(leds[ledNumber], 0)
    t.sleep(period)
    GPIO.output(leds[ledNumber], 1)


def blink(ledNumber, blinkCount=1, blinkPeriod=0.1):
    for i in range(blinkCount):
        lightUp(ledNumber, blinkPeriod)
        t.sleep(blinkPeriod)


def runningLight(count, period):
    for n in range(count):
        lightUp(n % 8, period)


def runningDark(count, period):
    GPIO.output(leds, [1 for _ in range(8)])
    for n in range(count): 
        lightDown(n % 8, period)
    

def lightNumber(number):
    GPIO.output(leds, decToBinList(number))


def runningPattern(pattern, direction: int):
    step = 0
    while step < direction:
        GPIO.output(leds, decToBinList((pattern << (step % (8 - int(log2(pattern)))))))
        t.sleep(0.3)
        step += 1


def RGB():
    P_leds = [GPIO.PWM(channel, 60) for channel in leds]
    for i in P_leds:
        i.start(10)
    while True:
        for dc in range(10, 101, 5):
            for i in P_leds:
                i.ChangeDutyCycle(dc)
            t.sleep(0.05)

        for dc in range(100, 9, -5):
            for i in P_leds:
                i.ChangeDutyCycle(dc)
            t.sleep(0.05)
        


if __name__ == "__main__":
    RGB()
    t.sleep(5)
    GPIO.cleanup()
