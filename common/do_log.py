#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time    : 2018/4/9 12:00
# @Author  : scrum
# @Email   : 718944679@qq.com
# @File    : do_log.py
# @Software: PyCharm

import os
from common.do_config import cfg
import logging
from common.constants import LOGS_DIR


class HandleLog:
    """
    日志文件类

    """
    def __init__(self):
        self.case_logger = logging.getLogger(cfg.get_values("log", "logger_name"))
        self.case_logger.setLevel(cfg.get_values("log", "logger_level"))

        console_handle = logging.StreamHandler()
        # 输出到日志文件
        file_handle = logging.FileHandler(os.path.join(LOGS_DIR,cfg.get_values("log", "log_filename")), encoding="utf-8")

        # 指定日志输出渠道的日志等级
        console_handle.setLevel(cfg.get_values("log", "console_level"))
        file_handle.setLevel(cfg.get_values("log", "file_level"))

        # 定义日志显示的格式
        simple_formatter = logging.Formatter(cfg.get_values("log", "simple_formatter"))
        verbose_formatter = logging.Formatter(cfg.get_values("log", "verbose_formatter"))

        console_handle.setFormatter(simple_formatter)
        file_handle.setFormatter(verbose_formatter)

        # 将日志收集器与输出渠道进行对接
        self.case_logger.addHandler(console_handle)
        self.case_logger.addHandler(file_handle)

    def get_logger(self):
        """

        :return:
        """
        return self.case_logger


logger = HandleLog().get_logger()


if __name__ == '__main__':
    case_logger = HandleLog().get_logger()
    case_logger.info("this is info")
    case_logger.debug("this is debug")
    case_logger.error("this is error")
    case_logger.warning("this is warning")