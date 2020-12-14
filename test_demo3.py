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

# time.sleep(5)
Enlement.operation.find_uiautomator_tager_click(driver, 'resourceId("cn.smartinspection.combine:id/btn_go_to_login")', 5, 3)

# Enlement.operation.find_uiautomator_tager_send_keys(driver ,'resourceId("cn.smartinspection.combine:id/et_login_username")', 5, 'kentestgrp10',3)
# Enlement.operation.find_uiautomator_tager_send_keys(driver ,'resourceId("cn.smartinspection.combine:id/et_login_pwd")', 5, '12345678',3)
#
# Enlement.operation.find_uiautomator_tager_send_keys(driver ,'resourceId("cn.smartinspection.combine:id/et_enterprise_id")', 5, 't8',3)
#
# Enlement.operation.find_uiautomator_tager_click(driver,'resourceId("cn.smartinspection.combine:id/btn_login")', 5, 3)
#
# Enlement.operation.find_uiautomator_tager_click(driver,'text("ken集团")', 5, 3)

# Enlement.operation.find_uiautomator_tager_click(driver,'text("ken集团")',5)
# Enlement.operation.find_uiautomator_tager_click(driver,'text("1kentest公司3").fromParent(text("向下展开"))', 5, 3)
# Enlement.operation.find_uiautomator_tager_click(driver,'text("公司3项目1")', 5, 3)
# Enlement.operation.find_uiautomator_tager_click(driver,'text("更多")', 5, 3)
# Enlement.operation.find_uiautomator_tager_click(driver,'text("实测实量")', 5, 3)
# Enlement.operation.find_uiautomator_tager_click(driver,'text("全部同步")', 5, 3)
# Enlement.operation.find_uiautomator_tager_click(driver, 'resourceId("android:id/text1").text("19#测试1")', 5, 3)
# Enlement.operation.find_uiautomator_tager_click(driver, 'resourceId("android:id/button1").text("确定")', 5, 3)
# time.sleep(15)
# Enlement.operation.find_uiautomator_tager_click(driver, 'text("19#测试1")', 5, 3)
# Enlement.operation.find_uiautomator_tager_click(driver, 'text("19#")', 5, 3)
# Enlement.operation.find_uiautomator_tager_click(driver, 'text("19#自身")', 5, 3)
# Enlement.operation.find_uiautomator_tager_click(driver, 'text("混凝土结构工程")', 5, 3)
# Enlement.operation.find_uiautomator_tager_click(driver, 'text("截面尺寸")', 5, 3)
# Enlement.operation.find_uiautomator_tager_click(driver, 'text("确定")', 5, 3)
# Enlement.operation.touch(driver, 430, 820)
# Enlement.operation.find_uiautomator_tager_click(driver, 'resourceId("android:id/button2").text("是")', 5, 3)
# Enlement.operation.find_uiautomator_tager_click(driver, 'resourceId("cn.smartinspection.combine:id/et_value").text("设计值")', 5, 3)
# Enlement.operation.find_uiautomator_tager_send_keys(driver, 'resourceId("cn.smartinspection.combine:id/et_value").text("设计值")', 5, '3', 3)
# Enlement.operation.find_uiautomator_tager_click(driver, 'resourceId("cn.smartinspection.combine:id/et_value").text("数值1")', 5, 3)
# Enlement.operation.find_uiautomator_tager_send_keys(driver, 'resourceId("cn.smartinspection.combine:id/et_value").text("数值1")', 5, '11', 3)
# Enlement.operation.find_uiautomator_tager_click(driver, 'resourceId("cn.smartinspection.combine:id/et_value").text("数值2")', 5, 3)
# Enlement.operation.find_uiautomator_tager_send_keys(driver, 'resourceId("cn.smartinspection.combine:id/et_value").text("数值2")', 5, '300', 3)
# Enlement.operation.find_uiautomator_tager_click(driver, 'text("保存")', 5, 3)
# Enlement.operation.find_uiautomator_tager_click(driver, 'text("爆点整改")', 5, 3)
# Enlement.operation.find_uiautomator_tager_click(driver, 'text("整改人")', 5, 3)
# Enlement.operation.find_uiautomator_tager_click(driver, 'text("kentest10")', 5, 3)
# Enlement.operation.find_uiautomator_tager_click(driver, 'text("整改日期")', 5, 3)
# Enlement.operation.find_uiautomator_tager_click(driver, 'text("2天")', 5, 3)
# Enlement.operation.find_uiautomator_tager_send_keys(driver, 'resourceId("cn.smartinspection.combine:id/et_issue_describe").text("补充描述")', 5, 'test', 3)
# Enlement.operation.find_uiautomator_tager_click(driver, 'resourceId("cn.smartinspection.combine:id/action_done")', 5, 3)


