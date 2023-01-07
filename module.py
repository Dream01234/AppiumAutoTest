import Device
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

"----模块类"
class cloudmodule:

    "展开"
    unfold = 'cn.smartinspection.combine:id/iv_indicator'

    "全部同步"
    synchronous ='text("全部同步")'


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
        name = 'text("' + project_name + '")'
        driver.find_element_by_android_uiautomator(name).click()

    "点击全部同步"
    def clicksynchronous(self):
        driver = Device.Setting.driver
        driver.find_element_by_android_uiautomator(self.synchronous).click()

    "点击任务同步"
    def clicktask(self,name):
        driver = Device.Setting.driver
        task = 'resourceId("cn.smartinspection.combine:id/ay5").fromParent(text("' + name + '"))'
        # task = 'text("' + father + '").fromParent(text("' + child + '"))'
        driver.find_element_by_android_uiautomator(task).click()

    "点击任务"
    def clicktask_name(self,name):
        driver = Device.Setting.driver
        name = 'text("' + name + '")'
        driver.find_element_by_android_uiautomator(name).click()

    "检测toast是否存在"
    def is_toast_exist(self,text, timeout=30, poll_frequency=0.5):
        driver = Device.Setting.driver
        try:
            message_loc = ("xpath", "//*[contains(@text,'%s')]" % text)
            WebDriverWait(driver, timeout, poll_frequency).until(EC.presence_of_element_located(message_loc))
            print("成功")
            return True
        except:
            print("--------------任务失败或者有什么别的麻烦吧")
            return False

    "等待同步加载(没有toast情况下)"
    def wait_loading(self):
        """
        driver:设备
        tager:同步检测的过程中的文本
        b_tager:同步检测前的文本
        """
        driver = Device.Setting.driver
        i = 0.5
        tager = 'text("正在同步")'
        b_tager = 'text("同步")'
        boss = True
        while boss:
            try:
                if driver.find_element_by_android_uiautomator(tager):
                    time.sleep(i)
            except Exception as e:
                try:
                    if driver.find_element_by_android_uiautomator(b_tager):
                        print("同步成功")
                        boss = False
                except Exception as e:
                        print("同步失败")
                        boss = False