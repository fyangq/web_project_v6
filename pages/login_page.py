#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time    : 2018/4/9 12:00
# @Author  : scrum
# @Email   : 718944679@qq.com
# @File    : login_page.py
# @Software: PyCharm


from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from pages.locators.login_locators import LoginLocator
from pages.base_page import BasePage

class LoginPage(BasePage):
    login_url = 'http://120.78.128.25:8765/Index/login.html'

    def get_actual_result(self):
        """获取实际结果"""
        return self.driver.find_element(*LoginLocator.error_msg_locator)

    def get_unvalidte_result(self):
        """获取授权错误信息需要等待"""
        return self.wait_visable_element(LoginLocator.unvalidate_msg_locator)

    def login(self,username,password):
        self.driver.get(self.login_url)
        # 显示等待
        user_element =self.user_elem
        pwd_element =self.pwd_elem
        user_element.send_keys(username)
        pwd_element.send_keys(password)

        e =self.wait_presence_element(LoginLocator.confirm_button_locator)
        e.click()
        e


    @property
    def user_elem(self) -> WebElement:
        """定位用户名输入框"""
        return self.wait_presence_element(LoginLocator.mobile_element_locator)
    @property
    def pwd_elem(self) -> WebElement:
        """定位用户名输入框"""
        return self.wait_presence_element(LoginLocator.password_element_locator)

# 多个不同的函数都共用一些形式参数参数，共享的实际参数---形参--封装成一个类
