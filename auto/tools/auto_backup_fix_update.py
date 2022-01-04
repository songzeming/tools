#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import time

# 创建文件夹
time_nyr = time.strftime("%Y%m%d", time.localtime())
filename_origin = "线上版本备份" + time_nyr
filename = "../../" + filename_origin
os.mkdir(filename)
# 备份Bundles
os.system("echo '备份Bundles' && cd ../../client_online && pwd && zip -q -r -o '../{path}/Production.zip' Product".format(path=filename_origin))

# 压缩HotUpdate，备份热更文件
os.system("echo '正在压缩HotUpdate' && cd ../../client_online && zip -q -r -o '../{path}/HotUpdate.zip' HotUpdate".format(path=filename_origin))

# 自动备份热更对比文件(git-submodule)
print("自动备份热更对比文件")
os.system("cd ../diff_hot_update/diff_folder && git add . && git commit -m 'auto: 发热更文件备份'")

# 设置tag并推送到远端
print("设置tag并推送到远端")
os.system("cd ../../client_online && git tag v{version} && git push origin v{version}".format(version=time_nyr))

print("线上备份完成")