#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import time

# 将config: develop -> release
print("将config: develop -> release")
os.system("cd ../../config/release && rm -rf excels && cd .. && cp -R develop/excels release/excels")
os.system("cd ../../config/release && svn add . --force && svn commit -m 'auto: config develop to release'")

# 上传三消校验代码
print("上传三消校验代码")
os.system("cd ../../client_online/Generator/PuzzleVerify && git pull")
os.system("cd ../../client_online && make puzzle_verify")
os.system("cd ../../client_online/Generator/PuzzleVerify && git add . && git commit -m 'auto: 三消校验' && git push")

# 自动备份热更对比文件(git-submodule)
print("自动备份热更对比文件")
os.system("cd ../diff_hot_update/diff_folder && git add . && git commit -m 'auto: 发版本热更文件备份'")

# 设置tag并推送到远端
print("设置tag并推送到远端")
time_nyr = time.strftime("%Y%m%d", time.localtime())
os.system("cd ../../client_online && git tag v{version} && git push origin v{version}".format(version=time_nyr))

print("线上备份完成")
