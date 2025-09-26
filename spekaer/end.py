#終了音#

import RPi.GPIO as GPIO
import time

BUZZER_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

pwm = GPIO.PWM(BUZZER_PIN, 1175)
pwm.start(40)

notes = [1175, 1047, 988, 880]
durations = [0.15, 0.15, 0.15, 0.3]

for freq, dur in zip(notes, durations):
    pwm.ChangeFrequency(freq)
    time.sleep(dur)

pwm.stop()
GPIO.cleanup()
