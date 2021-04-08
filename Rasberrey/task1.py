import RPi.GPIO as GPIO


def num2decLight(number, leds):
    GPIO.output(leds, list(map(int, bin(number)[2:].rjust(8, str(0)))))


if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    leds = [26, 19, 13, 6, 5, 11, 9, 10]
    config = [0 for _ in range(8)]
    GPIO.setup(leds, GPIO.OUT)
    GPIO.output(leds, config)


    try:
        while True:
            x = int(input())
            if 0 <= x <= 255:
                num2decLight(x, leds)
            else:
                print("ВВЕДИТЕ НОРМАЛЬНОЕ ЧИСЛО ОТ 0 ДО 255")
    except ValueError:
        print("ВВОДИТЕ ЧИСЛО А НЕ ФИГНЮ КАКУЮ-ТО")
    except KeyboardInterrupt:
        GPIO.cleanup()
    finally:    
        GPIO.cleanup()
