#起動音2#
#どちらか好きな方を使用してください#

import RPi.GPIO as GPIO
import time

BUZZER_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

pwm = GPIO.PWM(BUZZER_PIN, 440)
pwm.start(50)

notes = [523, 392, 659]
durations = [0.1, 0.1, 0.4]

for freq, dur in zip(notes, durations):
    pwm.ChangeFrequency(freq)
    time.sleep(dur)
    time.sleep(0.05)

pwm.stop()
GPIO.cleanup()
