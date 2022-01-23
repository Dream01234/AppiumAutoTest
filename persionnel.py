import Device
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction

"----人员类"
class member:

    "点击 搜索人员并输入人名"
    def findname(self,value):
        driver = Device.Setting.driver
        name = '\'text("搜索人员")\''
        driver.find_element_by_android_uiautomator(name).click()
        driver.find_element_by_android_uiautomator(name).send_keys(value)

    "选择 结果列表人员"
    def clickname(self,value):
        driver = Device.Setting.driver
        name = '\'text("' + value + '")\''
        driver.find_element_by_android_uiautomator(name).click()

