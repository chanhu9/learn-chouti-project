#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/4/12 15:44
#@Author: chanhu
#@File  : Basy.py

from selenium.webdriver.support.wait import WebDriverWait
class Base(object):
    def __init__(self,driver):
        self.driver = driver

    def find_element(self,loc,timeout=10):
            '''
                二次封装find_element方法，增加了显示等待和简化参数传递
            '''
            # 原生方法：find_element(by=By.ID, value=None)，需要传递两个值
            # *loc 将传入(By.XX, "value")解包为两个单独的值，满足find_element方法的参数传递
            return WebDriverWait(self.driver, timeout).until(lambda x: x.find_element(*loc))

    def click_element(self,loc):
            '''
                封装点击操作函数
            '''
            self.find_element(loc).click()

    def input_text(self,loc,text):
            '''
                封装输入操作函数
            '''
            self.fm = self.find_element(loc)
            self.fm.clear() # 需要先清空输入框，防止有默认内容
            self.fm.send_keys(text)