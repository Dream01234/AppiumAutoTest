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
