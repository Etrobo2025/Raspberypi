from gpiozero import DigitalOutputDevice, DigitalInputDevice
from random import randint
import time

# LEDとスイッチのGPIOピン番号
LED_PIN = [18, 23, 24, 25, 12, 16, 20, 21]
SW_PIN = [4, 17, 27, 22, 5, 6, 13, 19]
SW_START_PIN = [26]

scoa = 0

leds = [DigitalOutputDevice(pin) for pin in LED_PIN]
sws = [DigitalInputDevice(pin, pull_up=False) for pin in SW_PIN]
sw_st = DigitalInputDevice(SW_START_PIN[0], pull_up=False)

while True:
    if sw_st.value == 1:
        print("スタート")
        break
    time.sleep(0.1)
    
start_time = time.time()

while True:
    if (time.time() - start_time > 14) & (time.time() - start_time < 15):
        print("15秒経過")
        
    if time.time() - start_time > 30:
        print("30秒経過。ゲーム終了")
        print("合計スコア ", scoa)
        break
    # 0〜7までランダム
    num = randint(0, 7)        
    led = leds[num]
    sw = sws[num]
    
    # 難易度調整（反応時間）
    led.on()
    time.sleep(1)              
    led.off()
    time.sleep(0.3)  

    pressed_index = -1
    for i, s in enumerate(sws): #iは何回ループしたか、sは配列sws[]の中身が入る、でその中身分ループする
        if s.value == 1:        #スイッチが押されているか判定、配列sws[]の中身はhighか
            pressed_index = i   #どこにスイッチが押されたか
            break               #最初に押されたスイッチだけ判定

    if pressed_index == -1:
        continue                #何も押されていなかたら先頭に戻る

    if pressed_index == num:    #上のiとnumが同じだったら
        # 正しいスイッチが押された場合
        for i in range(2):
            led.on()
            time.sleep(0.15)
            led.off()
            time.sleep(0.15)
        scoa = scoa + 1
        print("⭕　スコア→→→", scoa)
        
    else:
        # 間違ったスイッチが押された場合
        for i in range(6):
            led.on()
            time.sleep(0.06)
            led.off()
            time.sleep(0.06)
        scoa = scoa - 1       
        if scoa < 0:
            scoa = 0
        print("❌　スコア→→→", scoa)
        

