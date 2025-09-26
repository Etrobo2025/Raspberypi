#正解音#

import RPi.GPIO as GPIO
import time

BUZZER_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

pwm = GPIO.PWM(BUZZER_PIN, 600)
pwm.start(50)

# 800Hz（真ん中の音）を削除した2音の正解音
notes = [600, 1000]
durations = [0.15, 0.15]

for freq, dur in zip(notes, durations):
    pwm.ChangeFrequency(freq)
    time.sleep(dur)

pwm.stop()
GPIO.cleanup()
