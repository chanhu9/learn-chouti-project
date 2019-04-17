#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/4/12 15:46
#@Author: chanhu
#@File  : search_page.py

from Basic.Basy import Base
import Page
class Search_Page(Base):

    def __init__(self,driver):
        Base.__init__(self,driver)

    def function(self, text):
        self.click_element(Page.button_ziti)
        self.click_element(Page.button_paihang)
        self.click_element(Page.button_sousuo)
        self.input_text(Page.button_sousokuang, text)
        self.click_element(Page.button_fanhui)
        self.click_element(Page.button_pai)
        self.click_element(Page.button_zi)