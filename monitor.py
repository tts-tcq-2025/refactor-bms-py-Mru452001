import sys
from time import sleep

def blink_alert(cycles=6, delay=1):
    for _ in range(cycles):
        print('\r* ', end='')
        sys.stdout.flush()
        sleep(delay)
        print('\r *', end='')
        sys.stdout.flush()
        sleep(delay)

def vitals_ok(temperature, pulseRate, spo2):
    if temperature > 102 or temperature < 95:
        print('Temperature critical!')
        blink_alert()
        return False
    elif pulseRate < 60 or pulseRate > 100:
        print('Pulse Rate is out of range!')
        blink_alert()
        return False
    elif spo2 < 90:
        print('Oxygen Saturation out of range!')
        blink_alert()
        return False
    return True
