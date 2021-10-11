#!/usr/bin/python
# -*- coding: UTF-8 -*-

import shutil

shutil.rmtree("new/", ignore_errors=True)
shutil.copytree("../../client_online/HotUpdate/", "new/")

shutil.rmtree("old/", ignore_errors=True)
shutil.copytree("../../client_online/HotUpdate/", "old/")