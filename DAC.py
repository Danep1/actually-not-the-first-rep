import RPi.GPIO as GPIO
from time import sleep


def num2decLight(number, leds):
    GPIO.output(leds, list(map(int, bin(number)[2:].rjust(8, str(0)))))


if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    leds = [26, 19, 13, 6, 5, 11, 9, 10]
    config = [0 for _ in range(8)]
    GPIO.setup(leds, GPIO.OUT)
    GPIO.output(leds, config)

    GPIO.setup(17, GPIO.OUT)
    GPIO.output(17, 1)

    GPIO.setup(4, GPIO.IN)
    num2decLight(128, leds)

    try:
        while True:
            v = 127
            for i in range(6, -1, -1):          
                num2decLight(v, leds)
                sleep(0.001)
                if GPIO.input(4):  # DOES NOT LIGHT
                    v += 2 ** i
                else:
                    v -= 2 ** i 
            print("Digital value: {}, Analog value: {} V".format(v, round(3.3 / 255 * v, 2)))
            sleep(0.01)
            
    except KeyboardInterrupt:
        GPIO.cleanup()
    finally:    
        GPIO.cleanup()