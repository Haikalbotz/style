#!/usr/bin/python2
# coding=utf-8

###### IMPORT MODULE ######

import os
import sys
import time

###### KODE WARNA ######

A  = '\033[1;97m'  # putih
B  = '\033[1;91m' # merah
C  = '\033[1;92m' # hijau
D = '\033[1;93m' # kuning
E  = '\033[1;94m' # biru
F  = '\033[1;95m' # Ungu
G = '\033[1;96m' # biru muda
H = '\033[1;90m' # Abu Abu

def runntxt(lolz):
    for noobs in lolz:
        sys.stdout.write(noobs)
        sys.stdout.flush()
        time.sleep(10. / 100)
        
os.system('clear')

###### LOGO ######

logo ='''\033[1;97m  ________  __________  _________
 /_  __/ / / / ____/  |/  / ____/
  / / / /_/ / __/ / /|_/ / __/
 / / / __  / /___/ /  / / /___
/_/ /_/ /_/_____/_/  /_/_____/

[01] Ubah Tampilan Termux
[02] Install Bahan
[00] Keluar
'''

def main():
    print logo
    ramdhan_noobs = input(">>> ")
    if ramdhan_noobs == 1:
        ubah()
    elif ramdhan_noobs == 2:
        install()
    elif ramdhan_noobs == 0:
        keluar()
    else:
        main()

def ubah():
    os.system('rm $HOME/../usr/etc/bash.bashrc')
    os.system('cp -f bash.bashrc $HOME/../usr/etc')
    os.system('clear')
    print "\033[1;97msedang proses Tunggu Sebentar..."
    time.sleep(1)
    os.system('termux-reload-settings')
    os.system('login')
    
def install():
    os.system('pkg install ruby') 
    os.system('pkg install toilet')
    os.system('pkg install figlet')
    os.system('gem install lolcat')
    main()

def keluar():
	os.sys.exit()
	
   
if __name__ == '__main__':
    main()

