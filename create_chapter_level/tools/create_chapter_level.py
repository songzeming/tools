#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import random
import math
import sys
sys.setrecursionlimit(1000000)
global_recursion = 0

#路径
global_path = "/assets/MatchThreeMap/ItemLevelDetails/"
#章节
global_chapter = 24
#关卡数量
global_level = 9
#生成组件名称
global_name = "ItemLevelDetails" + str(global_chapter)
#生成组件大小
component_width = 750
component_height = 1334
#组件引用
link_id = "n0_cqbq"
link_name = "Level"
link_src = "qhhj3y"
link_filename = "item/itemMatchthreepoint.xml"
link_pkg = "w4z0v1wf"
link_scale = 1.2
link_point_id = "n4_cqbq"
link_point_name = "dian"
link_point_src = "xa0c8m"
link_point_filename = "item/itemMatchthreesmallpoint.xml"
link_point_pkg = "w4z0v1wf"
link_point_scale = 0.8
#生成关卡位置限制
limit_left = 150
limit_right = 600
limit_up = 320
limit_down = 1100
limit_first_offset_x = 100
limit_first_random_y = {"min": 900, "max": 1100}
#关卡位置
global_pos = []
#两点之间距离
distance_level = 150
#关卡按钮大小
global_btn_level_size = {"width": 118, "height": 124}

#已知两点之间的距离和p1的xy坐标以及p2的x坐标, 求p2的y坐标(取整,返回两种情况)
def get_point_y(disance, p1, p2x):
	sign_y = math.sqrt(abs(math.pow(disance, 2) - math.pow(p1["x"] - p2x, 2)))
	return math.floor(p1["y"] - sign_y), math.floor(sign_y + p1["y"])

#获取两点之间的距离
def get_distance(p1, p2):
	return math.sqrt(math.pow(p1["x"] - p2["x"], 2) + math.pow(p1["y"] - p2["y"], 2))

#获取xml缩进
def get_xml_indent(count):
	return "  " * count

#生成关卡组件的位置(随机)
def create_level_pos(index):
	global global_recursion
	random_x = 0
	random_y = 0
	dirX = 1
	dirY = 1
	if index == 1:
		#随机x坐标
		random_x = random.randint(limit_left + limit_first_offset_x, limit_right - limit_first_offset_x)
		dirX = random.randint(0, 1) == 0 and -1 or 1

		#第一个随机点y坐标限制
		random_y = random.randint(limit_first_random_y["min"], limit_first_random_y["max"])
	else:
		#上一个点的坐标
		last_level_pos = global_pos[index - 1 - 1]
		
		#非第一个随机点x坐标限制
		random_x = random.randint(-distance_level, distance_level)
		final_x = last_level_pos["x"] + random_x
		if final_x < limit_left or final_x > limit_right:
			final_x = last_level_pos["x"] - random_x
			dirX = -1 * dirX
		random_x = final_x
		
		#随机y坐标
		random_y1, random_y2 = get_point_y(distance_level, last_level_pos, random_x)
		random_y = random_y1
		if random_y1 > limit_down or random_y1 < limit_up:
			random_y = random_y2
			dirY = -1 * dirY
		for obj in global_pos:
			if get_distance(obj, {"x": random_x, "y": random_y}) < distance_level:
				global_recursion = global_recursion + 1
				if global_recursion > 10000:
					return False
				return create_level_pos(index)

	global_pos.insert(index, {"x": random_x, "y": random_y, "dirX": dirX, "dirY": dirY})
	return True

#生成关卡点的位置
def create_point_pos(index, sub_index):
	level_pos1 = global_pos[index - 1]
	level_pos2 = global_pos[index]
	level_diff_x = level_pos2["x"] - level_pos1["x"]
	level_diff_y = level_pos2["y"] - level_pos1["y"]
	point_x = level_pos1["x"] + level_diff_x * (sub_index + 1) / 6
	point_y = level_pos1["y"] + level_diff_y * (sub_index + 1) / 6
	
	return point_x, point_y

#生成章节关卡信息(随机)
def create_chapter_info():
	print("开始生成章节关卡信息")
	fullpath = os.getcwd() + global_path + global_name + ".xml"
	print(fullpath)
	#打开或者创建关卡文件
	#wb:打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
	file = open(fullpath, "w")
	file.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n")
	file.write("<component size=\"{0},{1}\" opaque=\"false\">\n".format(component_width, component_height))
	file.write(get_xml_indent(1) + "<displayList>\n")

	for i in range(1, global_level + 1):
		isCreateSuccess = create_level_pos(i)
		if not isCreateSuccess:
			print("自动生成地图失败")
			return
		
	#点的数量
	for i in range(1, global_level):
		for j in range(1, 4):
			x, y = create_point_pos(i, j)
			file.write(get_xml_indent(2) + "<component id=\"{0}\" name=\"{1}\" src=\"{2}\" fileName=\"{3}\" pkg=\"{4}\" xy=\"{5},{6}\" scale=\"{7},{8}\"/>\n".format(link_point_id, link_point_name + str((i - 1) * 3 + j), link_point_src, link_point_filename, link_point_pkg, x, y, link_point_scale, link_point_scale))
	#关卡
	for i in range(1, global_level + 1):
		xy = global_pos[i - 1]
		file.write(get_xml_indent(2) + "<component id=\"{0}\" name=\"{1}\" src=\"{2}\" fileName=\"{3}\" pkg=\"{4}\" xy=\"{5},{6}\" pivot=\"0.45,0.35\" anchor=\"true\" scale=\"{7},{8}\">\n".format(link_id, link_name + str(i), link_src, link_filename, link_pkg, xy["x"], xy["y"], link_scale, link_scale))
		file.write(get_xml_indent(3) + "<Button title=\"{0}\"/>\n".format(i))
		file.write(get_xml_indent(2) + "</component>\n")

	file.write(get_xml_indent(1) + "</displayList>\n")
	file.write("</component>")
	file.close()
	print("自动生成地图成功")

#开始执行生成章节信息
create_chapter_info()