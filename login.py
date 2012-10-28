#!/usr/bin/env python

# This script allows a user to log in.
import cgi, os
import cgitb; cgitb.enable()
import sys
sys.path.append('\Python27\Scripts')

import MySQLdb as mdb

logFile = open('loginlog.txt', 'a')
logFile.write('Entered login script\n')
logFile.close()

db = mdb.connect(host = "eecs394db.cfcbispllbb4.us-east-1.rds.amazonaws.com",
                       user = "mrmarkwell",
                       passwd = "qwertyuiop",
                       db = "bluedb")

logFile = open('loginlog.txt', 'a')
logFile.write('Connected DB\n')
logFile.close()

cur = db.cursor()

form = cgi.FieldStorage()

username = form['username'].value

password = form['password'].value

logFile = open('loginlog.txt', 'a')
logFile.write('Read Post\n')
logFile.close()

queryString = "SELECT uuid FROM users WHERE username='" + username + "' AND password='" + password + "'"
cur.execute(queryString);

logFile = open('loginlog.txt', 'a')
logFile.write('Select complete\n')
logFile.close()

if cur.rowcount != 0:
    logFile = open('loginlog.txt', 'a')
    logFile.write('if entered\n')
    logFile.close()

    print "Content-Type: text"
    print
    print "False"
    print
    # Toast it to the screen and stay on that activity.
else:
    logFile = open('loginlog.txt', 'a')
    logFile.write('else entered\n')
    logFile.close()

    print "Content-Type: text"
    print
    print "True"
    print

logFile = open('loginlog.txt', 'a')
logFile.write('Done\n')
logFile.close()



