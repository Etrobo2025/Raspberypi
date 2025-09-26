# スピーカーテスト用プログラム
# GPIO 17 番ピンに接続されたブザー/スピーカーから1秒間ビープ音を鳴らします

import RPi.GPIO as GPIO
import time

BUZZER_PIN = 17  # ブザーを接続するGPIOピン番号

# GPIOモードをBCMに設定（GPIO番号で指定）
GPIO.setmode(GPIO.BCM)

# ブザー用GPIOピンを出力モードに設定
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# PWMオブジェクトを作成（周波数440Hz = ラの音）
pwm = GPIO.PWM(BUZZER_PIN, 440)

# PWMを開始（デューティ比50%で鳴らす）
pwm.start(50)

# 1秒間ビープ音を鳴らす
time.sleep(1)

# PWMを停止
pwm.stop()

# GPIOを解放（安全のため）
GPIO.cleanup()