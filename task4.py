import RPi.GPIO as GPIO
from time import sleep
import scipy
import matplotlib as plt
import matplotlib.pyplot as plt
import numpy as np


def show_plot(x, y):
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set(xlabel='time (s)', ylabel='voltage (mV)')
    ax.grid()
    plt.show()


def num2decLight(number, leds):
    GPIO.output(leds, list(map(int, bin(number)[2:].rjust(8, str(0)))))


if __name__ == "__main__":
    input_file = "example.wav"
    try:
        GPIO.setmode(GPIO.BCM)
        leds = [26, 19, 13, 6, 5, 11, 9, 10]
        config = [0 for _ in range(8)]
        GPIO.setup(leds, GPIO.OUT)
        GPIO.output(leds, config)

        n, sound = wav.read(input_file)
        print()
        print("Количество каналов: ", sound.shape[1])
        print("Длительность аудиозаписи: {} с".format(round(sound.shape[0] / n, 3)))
        print("Частота семплирования: {} Гц".format(n))
        print()

        t = np.arange(0, sound.shape[0] / n, 1/n)
        #show_plot(t, sound[:,0])

        for i in sound[:,0]:
            num2decLight(abs(i // 128), leds)
            sleep(1 / n)
    except ValueError:
        print(i)
    except KeyboardInterrupt:
        GPIO.cleanup()
    finally:    
        GPIO.cleanup()