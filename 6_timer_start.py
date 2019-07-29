
import time
from time import gmtime, strftime
import subprocess
from configparser import ConfigParser


cfg = ConfigParser()
cfg.read("./0_Settings.ini")
times = cfg.get('timer', 'time')
dates = cfg.get('timer', 'date')
file_address = cfg.get('address', 'file_address_is')
###############################
time_to_start = times
data_to_start = dates


###############################

def start():
    waiting_time = True
    while waiting_time:
        time_now = (strftime("%H:%M"))
        data_now = (strftime("%d.%m"))
        time.sleep(1)
        if data_now == data_to_start:
            time.sleep(1)
            if time_now == time_to_start:
                print("Selected time is now. Starting Autofill.")
                subprocess.call("4_Autofill.py", shell=True)
                waiting_time = False


start()
