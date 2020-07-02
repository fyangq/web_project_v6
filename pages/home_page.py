#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time    : 2018/4/9 12:00
# @Author  : scrum
# @Email   : 718944679@qq.com
# @File    : home_page.py
# @Software: PyCharm

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from pages.base_page import BasePage


class HomePage(BasePage):
    home_url = 'http://120.78.128.25:8765/Index/index'
    # 抢投标按钮定位
    bid_locator = (By.XPATH, '//a[@class="btn btn-special"]')
    user_nickname_locator =(By.XPATH, '//a[@href="/Member/index.html"]')

    def get(self):
        return self.driver.get(self.home_url)

    @property
    def user_element(self):
        """定位我的账户"""
        return self.wait_presence_element((By.XPATH,"//a[@href='/Member/index.html']"))


    @property
    def bid_button(self) -> WebElement:
        "首页抢投标按钮"
        return self.wait_visable_element(self.bid_locator)

    def click_bid_button(self):
        "首页点击抢投标"
        return self.bid_button.click()



