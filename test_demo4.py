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
caps["platformVersion"] = "7.1.2"
caps["deviceName"] = "MI_9"
caps["appPackage"] = "cn.smartinspection.combine"
caps["appActivity"] = "cn.smartinspection.login.ui.activity.WelcomeGuideActivity"
caps["ensureWebviewsHavePages"] = True

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

Enlement.operation.find_uiautomator_tager_click(driver, 'resourceId("cn.smartinspection.combine:id/btn_go_to_login")', 5, 3)
# el2 = driver.find_element_by_id("cn.smartinspection.combine:id/et_login_username")
# el2.send_keys("kentestgrp10")
Enlement.operation.find_uiautomator_tager_send_keys(driver ,'resourceId("cn.smartinspection.combine:id/et_login_username")', 5, 'kentestgrp10',3)
Enlement.operation.find_uiautomator_tager_send_keys(driver ,'resourceId("cn.smartinspection.combine:id/et_login_pwd")', 5, '12345678',3)
# el3 = driver.find_element_by_id("cn.smartinspection.combine:id/et_login_pwd")
# el3.send_keys("12345678")
Enlement.operation.find_uiautomator_tager_send_keys(driver ,'resourceId("cn.smartinspection.combine:id/et_enterprise_id")', 5, 't8',3)
# el4 = driver.find_element_by_id("cn.smartinspection.combine:id/et_enterprise_id")
# el4.send_keys("t8")
Enlement.operation.find_uiautomator_tager_click(driver,'resourceId("cn.smartinspection.combine:id/btn_login")', 5, 3)
Enlement.operation.find_uiautomator_tager_click(driver, 'text("我")', 5, 3)
Enlement.operation.find_uiautomator_tager_click(driver, 'text("切换帐号")', 5, 3)