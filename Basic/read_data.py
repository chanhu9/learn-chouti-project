#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/4/12 15:45
#@Author: chanhu
#@File  : read_data.py

import yaml
class Read_Data:

    def return_data(self):
        with open('./data/search_page.yaml', 'r', encoding='utf-8') as f:
            data = yaml.load(f)
            # 读取文件内容
            print(data)
            return data

# if __name__ == '__main__':
#     Read_Data().return_data()