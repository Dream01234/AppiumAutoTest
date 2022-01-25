import Device
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction

"-------日期类"
class dates:

    "选择日期--date为多少天"
    def clickdate(self,date):
        driver = Device.Setting.driver
        name = '\'text("' + date + '")\''
        driver.find_element_by_android_uiautomator(name).click()

    "点击 清除日期"
    def clickclear(self):
        driver = Device.Setting.driver
        name = '\'text("清除日期")\''
        driver.find_element_by_android_uiautomator(name).click()