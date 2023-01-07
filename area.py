import Device
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
"------区域类"
class district:

    "查询"
    find = 'cn.smartinspection.combine:id/et_filter'

    "选择本级"
    this_level = 'cn.smartinspection.combine:id/tv_select_this_level'

    "输入查询楼层"
    def findarea(self,name):
        driver = Device.Setting.driver
        timeout = 3
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.ID, self.find)),
            message='not find this ID').clear()
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.ID, self.find)),
            message='not find this ID').send_keys(name)

    "选择指定楼栋"
    def findbuilding(self,buildingname):
        driver = Device.Setting.driver
        name = 'text("' + buildingname + '")'
        driver.find_element_by_android_uiautomator(name).click()

    "选择指定楼层"
    def findfloor(self,floorname):
        driver = Device.Setting.driver
        name = 'text("' + floorname + '")'
        driver.find_element_by_android_uiautomator(name).click()

    "选择-选择本级"
    def findthis_level(self,name):
        driver = Device.Setting.driver
        level = 'text("' + name + '").fromParent(text("选择本级"))'
        driver.find_element_by_android_uiautomator(level).click()