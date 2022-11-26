# name : huaihua
# date : 2022/6/6-9:44
# -*- coding: utf-8 -*-

import datetime
import time
from selenium import webdriver
import pyttsx3

engine = pyttsx3.init()
# 当前时间
now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
# 秒杀时间
timer = "2022-06-06 15:06:00.00000000"
# 自动化测试Chrome插件
driver = webdriver.Chrome(r'D:\618\day\Scripts\chromedriver_win32\chromedriver.exe')
# 打开淘宝页面
driver.get("https://www.taobao.com/")
time.sleep(3)
# 点击请登录
driver.find_element_by_link_text("亲，请登录").click()

print(f"请尽快扫码登录")
# 预留20s扫码登录
time.sleep(20)
# 打开购物车
driver.get("https://cart.taobao.com/cart.htm")

time.sleep(3)

# 是否全选购物车

while True:
    try:
        if driver.find_element_by_id("J_SelectAll1"):
            driver.find_element_by_id("J_SelectAll1").click()
            break
    except:
        print(f"没有购买按钮")

while True:
    # 获取当前时间
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    print(now)
    # 判断
    if now > timer:
        while True:
            try:
                if driver.find_element_by_id("J_Go"):
                    print("here")
                    driver.find_element_by_id("J_Go").click()
                    print(f"恭喜，已将商品锁定，请及时支付订单")
                    engine.say("恭喜，已将商品锁定，请及时支付订单")
                    engine.runAndWait()
                    break
            except:
                pass
            # 提交订单