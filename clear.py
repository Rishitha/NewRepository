#!/usr/bin/env python
import cgi, os
import cgitb; cgitb.enable()
import sys
import glob
sys.path.append('\Python27\Scripts')

import MySQLdb as mdb

logFile = open('clearlog.txt', 'a')
logFile.write('Entered clear script\n')
logFile.close()

db = mdb.connect(host = "eecs394db.cfcbispllbb4.us-east-1.rds.amazonaws.com",
                       user = "mrmarkwell",
                       passwd = "qwertyuiop",
                       db = "bluedb")

logFile = open('clearlog.txt', 'a')
logFile.write('Connected DB\n')
logFile.close()

cur = db.cursor()

form = cgi.FieldStorage()

username = form['username'].value

password = form['password'].value

clear = form['clear'].value

logFile = open('clearlog.txt', 'a')
logFile.write('Read Post\n')
logFile.close()



queryString = "SELECT uuid FROM users WHERE username='" + username + "' AND password='" + password + "'"
cur.execute(queryString);
uuid = cur.fetchone()

logFile = open('clearlog.txt', 'a')
logFile.write('Select complete\n')
logFile.close()

if clear == "True" and cur.rowcount != 0:
    logFile = open('clearlog.txt', 'a')
    logFile.write('if entered\n')
    logFile.close()
    uuidstr = uuid[0]
    logFile = open('clearlog.txt', 'a')
    logFile.write(str(uuidstr) + "\n")
    logFile.close()
    queryString = "DELETE FROM Pictures WHERE uuid=" + str(uuidstr)
    logFile = open('clearlog.txt', 'a')
    logFile.write('querystring formed\n')
    logFile.close()
    cur.execute(queryString);
    logFile = open('clearlog.txt', 'a')
    logFile.write('execute\n')
    logFile.close()
    db.commit()
    logFile = open('clearlog.txt', 'a')
    logFile.write('db.commit\n')
    logFile.close()
    picsDirectoryName = str(uuidstr) + "/pics/"
    if not os.path.exists(picsDirectoryName):
        os.makedirs(picsDirectoryName)
    file_names = sorted((fn for fn in os.listdir(picsDirectoryName) if fn.endswith('.jpg')))
    for filename in file_names:
        os.remove(picsDirectoryName + filename)
    gifDirectoryName = str(uuidstr) + "/gif/"
    if not os.path.exists(gifDirectoryName):
        os.makedirs(gifDirectoryName)
    file_names = sorted((fn for fn in os.listdir(gifDirectoryName) if fn.endswith('.gif')))
    for filename in file_names:
        os.remove(gifDirectoryName + filename)

logFile = open('clearlog.txt', 'a')
logFile.write('Done\n')
logFile.close()




