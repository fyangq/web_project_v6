#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time    : 2018/4/9 12:00
# @Author  : scrum
# @Email   : 718944679@qq.com
# @File    : base_page.py
# @Software: PyCharm
import time

from gevent import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from common.do_log import logger
from common.constants import screen_DIR


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_presence_element(self, locator):
        """等待元素出现"""
        try:
           return WebDriverWait(self.driver, 20).until(ec.presence_of_element_located(locator))
        except Exception as e:
            logger.error("定位{}出错了,错误是{}".format(locator, e))
            self.save_screenshot()

    def wait_visable_element(self,locator):
        """等待元素可见"""
        try:
           return WebDriverWait(self.driver,20).until(ec.visibility_of_element_located(locator))
        except Exception as e:
            logger.error("定位{}出错了,错误是{}".format(locator, e))
            self.save_screenshot()

    def wait_click_element(self, locator):
        """等待按钮可点击,返回一个WebElement对象，如果没有找到就报错"""
        try:
           return  WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(locator))
        except Exception as e:
            logger.error("定位{}出错了,错误是{}".format(locator,e))
            self.save_screenshot()


    def save_screenshot(self):
        "自动截图保存"
        # file_name = self.file_name()
        # file_path= os.path.join(screen_DIR,file_name)
        # self.driver.save_screenshot(r'{}'.format(file_path))
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        filepath = "screen_{}.png".format(now)

        self.driver.save_screenshot(screen_DIR + "/" + filepath)




