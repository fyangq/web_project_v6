#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time    : 2018/4/9 12:00
# @Author  : scrum
# @Email   : 718944679@qq.com
# @File    : do_config.py
# @Software: PyCharm


from configparser import ConfigParser

from common.constants import CONFIG_FILE_PATH


class HandleConfig:
    """
    创建配置文件类
    """
    def __init__(self,filename=None):
        self.filename = filename
        self.config = ConfigParser()
        self.config.read(self.filename,encoding='utf-8')

    def get_values(self,section,option):
        """

        :param section:
        :param option:
        :return:
        """
        return self.config.get(section,option)

    def get_int(self,section,option):
        return self.config.getint(section,option)

    def get_float(self,section,option):
        return self.config.getfloat(section,option)

    def get_boolean(self,section,option):
        return self.config.getfloat(section,option)

    def get_eval_value(self,section,option):
        return eval(self.get_values(section,option))

    @staticmethod
    def write_config(data,filename,cfg_section):
        """

        :param data: #字典
        :param write_name: 写入的配置文件名字
        :return:
        """
        config = ConfigParser()
        config[cfg_section]= data
        with open(filename, 'a+') as file:
            config.write(file)
    @staticmethod
    def  write_config_new(datas,filename):
        config = ConfigParser()
        for key in datas:
            config[key] =datas[key]
        with open(filename,'w')as file:
            config.write(file)
    def remove_section(self,section):
        """
        移除对应的section
        :param section:
        :return:
        """
        self.config.remove_section(section)
        self.config.write(open(CONFIG_FILE_PATH, "w",encoding='utf-8'))


cfg = HandleConfig(CONFIG_FILE_PATH)

if __name__ == '__main__':
    config = HandleConfig(CONFIG_FILE_PATH)
    print(config.get_int("excel","actual_column"))
    result = {'id':'96824','mobilephone':'15959287436'}
    config.write_config(result,CONFIG_FILE_PATH,'admin')
