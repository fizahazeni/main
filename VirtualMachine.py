import datetime
import subprocess
import platform
from datetime import datetime, timedelta
import csv
import os
import string
import collections
from collections import Counter
import logging

folderpath = os.getenv("HOME") + "/ProfileScript/"

#####LOGGER######
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create a file handler
handler = logging.FileHandler(folderpath + "VM.log/")
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)
#################

#get today's month and year
today = datetime.now() + timedelta(days=0)
month = today.strftime("%m")
year = today.strftime("%Y")
dirName = month + year

directorypath = folderpath + dirName + "/"

#Memoryspace
with open("/proc/meminfo","r") as f:
    lines = f.readlines()

###totalmemory###

exclude = set(string.punctuation) #exclude punctuations

totalmem = [lines[0].strip()]
ttl = (str(totalmem)).split(' ')
ttl[9] = ''.join(a for a in ttl[9] if a not in exclude)
tmemcol = []
for i in totalmem:
    tmem = str(today) ,"TOTALMEM",ttl[9],ttl[8]
    tmemcol.append(tmem)

###freememory###
freemem = [lines[1].strip()]
free = (str(freemem)).split(' ')
free[11] = ''.join(a for a in free[11] if a not in exclude)
fmemcol = []
for i in freemem:
    fmem = str(today), "AVAILMEM",free[11],free[10]
    fmemcol.append(fmem)

#userdata
result = subprocess.check_output(['ps','-ef']).decode('utf-8')
userlist = [] 

for line in result.splitlines():
    name = line.split()[0]
    link = line.split()[7]
    if "sshd" in link and name != "root":
        userlist.append(name)

#users
setlist = list(set(userlist))
namecol = []
if len(userlist)>=1:
    for i in setlist:
        users = str(today) , "USERS", i,userlist.count(i)
        namecol.append(users)
    logger.info("There are " + str(len(setlist)) + " users online in VM now.")
else:
    users = str(today) , "USERS","No users online",0
    namecol.append(users)
    logger.info("There are no users online in VM now.")

#make new directory if dont exist
try:
    os.makedirs( directorypath )
    logger.info("File has been created to new path: " + directorypath)
except:
    logger.info("File has been updated to existing path: " + directorypath)

    
#export data to csv file if there is data ONLY

##header##
header = "Datetime","Category","Unit","Value"

filename =os.path.join( folderpath , dirName , "VM Profile Script v1.csv" )



with open(filename,'a') as myfile:
   writer = csv.writer(myfile,quoting = csv.QUOTE_ALL)
   file_is_empty = os.stat(filename).st_size == 0
   if file_is_empty:
       writer.writerow(header)
   for row in namecol:
       writer.writerow(row)
   for row in tmemcol:
       writer.writerow(row)
   for row in fmemcol:
       writer.writerow(row)
       
       
       
       
