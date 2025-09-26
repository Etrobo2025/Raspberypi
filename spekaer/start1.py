#スタート音1#
#どちらか好きな方を使用してください#

import RPi.GPIO as GPIO
import time

BUZZER_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

pwm = GPIO.PWM(BUZZER_PIN, 600)
pwm.start(50)


notes = [600, 900, 1200]
durations = [0.15, 0.15, 0.2]

for freq, dur in zip(notes, durations):
    pwm.ChangeFrequency(freq)
    time.sleep(dur)

pwm.stop()
GPIO.cleanup()
