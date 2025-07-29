from alerts import blink_alert 

def is_temp_ok(temp): return 95 <= temp <= 102
def is_pulse_ok(pulse): return 60 <= pulse <= 100
def is_spo2_ok(spo2): return spo2 >= 90

def vitals_ok(temperature, pulseRate, spo2):
    checks = [
        (temperature, is_temp_ok, "Temperature critical!"),
        (pulseRate, is_pulse_ok, "Pulse Rate is out of range!"),
        (spo2, is_spo2_ok, "Oxygen Saturation out of range!")
    ]

    for value, check_func, message in checks:
        if not check_func(value):
            print(message)
            blink_alert()
            return False
    return True
