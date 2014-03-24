#!/usr/bin/env python
'''
@author: moloch,hypn0s
@copyright: GPL

Compile RCrackPy and put RainbowCrack.so
onto the PYTHONPATH or in the cwd
'''

import os
import RainbowCrack  # This is RainbowCrack.so

# Rainbow tables directory
tables_md5 = "/data/rt/md5/"
tables_mysqlsha1 = "/data/rt/mysqlsha1/"

print "[*] " + RainbowCrack.version()
if not os.path.exists(tables_md5):
	print '[!] MD5 Rainbow tables directory not found', tables_md5
	os._exit(1)

if not os.path.exists(tables_mysqlsha1):
	print '[!] MySQL SHA1 Rainbow tables directory not found', tables_mysqlsha1
	os._exit(1)

md5_hashes = [
	"af5b3d17aa1e2ff2a0f83142d692d701",
	"5d41402abc4b2a76b9719d911017c592",
	"5f4dcc3b5aa765d61d8327deb882cf99",
	]

mysqlsha1_hashes = [
	"f7c3bc1d808e04732adf679965ccc34ca7ae3441",
	]

print "[*] Cracking a list of MD5 hashes, please wait..."
results = RainbowCrack.crack(md5_hashes, tables_md5, debug=True, maxThreads=4)
print "[+] Got:", results

print "[*] Cracking a list of MySQL SHA1 hashes, please wait..."
results = RainbowCrack.crack(mysqlsha1_hashes, tables_mysqlsha1, mysqlsha1format=True, debug=True, maxThreads=4)
print "[+] Got:", results

