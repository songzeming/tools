#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import time

# 设置tag并推送到远端
print("设置tag并推送到远端")
time_nyr = time.strftime("%Y%m%d", time.localtime())
os.system("cd ../../client_online && git tag v{version} && git push origin v{version}".format(version=time_nyr))