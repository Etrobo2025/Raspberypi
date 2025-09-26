#起動音1#
#どちらか好きな方を使用してください#

import RPi.GPIO as GPIO
import time

BUZZER_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
pwm = GPIO.PWM(BUZZER_PIN, 440)

pwm.start(50)

# 再生する音の周波数（Hz）のリスト
notes = [440, 554, 659, 880, 659, 554, 440]
# 各音の再生時間（秒）のリスト
durations = [0.1, 0.1, 0.1, 0.2, 0.1, 0.1, 0.3]

# 音階と再生時間を組み合わせて順に再生
for freq, dur in zip(notes, durations):
    pwm.ChangeFrequency(freq)  # 周波数を変更
    time.sleep(dur)           # 指定時間だけ再生

pwm.stop()
GPIO.cleanup()
