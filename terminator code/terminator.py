import os

print("getting rid of junk processes...")

os.system("taskkill /f /im PhoneExperienceHost.exe") #who uses phone link?
os.system("taskkill /f /im CompatTelRunner.exe") #no good use and might hog your drive if you're using an hdd
#^ seems to not work due to the script not having admin access, wont comment out tho
os.system("taskkill /f /im smartscreen.exe") #if you're reading this then you are smart enough to not need smartscreen
os.system("taskkill /f /im TiWorker.exe") #the process doesnt seem to do anything useful
#^ also requires admin access
#os.system("net stop wuauserv")
#os.system("net stop SysMain")
#^ held until further notice

print("=========================================================================")

killff = input("press y then enter to close all open and background firefox tasks, press anything else to keep: ")

if killff == "y":
    os.system("taskkill /f /im  firefox.exe")

#killspool = input("press y to close spooler subsystem app (used to print stuff), press any other key to keep: ")

#if killspool == "y":
    #os.system("taskkill /f /im spoolsv.exe")
#^ held until further notice
input("Finished. Press Enter to quit")
