import Device

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