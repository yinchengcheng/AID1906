#!/usr/bin/python3
# -*- coding: utf-8 -*-
# time: 2022/4/9 下午4:18
#
import os

files = os.listdir('/step-2/day10/ftp/')

if not files:
    print('没有文件')
else:
    print(files)