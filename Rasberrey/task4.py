import RPi.GPIO as GPIO
from time import sleep
from task1 import num2decLight
from task3 import show_plot
import scipy.io.wavfile as wav
import numpy as np

if __name__ == "__main__":
    input_file = "SOUND.WAV"
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