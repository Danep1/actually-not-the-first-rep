import RPi.GPIO as GPIO
from time import sleep
from task1 import num2decLight
from task3 import show_plot
import scipy.io.wavfile as wav
import numpy as np

if __name__ == "__main__":
    input_file = "SOUND.WAV"
    try:
        n, sound = wav.read(input_file)
        print()
        print("Количество каналов: ", sound.shape[1])
        print("Длительность аудиозаписи: {} с".format(round(sound.shape[0] / n, 3)))
        print("Частота семплирования: {} Гц".format(n))
        print()

        t = np.arange(0, sound.shape[0] / n, 1/n)
        show_plot(t, sound[:,0])

        u = np.array(map(lambda x: np.array(map(int, bin(x)[2:].rjust(16, str(0)))), sound))


    except KeyboardInterrupt:
        GPIO.cleanup()
    finally:    
        GPIO.cleanup()