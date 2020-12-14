from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction
import Enlement
import method
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "9"
caps["deviceName"] = "MHA_AL00"
caps["appPackage"] = "cn.smartinspection.combine"
caps["appActivity"] = "cn.smartinspection.login.ui.activity.CustomSplashActivity"
caps["ensureWebviewsHavePages"] = True

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

Enlement.operation.find_uiautomator_tager_click(driver, 'text("始终允许")', 3, 3)
time.sleep(0.5)
Enlement.operation.find_uiautomator_tager_click(driver, 'text("始终允许")', 3, 3)
time.sleep(1)
Enlement.operation.find_uiautomator_tager_click(driver, 'text("始终允许")', 3, 3)
time.sleep(1)
Enlement.operation.find_uiautomator_tager_click(driver, 'text("始终允许")', 3, 3)
time.sleep(1)
Enlement.operation.find_uiautomator_tager_click(driver, 'text("始终允许")', 3, 3)

Enlement.operation.find_uiautomator_tager_click(driver, 'text("马上登录")', 3, 3)
Enlement.operation.find_uiautomator_tager_send_keys(driver, 'text("请输入用户名")', 3, 'kentestgrp10', 3)


Enlement.operation.find_uiautomator_tager_send_keys(driver ,'text("请输入密码")', 3, '12345678',3)

Enlement.operation.find_uiautomator_tager_send_keys(driver ,'text("企业编码(非必填)")', 3, 't8',3)

Enlement.operation.find_uiautomator_tager_click(driver,'text("登录")', 3, 3)
# Enlement.operation.find_uiautomator_tager_click(driver, 'text("我")', 5, 3)
# Enlement.operation.find_uiautomator_tager_click(driver, 'text("切换帐号")', 5, 3)