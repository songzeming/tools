#!/usr/bin/python
# -*- coding: UTF-8 -*-

import shutil
import os
import time

# 创建文件夹
time_nyr = time.strftime("%Y%m%d", time.localtime())
filename_origin = "线上版本备份" + time_nyr
filename = "../../" + filename_origin
shutil.rmtree(filename, ignore_errors=True)
os.mkdir(filename)

# 拷贝aab和apk文件
root_dir = "/Users/xiaoze/Work/P601/client_online/build/releases/Android"
list = os.listdir(root_dir)
for i in range(0, len(list)):
    filepath = os.path.join(root_dir, list[i])
    if filepath.endswith(".aab"):
        filename_base = os.path.basename(filepath)
        filename_pre = filename_base.split('.')[0]
        shutil.copy(filepath, filename)
        print("备份aab成功")
        filename_apk = os.path.join(root_dir, "puzzles/standalones/" + filename_pre + ".apk")
        print("filename_apk: ", filename_apk)
        shutil.copy(filename_apk, filename)
        print("备份apk成功")

# 更新svn
up_list = {"config", "FairyGUI", "DynamicRes"}
for u_name in up_list:
    os.system("cd ../../{file} && svn up".format(file=u_name))

# 压缩config、FairyGUI、DynamicRes文件
z_list = {"config", "FairyGUI", "DynamicRes"}
for z_name in z_list:
    os.system("echo '正在压缩{file}' && zip -q -r -o '{path}/{file}.zip' ../../{file}".format(file=z_name, path=filename))

# 压缩HotUpdate，备份热更文件
os.system("echo '正在压缩HotUpdate' && cd ../../client_online && zip -q -r -o '../{path}/HotUpdate.zip' HotUpdate".format(path=filename_origin))

# 备份Bundles
os.system("echo '备份Bundles' && cd ../../client_online && zip -q -r -o '../{path}/Production.zip' Product".format(path=filename_origin))

print("备份完成\n")
