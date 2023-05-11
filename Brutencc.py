import os
import random
import sys
import time
import getpass
def ketik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)
os.system('clear')
print ('\33[0;31m        █████████████\33[0;37m    _   _   _   _   _   _   _   _')
print ('\33[0;31m        █████████████\33[0;37m   / \ / \ / \ / \ / \ / \ / \ / \ ')
print ('\33[0;37m        █████████████\33[0;37m  ( F | a | c | e | G | r | a | m )')
print ('\33[0;37m        █████████████\33[0;37m   \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/  ')
print ('       —————————————————————————————————————————————')
print ('                Authors      :\33[0;31m remon69z')
print ('\33[0;37m                Users        :\33[0;31m Not Registers\33[0;37m')
print ('\33[0;37m       —————————————————————————————————————————————')
print ('')
print ('')
userr = input ('  Enter license : \33[0;32m ')
os.system('sleep 1')
os.system('clear')
print ('\33[0;31m        █████████████\33[0;37m    _   _   _   _   _   _   _   _')
print ('\33[0;31m        █████████████\33[0;37m   / \ / \ / \ / \ / \ / \ / \ / \ ')
print ('\33[0;37m        █████████████\33[0;37m  ( F | a | c | e | G | r | a | m )')
print ('\33[0;37m        █████████████\33[0;37m   \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/  ')
print ('       —————————————————————————————————————————————')
print ('                Authors      :\33[0;31m REMONZ69')
print ('\33[0;37m                Users        :\33[0;37m Lic66910-afg772937c (\33[0;31m Active\33[0;37m )')
print ('\33[0;37m       —————————————————————————————————————————————')
print ('')
print ('')
print ('        Saldo : 100k')
print ('')
print ('        [\33[0;31m1\33[0;37m] 50k 1 Minggu (\33[0;31m Closed\33[37m] )')
print ('        [\33[0;31m2\33[0;37m] 100k 1 Bulan (\33[0;31m Closed\33[37m] )')
print ('        [\33[0;31m3\33[0;37m] 300k Permanent (\33[0;31m *Active\33[37m )')
print ('        [\33[0;31m0\33[0;37m] Exit\33[0;37m')
print ('')
print ('')
pill = input ('        Select Options : \33[0;32m ')
os.system('sleep 1')
while pill not in ["1", "2", "3", "4"]:
      pill == input ('[\33[0;31m?\33[0;37m] Ketik Y :\33[0;33m ')
if pill == '1':
   print ('')
   os.system('sleep 2')
   print ('Maaf 50k 1 Minggu Sedang Close')
elif pill == '2':
     os.system('sleep 2')
     print ('Maaf 100k 1 Bulan Sedang Close')
elif pill == '3':
     os.system('sleep 2')
     print ('Maaf Saldo Anda Tidak Cukup Mohon Hubungi Admin Untuk Membeli')
     os.system('sleep 1')
