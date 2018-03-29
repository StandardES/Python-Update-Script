import time
import os

localtime = time.asctime( time.localtime(time.time()) )

print("")
print ('**Local Script Started**') 
start = time.time()
print time.asctime( time.localtime(time.time()) )
print("")
os.system('sudo apt-get update && sudo apt-get upgrade && sudo apt-get dist-upgrade && sudo apt-get autoremove')
print ('**Local Script Ended**')
print time.asctime( time.localtime(time.time()) )
print("")
print ('**test-webserver Script Started**')
print time.asctime( time.localtime(time.time()) )
print("")
os.system('ssh -t linux@192.168.1.172')
print ('**test-webserver Script Ended**')
print time.asctime( time.localtime(time.time()) )
print("")
print ('**JSTRM Script Started**')
print time.asctime( time.localtime(time.time()) )
print("")
os.system('ssh -t linux@192.168.1.22')
print ('**JSTRM Script Ended**')
end = time.time()
print time.asctime( time.localtime(time.time()) )
print("")
total = end - start
print "Total time of update:", ("%.2f" % total), "seconds"
print("")
