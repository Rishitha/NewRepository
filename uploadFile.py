#!/usr/bin/env python
import cgi, os
import cgitb; cgitb.enable()
import sys
sys.path.append('\Python27\Scripts')

from images2gif import writeGif
from PIL import Image

import MySQLdb as mdb

logFile = open('log.txt', 'a')
logFile.write('ReceivedPost!!!\n')
logFile.close()

try: # Windows needs stdio set for binary mode.
    import msvcrt
    msvcrt.setmode (0, os.O_BINARY) # stdin  = 0
    msvcrt.setmode (1, os.O_BINARY) # stdout = 1
except ImportError:
    pass

#Connect to the DB
db = mdb.connect(host = "eecs394db.cfcbispllbb4.us-east-1.rds.amazonaws.com",
                       user = "mrmarkwell",
                       passwd = "qwertyuiop",
                       db = "bluedb")

cur = db.cursor()

logFile = open('log.txt', 'a')
logFile.write('Connected DB\n')
#for theChar in sys.stdin.read(1):
#    logFile.write(theChar)
#logFile.close()

#obtain the parameters from the POST
form = cgi.FieldStorage()

posttype = form['post_type'].value
if (posttype == 'image'):
    username = form['username'].value
    #username = 'user1'
    password = form['password'].value
    #password = 'password1'

    fileitem = form['file']

    logFile = open('log.txt', 'a')
    logFile.write(username + ' ' + password + '\n')
    logFile.close()

    queryString = "SELECT uuid FROM users WHERE username='" + username + "' AND password='" + password + "'"
    cur.execute(queryString);

    logFile = open('log.txt', 'a')
    logFile.write('DB execute\n')
    logFile.close()


    if cur.rowcount != 0:
        logFile = open('log.txt', 'a')
        logFile.write('Inside if\n')
        logFile.close()
        uuid = cur.fetchone()
        uuidstr = uuid[0]
        logFile = open('log.txt', 'a')
        logFile.write(str(uuidstr) + '\n')
        logFile.close()

        queryString = "SELECT MAX(pid) FROM pictures NATURAL JOIN users WHERE uuid='" + str(uuidstr) + "'"
        cur.execute(queryString);
        pid = cur.fetchone()
        if pid[0]:
            newPid = pid[0]+1
        else:
            newPid = 1

        logFile = open('log.txt', 'a')
        logFile.write(str(newPid) + '\n')
        logFile.close()
        queryString = "INSERT INTO pictures (uuid, pid, uuid_pid) values ('"+str(uuidstr)+"', '"+str(newPid)+"', '"+str(uuidstr)+"_"+str(newPid)+"')"
        logFile = open('log.txt', 'a')
        logFile.write(queryString + '\n')
        logFile.close()
        cur.execute(queryString);
        db.commit()

        picsDirectoryName = str(uuidstr) + '/pics/'
        logFile = open('log.txt', 'a')
        logFile.write(picsDirectoryName + '\n')
        logFile.close()
        if not os.path.exists(picsDirectoryName):
            os.makedirs(picsDirectoryName)
        logFile = open('log.txt', 'a')
        logFile.write('hi' + '\n')
        logFile.close()
        #if fileitem.filename:
        fn = str(uuidstr) + '_' + str(newPid) + '.jpg'
        logFile = open('log.txt', 'a')
        logFile.write(fn + '\n')
        logFile.close()
        uploadedFile = open(picsDirectoryName + fn, 'wb')
        uploadedFile.write(fileitem.file.read())
        uploadedFile.close()

        logFile = open('log.txt', 'a')
        logFile.write('PostIf\n')
        logFile.close()

        gifDirectoryName = str(uuidstr) + '/gif/'
        if not os.path.exists(gifDirectoryName):
            os.makedirs(gifDirectoryName)
        file_names = sorted((fn for fn in os.listdir(picsDirectoryName) if fn.endswith('.jpg')))
        #['animationframa.png', 'animationframb.png', 'animationframc.png', ...] "

        images = [Image.open(picsDirectoryName + fn) for fn in file_names]

        #print writeGif.__doc__
        # writeGif(filename, images, duration=0.1, loops=0, dither=1)
        #    Write an animated gif from the specified images.
        #    images should be a list of numpy arrays of PIL images.
        #    Numpy images of type float should have pixels between 0 and 1.
        #    Numpy images of other types are expected to have values between 0 and 255.

        querystring = "SELECT gifSpeed FROM users WHERE username='" + username + "' AND password='" + password + "'"
				cur.execute(queryString)

				tmp_speed = cur.fetchone()
				if tmp_speed[0]:
				    speed = tmp_speed[0]
				else:
				    speed = 0.2  # default

        filename = gifDirectoryName + str(uuidstr) + ".gif"
        writeGif(filename, images, speed)

        print filename
         #make a gif with pictures /uuid/pics/1.jpg to /uuid/pics/pid.jpg and store it at /uuid/gifs/uuid.gif

elif posttype == 'speed':
    speed = form['gifSpeed'].value
    username = form['username'].value
    password = form['password'].value

    queryString = "SELECT uuid FROM users WHERE username='" + username + "' AND password='" + password + "'"
    uuid = cur.execute(queryString);
    uuidstr = uuid[0]

    gifDirectoryName = str(uuidstr) + '/gif/'
    if not os.path.exists(gifDirectoryName):
        os.makedirs(gifDirectoryName)

		filename = gifDirectoryName + str(uuidstr) + ".gif"

		images = [Image.open(picsDirectoryName + fn) for fn in file_names]

		# speed of .gif, set it in db
    queryString = "UPDATE users SET gifSpeed='" + Double.toString(speed) + "' WHERE username ='" + username +"'"
    cur.execute(queryString)
    db.commit()

		writeGif(filename, images, speed)

		print filename


