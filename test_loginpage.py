# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import Device
import Enlement
import time
import pytest
import method
import allure
import os
from appium.webdriver.common.touch_action import TouchAction

class TestClass:

    def test_login(self, app_driver=Device.Setting.driver):
        Enlement.operation.find_element_click(app_driver,3,'ID','cn.smartinspection.combine:id/btn_go_to_login')
        Enlement.operation.find_element_sendkeys(app_driver,3,'ID','cn.smartinspection.combine:id/et_login_username',"kentestgrp10")
        Enlement.operation.find_element_sendkeys(app_driver,3,'ID','cn.smartinspection.combine:id/et_login_pwd','12345678')
        Enlement.operation.find_element_sendkeys(app_driver,3,'ID','cn.smartinspection.combine:id/et_enterprise_id','t8')
        Enlement.operation.find_element_click(app_driver,3,'ID','cn.smartinspection.combine:id/btn_login')
        Enlement.operation.find_uiautomator_text_click(app_driver,5,'text("ken集团")')
        app_driver.find_element_by_android_uiautomator('text("1kentest公司3").fromParent(text("向下展开"))').click()
        app_driver.find_element_by_android_uiautomator('text("公司3项目1")').click()
        app_driver.find_element_by_android_uiautomator('text("更多")').click()
        app_driver.find_element_by_android_uiautomator('text("实测实量")').click()
        time.sleep(3)
        app_driver.find_element_by_android_uiautomator('text("全部同步")').click()
        time.sleep(3)
        app_driver.find_element_by_android_uiautomator('resourceId("android:id/text1").text("19#测试1")').click()
        app_driver.find_element_by_android_uiautomator('resourceId("android:id/button1").text("确定")').click()
        time.sleep(15)
        app_driver.find_element_by_android_uiautomator('text("19#测试1")').click()
        app_driver.find_element_by_android_uiautomator('text("19#")').click()
        app_driver.find_element_by_android_uiautomator('text("19#自身")').click()
        app_driver.find_element_by_android_uiautomator('text("混凝土结构工程")').click()
        app_driver.find_element_by_android_uiautomator('text("截面尺寸")').click()
        app_driver.find_element_by_android_uiautomator('text("确定")').click()
        TouchAction(app_driver).tap(x=600, y=888).perform()
        # app_driver.tap([(666,888),(777,884)],100)
        # app_driver.find_element_by_android_uiautomator('resourceId("cn.smartinspection.combine:id/pv_plan")').click()
        # app_driver.find_element_by_android_uiautomator('text("设计值")').click()
        # app_driver.find_element_by_android_uiautomator('text("设计值")').send_keys(3)
        # app_driver.find_element_by_android_uiautomator('text("数值1")').send_keys(1)
        # app_driver.find_element_by_android_uiautomator('text("数值2")').send_keys(2)
        # app_driver.find_element_by_android_uiautomator('text("保存")').click()


        # result = method.results.is_element_exist(app_driver, 5, 'ID', 'cn.smartinspection.combine:id/iv_edit_module_board')
        # assert result

    # def test_logout(self, app_driver=Device.Setting.driver):
    #     Enlement.operation.find_element_click(app_driver, 3, 'xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.TabHost/android.widget.LinearLayout/android.widget.TabWidget/android.widget.RelativeLayout[5]/android.widget.ImageView')
    #     Enlement.operation.find_element_click(app_driver, 3, 'xpath','/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout[3]/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[3]')
    #     Enlement.operation.find_element_click(app_driver, 3, 'ID', 'android:id/button1')
    #     result = method.results.is_element_exist(app_driver, 5, 'ID', 'cn.smartinspection.combine:id/btn_login')
    #     assert result

if __name__ == '__main__':
        pytest.main(["test_loginpage.py", "--alluredir=report/alluer_raw"])
        os.system(
            "allure generate C:/Users/41708/PycharmProjects/pythonProject/report/alluer_raw -o C:/Users/41708/PycharmProjects/pythonProject/report/allure_report --clean")





