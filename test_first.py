#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time    : 2018/4/9 12:00
# @Author  : scrum
# @Email   : 718944679@qq.com
# @File    : test_first.py
# @Software: PyCharm

import pytest

@pytest.fixture(scope="class")
def myfixture():
    print("执行myfixture")

class Test_firstFile():

    def test_one(self,myfixture):
        print("执行test_one")
        assert 1+2==3

    def test_two(self,myfixture):
        print("执行test_two")
        assert 1==1

    def test_three(self,myfixture):
        print("执行test_three")
        assert 1+1==2

if __name__=="__main__":
    pytest.main(["-s","test_first.py"])
