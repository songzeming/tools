#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import shutil

hot_update_path = "../../jenkins/workspace/p601_release/HotUpdate/"
dirs = os.listdir(hot_update_path)

shutil.rmtree("diff_folder/new", ignore_errors=True)
shutil.copytree("{path}/{version}/Bundles/".format(path=hot_update_path, version=dirs[0]), "diff_folder/new/")