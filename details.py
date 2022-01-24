import Device
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction

"----爆点详情类"
class boompoint:

    "点击 整改负责人"
    def clickrepairer(self):
        driver = Device.Setting.driver
        name = '\'text("整改负责人")\''
        driver.find_element_by_android_uiautomator(name).click()

    "点击 整改期限"
    def clickdate(self):
        driver = Device.Setting.driver
        name = '\'text("整改期限")\''
        driver.find_element_by_android_uiautomator(name).click()

    "点击 补充描述"
    def clicksupplement(self):
        driver = Device.Setting.driver
        name = '\'text("补充描述")\''
        driver.find_element_by_android_uiautomator(name).click()

    "点击 保存"
    def clicksave(self):
        driver = Device.Setting.driver
        name = '\'text("保存")\''
        driver.find_element_by_android_uiautomator(name).click()

    "确定类弹框处理"
    def clickconfirm(self, choice):
        driver = Device.Setting.driver
        name = '\'text("' + choice + '")\''
        driver.find_element_by_android_uiautomator(name).click()

    "点击 已标识"
    def clicktag(self,tag):
        driver = Device.Setting.driver
        name = '\'text("' + tag + '")\''
        driver.find_element_by_android_uiautomator(name).click()

