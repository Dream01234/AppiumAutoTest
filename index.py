import Device
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
"----首页类"
class cloudIndex:

    "免费注册"
    btn_register = 'text("免费注册")'

    "马上登录"
    btn_go_to_login = 'text("马上登录")'

    "同意"
    agree = 'text("同意")'

    "暂不使用"
    no = 'text("暂不使用")'

    "始终允许"
    allow = 'text("允许")'

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
        driver.find_element_by_android_uiautomator(self.btn_register).click()

    "点击马上登录"
    def click_btngotologin(self):
        driver = Device.Setting.driver
        driver.find_element_by_android_uiautomator(self.btn_go_to_login).click()