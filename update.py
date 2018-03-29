import time
import os

localtime = time.asctime( time.localtime(time.time()) )

print ('Local Script Started') 
print localtime
os.system('sudo apt-get update && sudo apt-get upgrade && sudo apt-get dist-upgrade && sudo apt-get autoremove')
print ('Local Script Ended')
print localtime

print ('test-webserver Script Started')
print localtime
os.system('ssh -t linux@192.168.1.172')
os.system('sudo apt-get update && sudo apt-get upgrade && sudo apt-get dist-upgrade && sudo apt-get autoremove')
os.system('exit')
print ('test-webserver Script Ended')
print localtime
