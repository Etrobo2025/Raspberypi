#不正解音#

import RPi.GPIO as GPIO
import time

BUZZER_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

pwm = GPIO.PWM(BUZZER_PIN, 400)  # ちょっと低めの音からスタート
pwm.start(50)

# 不正解音：低めの音を2つ、少し長めに鳴らす
notes = [400, 300]
durations = [0.3, 0.4]

for freq, dur in zip(notes, durations):
    pwm.ChangeFrequency(freq)
    time.sleep(dur)

pwm.stop()
GPIO.cleanup()
