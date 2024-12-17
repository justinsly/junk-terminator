import os
import random
import subprocess

os.system("title Junk Terminator")

tips = ["cool tip: its recommended to periodically run this program every time", "cool tip: you can", "cool tip: give me all your money (pls)"]

print("getting rid of junk processes...")

os.system("taskkill /f /im PhoneExperienceHost.exe") #who uses phone link?
os.system("taskkill /f /im CompatTelRunner.exe") #no good use and might hog your drive if you're using an hdd
os.system("taskkill /f /im smartscreen.exe") #if you're reading this then you are smart enough to not need smartscreen
os.system("taskkill /f /im TiWorker.exe") #the process doesnt seem to do anything useful
os.system("taskkill /f /im HxTsr.exe") #outlook
try:
    subprocess.check_call("net stop wuauserv", stderr=subprocess.DEVNULL)
except subprocess.CalledProcessError:
    print("failed to close windows update service")

try:
    subprocess.check_call("net stop SysMain", stderr=subprocess.DEVNULL)
except subprocess.CalledProcessError:
    print("failed to close sysmain service")


print(" ")
print("-------------------------------------------------------------------------------")
print(" ")


killspool = input("press y to close spooler subsystem app (used for printers), press any other key to keep: ")

if killspool == "y":
    os.system("taskkill /f /im spoolsv.exe")


print(" ")
print("Finished. Press Enter to quit")
print(" ")
input(random.choice(tips))