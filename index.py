import Device
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class cloudIndex:

    "免费注册"
    btn_register = 'cn.smartinspection.combine:id/btn_register'

    "马上登录"
    btn_go_to_login = 'cn.smartinspection.combine:id/btn_go_to_login'

    "同意"
    agree = 'text("同意")'

    "暂不使用"
    no = 'text("暂不使用")'

    "始终允许"
    allow = 'text("始终使用")'

    "禁止"
    ban = 'text("禁止")'

    "点击同意"
    def click_agree(self):
        driver = Device.Setting.driver
        driver.find_element_by_android_uiautomator(self.agree).click()

    "点击暂不使用"
    def click_no(self):
        driver = Device.Setting.driver
        driver.find_element_by_android_uiautomator(self.no).click()

    "点击始终允许"
    def click_allow(self):
        driver = Device.Setting.driver
        driver.find_element_by_android_uiautomator(self.allow).click()

    "点击禁止"
    def click_ban(self):
        driver = Device.Setting.driver
        driver.find_element_by_android_uiautomator(self.ban).click()

    "点击免费注册"
    def click_btnregister(self):
        driver = Device.Setting.driver
        timeout = 3
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.ID, self.btn_register)),
            message='not find this ID').click()

    "点击马上登录"
    def click_btngotologin(self):
        driver = Device.Setting.driver
        timeout = 3
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.ID, self.btn_go_to_login)),
            message='not find this ID').click()