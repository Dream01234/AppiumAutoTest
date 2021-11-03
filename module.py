import Device
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class cloudmodule:

    "展开"
    unfold = 'cn.smartinspection.combine:id/iv_indicator'

    "全部同步"
    synchronous ='cn.smartinspection.combine:id/tv_sync_all'


    "点击下展开"
    def clickunfold(self):
        driver = Device.Setting.driver
        timeout = 3
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.ID, self.unfold)),
            message='not find this ID').click()

    "选择项目"
    def clickproject(self,project_name):
        driver = Device.Setting.driver
        name = 'text(' + project_name + ')'
        driver.find_element_by_android_uiautomator(name).click()

    "点击全部同步"
    def clicksynchronous(self):
        driver = Device.Setting.driver
        timeout = 3
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.ID, self.synchronous)),
            message='not find this ID').click()

    "点击任务同步"
    def clicktask(self,father,child):
        driver = Device.Setting.driver
        task = 'text(' + father + ').fromParent(text(' + child + '))'
        driver.find_element_by_android_uiautomator(task).click()

    "点击任务"
    def clicktask_name(self,name):
        driver = Device.Setting.driver
        name = 'text(' + name + ')'
        driver.find_element_by_android_uiautomator(name).click()

