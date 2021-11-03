from machine import Pin, Timer

led = Pin(25, Pin.OUT)
led_state = True

timing = Timer()

def tick(timer):
    global led, led_state
    led_state = not led_state
    led.value(led_state)

timing.init(freq=1, mode=Timer.PERIODIC, callback=tick)

