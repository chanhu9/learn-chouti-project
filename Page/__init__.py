#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/4/12 15:45
#@Author: chanhu
#@File  : __init__.py.py

from selenium.webdriver.common.by import By
# selenium原生定位策略集
# 设置页面

# 字体按钮
button_ziti = (By.XPATH, '//*[contains(@text,"默认")]')
# 排行按钮
button_paihang = (By.XPATH, '//*[contains(@text,"排行")]')
# 搜索按钮
button_sousuo = (By.XPATH, '//*[contains(@NAF,"true")]')
# 搜索框
button_sousokuang = (By.CLASS_NAME, 'android.widget.EditText')
# 返回按钮
button_fanhui = (By.ID, 'android:id/home')
# 点击排行
button_pai = (By.ID,'miui:id/action_bar_title')
# 点击字体
button_zi = (By.ID,'miui:id/action_bar_title')

