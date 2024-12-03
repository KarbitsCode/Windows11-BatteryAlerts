from psutil import sensors_battery
from win11toast import toast
from time import sleep

charging_toast = 0
uncharged_toast = 0
in80charged_toast = 0
fullycharged_toast = 0

while True:
    battery = sensors_battery()
    plugged = battery.power_plugged
    percent = str(battery.percent)
    # print(battery)
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
    
