#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/4/12 15:50
#@Author: chanhu
#@File  : test_search.py

# 导入封装好的页面类
from Page.search_page import Search_Page
# 导入独立的手机驱动对象
from Basic.Init_Driver import init_driver
import sys,os
from Basic.read_data import Read_Data
import pytest
import time
sys.path.append(os.getcwd())


def package_param_data():
    list_data = []  # 存储参数值列表，格式[(用例编号1,输入内容2),(用例编号1,输入内容2)...]
    yaml_data = Read_Data().return_data()  # 返回yaml文件读取数据
    for i in yaml_data.keys():
        list_data.append((i, yaml_data.get(i).get('input_text')))  # list_data中添加参数值
        # print(list_data)
    return list_data


class Test_search:
    # def __init__(self):
    #     self.driver = init_driver()

    def setup_class(self):
        self.driver = init_driver()

    @pytest.mark.parametrize('test_id,text',package_param_data())
    def test_search(self,test_id,text):
        print("test_id:", test_id)
        # 示例化页面封装类
        sp = Search_Page(self.driver)
        # 调用操作类
        sp.function(text)
        assert 1 == 1


    def teardown_class(self):
        self.driver.quit()
