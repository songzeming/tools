#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import hashlib

filesnew = {}
filesold = {}
filelist = {}
diffsize = 0

def turn_mb(b):
    return round(b / 1024 / 1024, 2)
 
def getmd5(file):
    m = hashlib.md5()
    with open(file,'rb') as f:
        for line in f:
            m.update(line)
    md5code = m.hexdigest()
    return md5code

def insert_files(file, t):
    if t == "new":
        filesnew[os.path.basename(file)] = file
    else:
        filesold[os.path.basename(file)] = file

def find_file(path, t):
	dirs = os.listdir(path)
	for i in range(0, len(dirs)):
		file = os.path.join(path, dirs[i])
		if os.path.isdir(file):
			find_file(file, t)
		elif os.path.isfile(file):
			insert_files(file, t)

find_file("./old", "old")
find_file("./new", "new")

def calculate(name, file, desc):
    filesize = os.path.getsize(file)
    filefullname = os.path.dirname(file)
    filesplit = filefullname.split('/')
    if len(filesplit) > 5:
        filesplit5 = filesplit[5]
        if filesplit5 != None or filesplit5 != "":
            if filelist.get(filesplit5, None) == None:
                filelist[filesplit5] = 0
            filelist[filesplit5] += filesize
    fileshortname = filefullname.replace('./new/1.1/Bundles/Android', '')
    print('%-32s%-8s%-6s%-6s%-20s' %(fileshortname, desc, turn_mb(filesize), "MB", name))
    return filesize

for name, file in filesnew.items():
    if filesold.get(name, None) != None:
        if getmd5(file) != getmd5(filesold[name]):
            diffsize += calculate(name, file, "add")
    else:
        diffsize += calculate(name, file, "diff")

print("")
    
for name, size in filelist.items():
    print('%-20s%-6s%-6s' %(name, turn_mb(size), "MB"))
    
print("")
print("热更大小:", diffsize, "B")
print("热更大小:", turn_mb(diffsize), "MB")