import os
import random

tips = ["cool tip: its recommended to periodically run this program every time", "cool tip: you can contribute to the program on https://github.com/justinsly/junk-terminator", "cool tip: you can", "cool tip: give me all your money (pls)"]

print("getting rid of junk processes...")

os.system("taskkill /f /im PhoneExperienceHost.exe") #who uses phone link?
os.system("taskkill /f /im CompatTelRunner.exe") #no good use and might hog your drive if you're using an hdd
os.system("taskkill /f /im smartscreen.exe") #if you're reading this then you are smart enough to not need smartscreen
os.system("taskkill /f /im TiWorker.exe") #the process doesnt seem to do anything useful

os.system("net stop wuauserv")
os.system("net stop SysMain")
#^ spits out big errors when they fail, need to figure out how to suppress that and replace it with shorter errors


print(" ")
print("-------------------------------------------------------------------------------")
print(" ")


killspool = input("press y to close spooler subsystem app (used to print stuff), press any other key to keep: ")

if killspool == "y":
    os.system("taskkill /f /im spoolsv.exe")


print(" ")
print("Finished. Press Enter to quit")
print(" ")
input(random.choice(tips))