#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

# 解压aab文件
root_dir = "/Users/xiaoze/Work/P601/client_online/build/releases/Android"
aab_path = "../../client_online/build/releases/Android/"
apk_dir = "/Users/xiaoze/Work/P601/client_online/build/releases/Android/puzzles/standalones"
apk_path = "../../client_online/build/releases/Android/puzzles/standalones/"
list = os.listdir(root_dir)

print("删除非abb相关文件")
for i in range(0, len(list)):
    rm_filepath = os.path.join(root_dir, list[i])
    if not rm_filepath.endswith(".aab"):
        rm_name = os.path.basename(rm_filepath)
        if os.path.isdir(rm_filepath):
            os.system("cd {path} && rm -rf {name}".format(path=aab_path, name=rm_name))
        elif os.path.isfile(rm_filepath):
            os.system("cd {path} && rm {name}".format(path=aab_path, name=rm_name))

for i in range(0, len(list)):
    filepath = os.path.join(root_dir, list[i])
    if filepath.endswith(".aab"):
        aab_name = os.path.basename(filepath)
        pre_name = aab_name.split('.')[0]
        print("aab_name: " + aab_name)
        print("正在解压缩aab文件")
        os.system("cd {path} && bundletool build-apks --bundle=./{name} {apks} {keystore} {alias} {password}".format(
            path=aab_path,
            name=aab_name,
            apks="--output=./puzzles.apks",
            keystore="--ks=/Users/xiaoze/Work/P601/client/jks/key.keystore",
            alias="--ks-key-alias=puzzles",
            password="--ks-pass=pass:12345678"
        ))
        print("正在解压缩apks文件")
        os.system("cd {path} && mv {apks}.apks {apks}.zip && unzip -q {apks} -d {apks}".format(
            path=aab_path,
            apks="puzzles"
        ))
        print("正在改名v7a.apk")
        sub_list = os.listdir(apk_dir)
        for j in range(0, len(sub_list)):
            sub_filepath = os.path.join(apk_dir, sub_list[j])
            if sub_filepath.endswith("v7a.apk"):
                apk_name = os.path.basename(sub_filepath)
                os.system("cd {path} && mv {apk} {aab}.apk".format(
                    path=apk_path,
                    apk=apk_name,
                    aab=pre_name
                ))
                break
        break

os.system("open {path}".format(path=apk_path))
print("完成")
