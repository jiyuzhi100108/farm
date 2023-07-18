import time
import RPi.GPIO as GPIO
import Adafruit_ADS1x15 # 引用模数转换器第三方库包
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(6, GPIO.OUT,initial = False)
adc = Adafruit_ADS1x15.ADS1115() # 生成模数转换器具体实例
High =1000
Low =2000
while True:
    L1 = adc.read_adc(0, gain=1)
    L2 = adc.read_adc(1, gain=1)
    La = (L1+L2)/2
    print(La)
    if La < High:
        print("光照强，开启水幕遮挡")
        GPIO.output(5, GPIO.HIGH) #GPIO5/、6高电平
        GPIO.output(6, GPIO.HIGH)
        time.sleep(35)
        GPIO.output(5, GPIO.LOW)
        GPIO.output(6, GPIO.LOW)
    if La > Low:
        print("光照弱，开启补光")
        GPIO.output(12, GPIO.HIGH)
        time.sleep(60)
        GPIO.output(12, GPIO.LOW)