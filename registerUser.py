#!/usr/bin/env python

# This script registers a new user, or tells the user to enter a new username if the username they choose is taken.
import cgi, os
import cgitb; cgitb.enable()
import sys
import glob
sys.path.append('\Python27\Scripts')

import MySQLdb as mdb

logFile = open('registerlog.txt', 'a')
logFile.write('Entered register user script\n')
logFile.close()

db = mdb.connect(host = "eecs394db.cfcbispllbb4.us-east-1.rds.amazonaws.com",
                       user = "mrmarkwell",
                       passwd = "qwertyuiop",
                       db = "bluedb")

logFile = open('registerlog.txt', 'a')
logFile.write('Connected DB\n')
logFile.close()

cur = db.cursor()

form = cgi.FieldStorage()

username = form['username'].value

password = form['password'].value

logFile = open('registerlog.txt', 'a')
logFile.write('Read Post\n')
logFile.close()

queryString = "SELECT username FROM users WHERE username='" + username + "'"
cur.execute(queryString);
uid = cur.fetchone()

logFile = open('registerlog.txt', 'a')
logFile.write('Select complete\n')
logFile.close()

if cur.rowcount != 0:
    logFile = open('registerlog.txt', 'a')
    logFile.write('if entered\n')
    logFile.close()
    # Return a message to user that this username is taken.
    # Toast it to the screen and stay on that activity.
else:
    logFile = open('registerlog.txt', 'a')
    logFile.write('else entered\n')
    logFile.close()

    queryString = "INSERT INTO users (username, password, uuid) values('" + username + "','" + password + "', UUID())"
    cur.execute(queryString);
    db.commit()

    logFile = open('registerlog.txt', 'a')
    logFile.write('db.commit\n')
    logFile.close()
    # Return a message to phone to go to main activity and store this username and password.

logFile = open('registerlog.txt', 'a')
logFile.write('Done\n')
logFile.close()


