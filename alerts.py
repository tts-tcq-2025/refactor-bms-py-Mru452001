
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
