#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time    : 2018/4/9 12:00
# @Author  : scrum
# @Email   : 718944679@qq.com
# @File    : login_locators.py
# @Software: PyCharm

from selenium.webdriver.common.by import By


class LoginLocator:
    error_msg_locator = (By.XPATH, "//div[@class='form-error-info']")
    unvalidate_msg_locator = (By.XPATH,'//div[@class="layui-layer-content"]')
    mobile_element_locator = (By.NAME, 'phone')
    password_element_locator = (By.NAME, 'password')
    confirm_button_locator = (By.CSS_SELECTOR, "button.btn-special")



