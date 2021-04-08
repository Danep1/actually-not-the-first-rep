import RPi.GPIO as GPIO
from time import sleep
from task1 import num2decLight

if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    leds = [26, 19, 13, 6, 5, 11, 9, 10]
    config = [0 for _ in range(8)]
    GPIO.setup(leds, GPIO.OUT)
    GPIO.output(leds, config)
    try:
        n = int(input("Введите число повторений:"))
        delay = 0.05  # Время задержки
        for i in range(n):
            for u in range(0, 256):
                num2decLight(u, leds)
                sleep(delay)
            for u in range(254, -1, -1):
                num2decLight(u, leds)
                sleep(delay)
    except ValueError:
        print("ВВОДИТЕ ЧИСЛО А НЕ ФИГНЮ КАКУЮ-ТО")
    except KeyboardInterrupt:
        GPIO.cleanup()
    finally:    
        GPIO.cleanup()