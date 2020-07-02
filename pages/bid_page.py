#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time    : 2018/4/9 12:00
# @Author  : scrum
# @Email   : 718944679@qq.com
# @File    : bid_page.py
# @Software: PyCharm

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from pages.base_page import BasePage


class BidPage(BasePage):

    bid_input_locator=(By.CSS_SELECTOR,'.invest-unit-investinput')

    bid_confirm_locator= (By.CSS_SELECTOR,'.btn-special')

    bid_alert_locator =(By.XPATH,"//div[@class='text-center']")

    active_button_locator=(By.XPATH,"//div[@class='layui-layer-content']//button")

    bid_success_msg_locator =(By.XPATH,"//div[@class='layui-layer-content']//div[@class='capital_font1 note']")




    @property
    def bid_input(self)-> WebElement:
        "投资输入框"
        return self.wait_visable_element(self.bid_input_locator)

    def bid_succes(self,money):
        "投标成功"
        e = self.bid_input
        balance= e.get_attribute("data-amount")
        e.send_keys(money)
        self.bid_confirm_button.click()
        return balance


    @property
    def bid_confirm_button(self):
        """投资确认按钮"""
        return self.wait_visable_element(self.bid_confirm_locator)

    @property
    def bid_alert_element(self):
        """投标金额输入错误弹框信息"""
        return self.wait_visable_element(self.bid_alert_locator)


    @property
    def bid_success_msg_elem(self):
        """定位投标成功信息元素"""
        return self.wait_visable_element(self.bid_success_msg_locator)

    def click_bid_active_button(self):
        """点击【查看并激活】"""
        return self.wait_click_element(self.active_button_locator).click()













