#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import hashlib

filesnew = {}
filesold = {}
filelist = {}
diffsize = 0
dynamicsize = 0


def turn_mb(b):
    return round(b / 1024 / 1024, 2)


def getmd5(file):
    m = hashlib.md5()
    with open(file, 'rb') as f:
        for line in f:
            m.update(line)
    md5code = m.hexdigest()
    return md5code


def insert_files(file, t):
    if t == "diff_folder/new":
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


find_file("./diff_folder/old", "diff_folder/old")
find_file("./diff_folder/new", "diff_folder/new")


def calculate(name, file, desc):
    filesize = os.path.getsize(file)
    filefullname = os.path.dirname(file)
    filesplit = filefullname.split('/')
    if len(filesplit) > 4:
        filesplit5 = filesplit[4]
        if filesplit5 != None or filesplit5 != "":
            if filelist.get(filesplit5, None) == None:
                filelist[filesplit5] = 0
            filelist[filesplit5] += filesize
    fileshortname = filefullname.replace('./diff_folder/new/Android', '')
    print('%-35s%-8s%-6s%-6s%-20s' % (fileshortname, desc, turn_mb(filesize), "MB", name))
    return filesize, fileshortname.startswith("/dynamicres")


for name, file in filesnew.items():
    if filesold.get(name, None) != None:
        if getmd5(file) != getmd5(filesold[name]):
            f_size, f_dynamic = calculate(name, file, "add")
            if f_dynamic:
                dynamicsize += f_size
            else:
                diffsize += f_size
    else:
        f_size, f_dynamic = calculate(name, file, "diff")
        if f_dynamic:
            dynamicsize += f_size
        else:
            diffsize += f_size


print("")
for name, size in filelist.items():
    print('%-20s%-6s%-6s' % (name, turn_mb(size), "MB"))


print("")
strdiffsize = str(turn_mb(diffsize)) + "MB"
strdyanmicsize = str(turn_mb(dynamicsize)) + "MB"
strtotalsize = str(turn_mb(diffsize + dynamicsize)) + "MB"
print("热更大小: " + strtotalsize + "（热更新: " + strdiffsize + "，动态资源: " + strdyanmicsize + "）")