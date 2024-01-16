from win11toast import toast
from time import sleep
import psutil

toast_count = 0

while True:
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = str(battery.percent)
    if plugged and percent != "100" and toast_count == 0:
        toast('Charging Status🔌', 'Laptop is now charging. Current charge: ' + percent + '%', button='Dismiss')
        toast_count += 1
        print("toast_count", toast_count)
    if plugged and percent == "100" and toast_count == 1:
        toast('Charging Status🔋', 'Fully charged! Unplug your laptop', button='Dismiss')
        toast_count = 0
        print("toast_count", toast_count)
    sleep(1)
    
