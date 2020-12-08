# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction
import Enlement


caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "7.1.2"
caps["deviceName"] = "MI_9"
caps["appPackage"] = "cn.smartinspection.combine"
caps["appActivity"] = "cn.smartinspection.login.ui.activity.WelcomeGuideActivity"
caps["ensureWebviewsHavePages"] = True

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

el1 = driver.find_element_by_id("cn.smartinspection.combine:id/btn_go_to_login")
el1.click()
time.sleep(1)
el2 = driver.find_element_by_id("cn.smartinspection.combine:id/et_login_username")
el2.send_keys("kentestgrp10")
el3 = driver.find_element_by_id("cn.smartinspection.combine:id/et_login_pwd")
el3.send_keys("12345678")
el4 = driver.find_element_by_id("cn.smartinspection.combine:id/et_enterprise_id")
el4.send_keys("t8")
el5 = driver.find_element_by_id("cn.smartinspection.combine:id/btn_login")
el5.click()
time.sleep(5)
el20 = driver.find_element_by_android_uiautomator('text("ken集团")').click()
el7 = driver.find_element_by_android_uiautomator('text("1kentest公司3").fromParent(text("向下展开"))').click()
el8 = driver.find_element_by_android_uiautomator('text("公司3项目1")').click()
el9 = driver.find_element_by_android_uiautomator('text("更多")').click()
el10 = driver.find_element_by_android_uiautomator('text("实测实量")').click()
time.sleep(3)
el11 = driver.find_element_by_android_uiautomator('text("全部同步")').click()
time.sleep(3)
el12 = driver.find_element_by_android_uiautomator('resourceId("android:id/text1").text("19#测试1")').click()
el13 = driver.find_element_by_android_uiautomator('resourceId("android:id/button1").text("确定")').click()
time.sleep(15)
el14 = driver.find_element_by_android_uiautomator('text("19#测试1")').click()
el15 = driver.find_element_by_android_uiautomator('text("19#")').click()
el16 = driver.find_element_by_android_uiautomator('text("19#自身")').click()
el17 = driver.find_element_by_android_uiautomator('text("混凝土结构工程")').click()
el18 = driver.find_element_by_android_uiautomator('text("截面尺寸")').click()
el19 = driver.find_element_by_android_uiautomator('text("确定")').click()
# time.sleep(10)
# TouchAction(driver).tap(x=550,y=1350).perform()
# time.sleep(2)
# el22 = driver.find_element_by_android_uiautomator('resourceId("android:id/button2").text("是")').click()
# el23 = driver.find_element_by_android_uiautomator('resourceId("cn.smartinspection.combine:id/et_value").text("设计值")').click()
# el24 = driver.find_element_by_android_uiautomator('resourceId("cn.smartinspection.combine:id/et_value").text("设计值")').send_keys(3)
# el25 = driver.find_element_by_android_uiautomator('resourceId("cn.smartinspection.combine:id/et_value").text("数值1")').click()
# el27 = driver.find_element_by_android_uiautomator('resourceId("cn.smartinspection.combine:id/et_value").text("数值1")').send_keys(1)
# el28 = driver.find_element_by_android_uiautomator('resourceId("cn.smartinspection.combine:id/et_value").text("数值2")').click()
# el26 = driver.find_element_by_android_uiautomator('resourceId("cn.smartinspection.combine:id/et_value").text("数值2")').send_keys(1)
# el29 = driver.find_element_by_android_uiautomator('text("保存")').click()

TouchAction(driver).tap(x=215,y=820).perform()
time.sleep(2)
el22 = driver.find_element_by_android_uiautomator('resourceId("android:id/button2").text("是")').click()
el23 = driver.find_element_by_android_uiautomator('resourceId("cn.smartinspection.combine:id/et_value").text("设计值")').click()
el24 = driver.find_element_by_android_uiautomator('resourceId("cn.smartinspection.combine:id/et_value").text("设计值")').send_keys(3)
el25 = driver.find_element_by_android_uiautomator('resourceId("cn.smartinspection.combine:id/et_value").text("数值1")').click()
el27 = driver.find_element_by_android_uiautomator('resourceId("cn.smartinspection.combine:id/et_value").text("数值1")').send_keys(11)
el28 = driver.find_element_by_android_uiautomator('resourceId("cn.smartinspection.combine:id/et_value").text("数值2")').click()
el26 = driver.find_element_by_android_uiautomator('resourceId("cn.smartinspection.combine:id/et_value").text("数值2")').send_keys(300)
el29 = driver.find_element_by_android_uiautomator('text("保存")').click()
el29 = driver.find_element_by_android_uiautomator('text("爆点整改")').click()
el29 = driver.find_element_by_android_uiautomator('text("整改人")').click()
el29 = driver.find_element_by_android_uiautomator('text("kentest10")').click()
el29 = driver.find_element_by_android_uiautomator('text("整改日期")').click()
el29 = driver.find_element_by_android_uiautomator('text("2天")').click()
el29 = driver.find_element_by_android_uiautomator('resourceId("cn.smartinspection.combine:id/et_issue_describe").text("补充描述")').send_keys('test')
el29 = driver.find_element_by_android_uiautomator('resourceId("cn.smartinspection.combine:id/action_done")').click()