from win11toast import toast
from time import sleep
from psutil import sensors_battery

charging_toast = 0
uncharged_toast = 0
fullycharged_toast = 0

while True:
    battery = sensors_battery()
    plugged = battery.power_plugged
    percent = str(battery.percent)
    if plugged and percent != '100' and charging_toast == 0:
        charging_toast = 1
        uncharged_toast = 0
        fullycharged_toast = 0
        toast('Charging Status🔌', 'Laptop is now charging. Current charge: ' + percent + '%', button='Dismiss')
        print(charging_toast, uncharged_toast, fullycharged_toast)
    if not plugged and percent != '100' and uncharged_toast == 0:
        charging_toast = 0
        uncharged_toast = 1
        fullycharged_toast = 0
        toast('Charging Status🔌', 'Laptop is uncharged. Current charge: ' + percent + '%', button='Dismiss')
        print(charging_toast, uncharged_toast, fullycharged_toast)
    if plugged and percent == '100' and fullycharged_toast == 0:
        charging_toast = 0
        uncharged_toast = 0
        fullycharged_toast = 1
        toast('Charging Status🔋', 'Fully charged! Unplug your laptop', button='Dismiss')
        print(charging_toast, uncharged_toast, fullycharged_toast)
    sleep(1)
    
