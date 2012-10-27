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

queryString = "SELECT uid FROM users WHERE username='" + username + "' AND password='" + password + "'"
cur.execute(queryString);
uid = cur.fetchone()

logFile = open('loginlog.txt', 'a')
logFile.write('Select complete\n')
logFile.close()

if cur.rowcount != 0:
    logFile = open('loginlog.txt', 'a')
    logFile.write('if entered\n')
    logFile.close()
    # Return a message to user that they didn't enter a valid username/password combo.
    # Toast it to the screen and stay on that activity.
else:
    logFile = open('loginlog.txt', 'a')
    logFile.write('else entered\n')
    logFile.close()

    #Return a message to phone to go to main activity.  Store the users username, password, and uid.

logFile = open('loginlog.txt', 'a')
logFile.write('Done\n')
logFile.close()



