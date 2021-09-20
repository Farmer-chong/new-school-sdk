# -*- coding: utf-8 -*-
'''
    :file: base_sample.py
    :author: -Farmer
    :url: https://blog.farmer233.top
    :date: 2021/09/18 00:31:02
'''

from school_sdk.client import UserClient
from school_sdk import SchoolClient

# 实例化学校
Gdust = SchoolClient("172.16.254.1")

# 实例化用户
user:UserClient = Gdust.user_login("account", "password")

# 获取课表
cours = user.get_schedule(year=2021, term=1)

print(cours)