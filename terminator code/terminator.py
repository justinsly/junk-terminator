import os

print("getting rid of junk/useless processes...")

os.system("taskkill /f /im PhoneExperienceHost.exe") #who uses phone link?
os.system("taskkill /f /im CompatTelRunner.exe") #no good use and might hog your drive if you're using an hdd
os.system("taskkill /f /im smartscreen.exe") #if you're reading this then you are smart enough to not need smartscreen
#os.system("net stop wuauserv")
#^ doesnt work


print("=========================================================================")

killff = input("press y then enter to close all firefox open and background tasks, press anything else to keep: ")

if killff == "y":
    os.system("taskkill /f /im  firefox.exe")


input("Finished. Press Enter to quit")
