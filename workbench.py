import Device
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

"---工作台类"
class cloudworkbench:

    "组织"
    organization = 'text("华坤工程建设集团十局总部")'

    "模块"
    module = 'text("统计")'

    "更多"
    more = 'text("更多")'

    "组织展开"
    organization_launched = 'text("1分公司").fromParent(text("向下展开"))'

    "公司1项目贰"
    project = 'text("公司1项目贰")'

    "搜索"
    find = 'cn.smartinspection.combine:id/et_search'

    "点击组织"
    def clickorganization(self):
        driver = Device.Setting.driver
        driver.find_element_by_android_uiautomator(self.organization).click()

    "点击模块"
    def clickmodule(self,module):
        driver = Device.Setting.driver
        name = 'text("' + module + '")'
        driver.find_element_by_android_uiautomator(name).click()

    "点击更多"
    def clickmore(self):
        driver = Device.Setting.driver
        driver.find_element_by_android_uiautomator(self.more).click()

    "点击组织展开"
    def clickorganization_launched(self):
        driver = Device.Setting.driver
        driver.find_element_by_android_uiautomator(self.organization_launched).click()

    "点击搜索"
    def clickfind(self):
        driver = Device.Setting.driver
        timeout = 3
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.ID, self.find)),
            message='not find this ID').click()

    "输入模块名"
    def sendkey(self,module_name):
        driver = Device.Setting.driver
        timeout = 3
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.ID, self.find)),
            message='not find this ID').send_keys(module_name)

    "输入查找组织名字"
    def senkorganization(self,name):
        driver = Device.Setting.driver
        timeout = 3
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.ID, self.find)),
            message='not find this ID').clear()
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.ID, self.find)),
            message='not find this ID').send_keys(name)

    "选择项目"
    def clicktager(self):
        driver = Device.Setting.driver
        driver.find_element_by_android_uiautomator(self.project).click()


