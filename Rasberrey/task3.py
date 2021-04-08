import RPi.GPIO as GPIO
from time import sleep
from task1 import num2decLight
import matplotlib as plt
import matplotlib.pyplot as plt
import numpy as np

def show_plot(x, y):
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set(xlabel='time (s)', ylabel='voltage (mV)')
    ax.grid()
    plt.show()


if __name__ == "__main__":
    try:
        GPIO.setmode(GPIO.BCM)
        leds = [26, 19, 13, 6, 5, 11, 9, 10]
        config = [0 for _ in range(8)]
        GPIO.setup(leds, GPIO.OUT)
        GPIO.output(leds, config)

        time = 10                          # Время работы
        frequency = 500                   # Частота сигнала
        sampingFrequency = frequency * 10   # Частота вывода

        t = np.arange(0, time, 1/sampingFrequency)
        u = 128 + 127 * np.sin(2 * np.pi * frequency * t)
        u = u.astype(int)
        show_plot(t, u)

        for i in u:
            num2decLight(i, leds)
            sleep(1 / sampingFrequency)
    except KeyboardInterrupt:
        GPIO.cleanup()
    finally:    
        GPIO.cleanup()