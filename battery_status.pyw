from psutil import sensors_battery
from win11toast import toast
from pynput import keyboard
from pymsgbox import alert
from pathlib import Path
from time import sleep
import threading
import traceback
import datetime

charging_toast = 0
uncharged_toast = 0
in80charged_toast = 0
fullycharged_toast = 0
running = 1

def flip():
    global running
    running = not running
    alert(f"Running status changed to: {bool(running)}", Path(__file__).name)

def log_thread_exception(args):
    with open("keyboard_crash.log", "a") as f:
        f.write(f"\n--- {datetime.datetime.now()} ---\n")
        f.write(f"Thread: {args.thread.name}\n")
        traceback.print_exception(args.exc_type, args.exc_value, args.exc_traceback, file=f)

Path("keyboard_crash.log").unlink(missing_ok=True)
threading.excepthook = log_thread_exception

hotkey = keyboard.GlobalHotKeys({"<ctrl>+<shift>+<alt>+o": flip})
hotkey.start()

while running:
    battery = sensors_battery()
    plugged = battery.power_plugged
    percent = str(battery.percent)
    if plugged and percent == '80' and charging_toast == 1 and in80charged_toast == 0:
        charging_toast = 0
        uncharged_toast = 0
        in80charged_toast = 1
        fullycharged_toast = 0
        toast('Charging Status🔌', 'Laptop is still charging. Current charge: ' + percent + '%', button='Dismiss')
        print(charging_toast, uncharged_toast, in80charged_toast, fullycharged_toast)
    if plugged and percent != '100' and charging_toast == 0 and in80charged_toast == 0:
        charging_toast = 1
        uncharged_toast = 0
        in80charged_toast = 0
        fullycharged_toast = 0
        toast('Charging Status🔌', 'Laptop is now charging. Current charge: ' + percent + '%', button='Dismiss')
        print(charging_toast, uncharged_toast, in80charged_toast, fullycharged_toast)
    if not plugged and percent != '100' and uncharged_toast == 0:
        charging_toast = 0
        uncharged_toast = 1
        in80charged_toast = 0
        fullycharged_toast = 0
        toast('Charging Status🔌', 'Laptop is uncharged. Current charge: ' + percent + '%', button='Dismiss')
        print(charging_toast, uncharged_toast, in80charged_toast, fullycharged_toast)
    if plugged and percent == '100' and fullycharged_toast == 0:
        charging_toast = 0
        uncharged_toast = 0
        in80charged_toast = 0
        fullycharged_toast = 1
        toast('Charging Status🔋', 'Fully charged! Unplug your laptop.', button='Dismiss')
        print(charging_toast, uncharged_toast, in80charged_toast, fullycharged_toast)
    sleep(1)

