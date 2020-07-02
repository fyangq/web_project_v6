#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time    : 2018/4/9 12:00
# @Author  : scrum
# @Email   : 718944679@qq.com
# @File    : test_login.py
# @Software: PyCharm
import unittest

import allure,pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.home_page import HomePage
from ddt import ddt,data
from datas.login_data import user_info_unregister,user_info_error,user_common_info

# @pytest.fixture()
# def init_web():
#     driver = webdriver.Chrome()
#     driver.implicitly_wait(20)
#     driver.maximize_window()
#     login_page = LoginPage(driver)
#     yield driver,login_page


# @ddt

class TestLogin():

    # def setUpClass(self,init_web):
    #      self.driver, self.login_page = init_web
    # #
    # #
    # # @classmethod
    # # def tearDownClass(self):
    # #      self.driver.quit()
    #
    # def setUp(self):
    #     self.driver.refresh()

    # @allure.mark.login
    # @data(*user_info_error)

    @allure.feature('测试登录功能异常1')  # feature定义功能
    @pytest.mark.parametrize("user_data",user_info_error)
    def test_login_01_error(self,user_data,init_login):
        """测试登录功能异常。
        步骤：
        1、启动浏览器，进入登录页面；
        2、元素定位用户名和密码；
        3、发送用户名和密码(测试数据)；
        4、点击登录按钮
        5、断言

        1、登录  login()
        2、获取实际结果, actual = get_actual_result()
        3、断言  self.assertEqual(actual, expected)
        """
        driver,login_page=init_login
        login_page.login(user_data['username'],user_data['password'])
        error_msg_element = login_page.get_actual_result()
        assert(error_msg_element.text, user_data['e_msg'])
        driver.refresh()

    # # @data(*user_info_unregister)
    # @allure.feature('测试未注册用户登录')
    # @pytest.mark.parametrize("user_info",user_info_unregister)
    # def test_login_02_unregister(self, user_info,init_web):
    #     driver, login_page = init_web
    #     login_page.login(user_info['username'], user_info['password'])
    #     error_msg_element = login_page.get_unvalidte_result()
    #     assert(error_msg_element.text, user_info['e_msg'])
    # #
    # # #
    # @allure.feature('测试已注册用户登录')
    # @pytest.mark.login
    # def test_login_03_success(self,init_web):
    #     driver, login_page = init_web
    #     login_page.login(user_common_info['username'],user_common_info['password'])
    #     user_element = HomePage(driver).user_element
    #     assert(user_element.text,'我的帐户[scrum19]')


if __name__ == '__main__':
    pytest.main(['-s',"test_login.py"])
    # pytest.main(['--allure_stories=test_login', '--allure_severities=critical, blocker'])
    # pytest.main(["-s", "test_login.py","--alluredir", "../report"])