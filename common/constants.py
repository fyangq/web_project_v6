#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time    : 2018/4/9 12:00
# @Author  : scrum
# @Email   : 718944679@qq.com
# @File    : constants.py
# @Software: PyCharm

import os

# 获取项目根路径

# root_path = os.path.abspath(__file__)
# two_path =os.path.dirname(root_path)
# three_path = os.path.dirname(two_path)
r1= os.path.abspath(__file__)
print(r1)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
# 获取测试数据datas所在目录的绝对路径
DATAS_DIR = os.path.join(BASE_DIR,'datas')


# 获取配置文件configs所在目录的路径
CONFIGS_DIR = os.path.join(BASE_DIR,'configs')
CONFIG_FILE_PATH = os.path.join(CONFIGS_DIR,'test.conf')


# 获取日志文件logs所在目录的路径
LOGS_DIR = os.path.join(BASE_DIR,'logs')

# 获取报告文件reports所在目录的路径
REPORTS_DIR = os.path.join(BASE_DIR,'reports')


# 获取截图文件夹路径
screen_DIR = os.path.join(BASE_DIR,'screenshots')

