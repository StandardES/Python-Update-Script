import time
import os

localtime = time.asctime( time.localtime(time.time()) )

os.system('sudo cp -r /var/www/html localtime-html')
