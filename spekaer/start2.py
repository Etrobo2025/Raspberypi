#スタート音2#
#どちらか好きな方を使用してください#

import RPi.GPIO as GPIO
import time

BUZZER_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

pwm = GPIO.PWM(BUZZER_PIN, 700)  # 高めの音からスタート
pwm.start(50)

# 明るく軽快なスタート音：3音メロディー
notes = [700, 900, 1100]
durations = [0.08, 0.08, 0.12]

for freq, dur in zip(notes, durations):
    pwm.ChangeFrequency(freq)
    time.sleep(dur)

pwm.stop()
GPIO.cleanup()
