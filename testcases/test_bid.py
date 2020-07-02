#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time    : 2018/4/9 12:00
# @Author  : scrum
# @Email   : 718944679@qq.com
# @File    : test_bid.py
# @Software: PyCharm


import time
import unittest

import allure
import pytest
from selenium import webdriver

from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.bid_page import BidPage
from pages.user_page import UserPage

from ddt import ddt,data
from datas.login_data import user_common_info
from datas.bid_data import bid_error_100_data,bid_error_data,bid_success_data





class TestBid():
    # @classmethod
    # def setUpClass(cls):
    #     cls.driver = webdriver.Chrome()
    #     cls.driver.implicitly_wait(20)
    #     cls.driver.maximize_window()
    #     cls.login_page = LoginPage(cls.driver)
    #     cls.login_page.login(user_common_info['username'], user_common_info['password'])
    #     cls.home_page= HomePage(cls.driver)
    #     cls.home_page.get()
    #     cls.home_page.click_bid_button()
    # #
    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()
    # #
    #
    # def tearDown(self):
    #       self.driver.refresh()
    #
    # @data(*bid_error_data)
    @allure.feature('测试投资金额不是10的倍数')
    @pytest.mark.parametrize("error_data_1", bid_error_data)
    def test_bid_01_error(self,error_data_1,init_bid):
        driver,login_page, home_page=init_bid
        bid_page= BidPage(driver)
        bid_page.bid_input.send_keys(error_data_1['money'])
        assert(bid_page.bid_confirm_button.text,error_data_1['checks'])
        driver.refresh()

    # @data(*bid_error_100_data)
    @allure.feature('测试投资金额不是100的倍数')
    @pytest.mark.parametrize("bid_error_alert", bid_error_100_data)
    def test_bid_02_error(self,bid_error_alert,init_bid):
        driver, login_page, home_page = init_bid
        bid_page=BidPage(driver)
        bid_page.bid_input.send_keys(bid_error_alert['money'])
        bid_page.bid_confirm_button.click()
        assert(bid_page.bid_alert_element.text,bid_error_alert['checks'])
        driver.refresh()

    # @data(*bid_success_data)
    @allure.feature('测试投资成功')
    @pytest.mark.parametrize("succes_data", bid_success_data)
    def test_bid_03_success(self,succes_data,init_bid):
        # self.home_page.get()
        # self.home_page.click_bid_button()
        driver, login_page, home_page = init_bid
        bid_page=BidPage(driver)
        # bid_page.bid_input_money(succes_data['money'])
        bid_before_money= eval(bid_page.bid_succes(succes_data['money']))
        assert(bid_page.bid_success_msg_elem.text,succes_data['msg'])
        bid_page.click_bid_active_button()
        user_page=UserPage(driver)
        bid_after_money=user_page.get_avaiable_money()
        assert(bid_before_money-succes_data['money'],bid_after_money)
        driver.back()
        driver.refresh()






if __name__ == '__main__':
    pytest.main(['-s',"test_bid.py"])