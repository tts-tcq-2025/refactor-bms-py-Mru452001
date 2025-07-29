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


def is_temp_ok(temp):
    return 95 <= temp <= 102


def is_pulse_ok(pulse):
    return 60 <= pulse <= 100


def is_spo2_ok(spo2):
    return spo2 >= 90


def vitals_ok(temperature, pulseRate, spo2):
    if not is_temp_ok(temperature):
        print("Temperature critical!")
        blink_alert()
        return False

    if not is_pulse_ok(pulseRate):
        print("Pulse Rate is out of range!")
        blink_alert()
        return False

    if not is_spo2_ok(spo2):
        print("Oxygen Saturation out of range!")
        blink_alert()
        return False

    return True
