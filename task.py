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
    def click_null_point(self):
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

    "确认类弹框"
    def clickconfirm(self,choice):
        driver = Device.Setting.driver
        name = '\'text("' + choice + '")\''
        driver.find_element_by_android_uiautomator(name).click()

    "点击 设计值并填写"
    def sendkey(self,value):
        driver = Device.Setting.driver
        name = '\'text("设计值")\''
        driver.find_element_by_android_uiautomator(name).click()
        driver.find_element_by_android_uiautomator(name).send_keys(value)

    "点击 数值并填写"
    def senkvalue(self,number,value):
        driver = Device.Setting.driver
        name = '\'text("数值' + number + '")\''
        driver.find_element_by_android_uiautomator(name).click()
        driver.find_element_by_android_uiautomator(name).send_keys(value)

    "点击 删除"
    def clickdelete(self):
        driver = Device.Setting.driver
        name = '\'text("删除")\''
        driver.find_element_by_android_uiautomator(name).click()

    "点击 保存"
    def clicksave(self):
        driver = Device.Setting.driver
        name = '\'text("保存")\''
        driver.find_element_by_android_uiautomator(name).click()

    "点击 增加数值按钮 + "
    def clickplus(self):
        driver = Device.Setting.driver
        name = '\'text("+")\''
        driver.find_element_by_android_uiautomator(name).click()

    "点击 请选择下拉列表"
    def clickpulldown(self):
        driver = Device.Setting.driver
        name = '\'text("请选择")\''
        driver.find_element_by_android_uiautomator(name).click()

    "点击 爆点整改"
    def clickadjust(self):
        driver = Device.Setting.driver
        name = '\'text("爆点整改")\''
        driver.find_element_by_android_uiautomator(name).click()

    "点击 新增检查项"
    def clicknewitem(self):
        driver = Device.Setting.driver
        name = '\'text("新增检查项")\''
        driver.find_element_by_android_uiautomator(name).click()

    "点击 删除描点"
    def clickdeletepoint(self):
        driver = Device.Setting.driver
        name = '\'text("删除描点")\''
        driver.find_element_by_android_uiautomator(name).click()

