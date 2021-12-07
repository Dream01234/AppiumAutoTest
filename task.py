import Device
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction

"-----任务类"
class picture:


    "点击空白处新增测量点"
    null_point = 'cn.smartinspection.combine:id/cb_click_blank_to_add_measure_zone'


    "点击全部区域"
    def clickarea(self,area):
        driver = Device.Setting.driver
        name = '\'text("' + area + '")\''
        driver.find_element_by_android_uiautomator(name).click()

    "点击测量"
    def clickmeasure(self,measure):
        driver = Device.Setting.driver
        name = '\'text("' + measure + '")\''
        driver.find_element_by_android_uiautomator(name).click()

    "点击空白处按钮"
    def click_null_point(self,null_point):
        driver = Device.Setting.driver
        timeout = 3
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.ID, self.null_point)),
            message='not find this ID').click()

    "点击选择测量指标"
    def clickindicators(self,indicators):
        driver = Device.Setting.driver
        name = '\'text("' + indicators + '")\''
        driver.find_element_by_android_uiautomator(name).click()

    "点击图纸某处"
    def clickpir(self,x,y):
        driver = Device.Setting.driver
        TouchAction(driver).tap(x=x, y=y).perform()


