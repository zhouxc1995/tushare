# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 13:50:29 2020

@author: Meng Guangming
"""

import tushare as ts
import datetime
pro = ts.pro_api('...')#输入自己的API

import numpy as np
import pandas as pd
from pandas import DataFrame
import time

from datetime import timedelta, datetime

yesterday = datetime.today() + timedelta(-1)
 
yesterday_format = yesterday.strftime('%Y%m%d')

today = time.strftime("%Y%m%d",time.localtime(time.time()))
print(today)

df = pro.cctv_news(date=yesterday_format)####根据时间看昨晚的，还是当天晚上的而选择 yesterday or today

print(df.title)

for i in df.index:
    if df.title[i]=='联播快讯' or df.title[i]=='国内联播快讯' :
        print(df.content[i])