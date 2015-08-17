#! /usr/bin/python

"""
Script to upgrade ddbb in mysql servers
17/08/2015 by Miguel Jimenez
"""

import os
import sys

ddbb_servers = [] #Complete with MySQL servers
ddbb_users = [] #Complete with MySQL users
ddbb_passwords = [] #Complete with MySQL passwords
ddbb_names = [] #Complete with MySQL DDBB names

if sys.argv[1] == "help":
    print("Usage:\n\tupdateNicaDDBB.py mysql_file.sql")
    sys.exit(1)

if not os.path.exists(sys.argv[1]):
    print("Cannot open " + sys.argv[1])
    sys.exit(1)

i = 0
for server in ddbb_servers:
    
    os.system("mysql -h" + server + " -u" + ddbb_users[i] + " -p" + ddbb_passwords[i] + " " + ddbb_names[i] + " < " + sys.argv[1])
    
    i += 1