import Device
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
"-----指标类"

class indicator:

    "确定"
    confirm = 'cn.smartinspection.combine:id/btn_confirm'

    "重置"
    reset = 'cn.smartinspection.combine:id/btn_reset'

    "点击确定"
    def clickconfirm(self):
        driver = Device.Setting.driver
        timeout = 3
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.ID, self.confirm)),
            message='not find this ID').click()
    "点击重置"
    def clickreset(self):
        driver = Device.Setting.driver
        timeout = 3
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.ID, self.reset)),
            message='not find this ID').click()

    "选择检查项"
    def clickitem(self,itemname):
        driver = Device.Setting.driver
        name = '\'text("' + itemname + '")\''
        driver.find_element_by_android_uiautomator(name).click()

    "勾选检查项(末级检查项)"
    def clicklastitem(self,itemname):
        driver = Device.Setting.driver
        name = '\'resourceId("cn.smartinspection.combine:id/cb_select").text("' + itemname + '")\''
        driver.find_element_by_android_uiautomator(name).click()