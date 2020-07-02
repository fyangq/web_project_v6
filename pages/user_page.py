#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time    : 2018/4/9 12:00
# @Author  : scrum
# @Email   : 718944679@qq.com
# @File    : user_page.py
# @Software: PyCharm


from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage


class UserPage(BasePage):
    available_money_locator=(By.XPATH,"//li[@class='color_sub']")


    @property
    def available_money_element(self)->WebElement:
        return self.wait_visable_element(self.available_money_locator)

    def get_avaiable_money(self):
        "获取可用余额"
        available_money = self.available_money_element.text
        save_money = eval(available_money.strip("元"))
        save_money = round(save_money, 2)
        return save_money



