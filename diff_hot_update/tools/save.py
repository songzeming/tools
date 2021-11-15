#!/usr/bin/python
# -*- coding: UTF-8 -*-

import shutil

shutil.rmtree("diff_folder/new/", ignore_errors=True)
shutil.copytree("../../client_online/HotUpdate/", "diff_folder/new/")

shutil.rmtree("diff_folder/old/", ignore_errors=True)
shutil.copytree("../../client_online/HotUpdate/", "diff_folder/old/")