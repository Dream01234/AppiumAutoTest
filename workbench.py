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
    find = 'text("搜索应用")'

    "返回上一级"
    retu = 'text("集团及其下属公司")'

    name = 'cn.smartinspection.combine:id/ary'

    "点击组织"
    def clickorganization(self):
        driver = Device.Setting.driver
        driver.find_element_by_android_uiautomator(self.organization).click()

    "点击模块"
    def clickmodule(self):
        driver = Device.Setting.driver
        driver.find_element_by_android_uiautomator(self.name).click()

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
        driver.find_element_by_android_uiautomator(self.find).click()

    "输入模块名"
    def sendkey(self,module_name):
        driver = Device.Setting.driver
        driver.find_element_by_android_uiautomator(self.find).send_keys(module_name)

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

    "返回上一层组织"
    def clickreturn(self):
        driver = Device.Setting.driver
        driver.find_element_by_android_uiautomator(self.retu).click()

    "滚动寻找模块并点击模块"
    def swipefind(self,name):
        driver = Device.Setting.driver
        width = driver.get_window_size().get('width')
        height = driver.get_window_size().get('height')
        tager = 'text("' + name + '")'
        boss = 0
        while 5 > boss:
            try:
                if driver.find_element_by_android_uiautomator(tager):
                    driver.find_element_by_android_uiautomator(tager).click()
                    print("找到目标:" + tager)
                    break
            except Exception as e:
                driver.swipe(int(width) / 2, int(height) / 2, int(width) / 2, int(height) / 8, duration=3000)
                boss = boss + 1
                print("-----------------找不到目标:" +tager + ",滚吧!+" + str(boss))



