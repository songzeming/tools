#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

building_list = [
    ["400000", "指挥中心", "BuildingCenter"],
    ["401000", "物资交易所", "BuildingTransferStation"],
    ["402000", "联盟大厦", "BuildingUnionBuilding"],
    ["403000", "科研中心", "BuildingScience"],
    ["404000", "物资仓库", "BuildingVault"],
    ["407000", "联合指挥部", "BuildingJointCommand"],
    ["411000", "战区医院", "BuildingHospital"],
    ["412000", "稀土工厂", "BuildingStone"],
    ["413000", "钢铁厂", "BuildingWood"],
    ["414000", "炼制工厂", "BuildingIron"],
    ["415000", "食品厂", "BuildingFood"],
    ["416000", "安保工厂", "BuildingSecurityFactory"],
    ["417000", "雷达", "BuildingRadar"],
    ["419000", "城墙", "BuildingWall"],
    ["423000", "坦克工厂(步)", "BuildingTankFactory"],
    ["424000", "战车工厂(骑)", "BuildingWarFactory"],
    ["425000", "直升机工厂(弓)", "BuildingHelicopterFactory"],
    ["426000", "重型载具工厂(车)", "BuildingVehicleFactory"],
    ["428000", "军需站", "BuildingMilitarySupply"],
    ["431000", "零件装配厂", "BuildingMarchTent"],
    ["432000", "阅兵广场", "BuildingParadeSquare"],
    ["433000", "特价商城", "BuildingSpecialMall"],
    ["444000", "装备制造厂", "BuildingEquipFactory"],
    ["452000", "强化药剂资源建筑", "BuildingDrug"],
    ["453000", "遗迹探索（三消入口）", "BuildingExplore"],
    ["454000", "废墟（爬塔入口）", "BuildingChallenge"],
    ["455000", "广播电台（在线奖励入口）", "BuildingRadio"],
    ["456000", "竞技场（入口）", "BuilldingArena"],
    ["457000", "矿洞（抢矿入口）", "BuildingOccupyMine"],
    ["458000", "银行", "BuildingBank"],
    ["459000", "英雄酒馆(招募入口）", "BuildingRecruit"],
    ["460000", "战略武器部(入口）", "BuildingSuperWeapon"],
    ["461000", "巨兽巢穴（EVA入口）", "BuildingSuperBeast"],
    ["462000", "GM入口", "BuildingGM"],
]

for building in building_list:
    print("")
    print("---is{field} {name}({id})".format(field=building[2], name=building[1], id=building[0]))
    print("function building_type:is{field}()".format(field=building[2]))
    print("    return self.confId == Global.{field}".format(field=building[2]))
    print("end")