#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/4/12 15:44
#@Author: chanhu
#@File  : Init_Driver.py

from appium import webdriver
def init_driver():
    # 启动参数
    desired_caps = {}
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.4.4'
    desired_caps['deviceName'] = '740e5dfa'
    # app信息
    desired_caps['appPackage'] = 'com.android.settings'
    desired_caps['appActivity'] = '.MiuiSettings'
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    return driver