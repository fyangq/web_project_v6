#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time    : 2018/4/9 12:00
# @Author  : scrum
# @Email   : 718944679@qq.com
# @File    : conftest.py.py
# @Software: PyCharm
import pytest
import allure
from selenium import webdriver

from datas.login_data import user_common_info
from pages.home_page import HomePage
from pages.login_page import LoginPage

@pytest.fixture(scope='class')
def init_login():
    driver= webdriver.Chrome()
    driver.implicitly_wait(15)
    driver.maximize_window()
    login_page=LoginPage(driver)
    yield driver,login_page
    driver.quit()

# @pytest.fixture(scope='class')
# def init_web():
#     driver = webdriver.Chrome()
#     driver.implicitly_wait(20)
#     driver.maximize_window()
#     login_page = LoginPage(driver)
#     yield driver,login_page
#     driver.quit()

#
@pytest.fixture(scope='class')
def init_bid():
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    driver.maximize_window()
    login_page = LoginPage(driver)
    login_page.login(user_common_info['username'], user_common_info['password'])
    home_page = HomePage(driver)
    home_page.get()
    home_page.click_bid_button()
    yield driver, login_page,home_page
    driver.quit()

