#!/usr/bin/python3
# -*- coding: utf-8 -*-
# time: 2022/4/4 下午3:58
#
import time
from multiprocessing import *
from time import sleep
from random import randint

money = Value('i', 5000)

def man():
    for i in range(30):
        time.sleep(0.2)
        money.value += randint(1,1000)

def girl():
    for i in range(30):
        time.sleep(0.15)
        money.value -= randint(100,800)

p1 = Process(target=man)
p2 = Process(target=girl)

p1.start()
p2.start()
p1.join()
p2.join()

print(money.value)