from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime
import time
import xlrd
import os
from appium.webdriver.common.touch_action import TouchAction

class operation:
    """选择控件点击"""
    def find_element_click(driver, timeout, select, name):
        """滑动寻找控件点击"""
        width = driver.get_window_size().get('width')
        height = driver.get_window_size().get('height')
        if select == 'ID':
            i = 0
            while i < 10:
                try:
                    WebDriverWait(driver, timeout).until(
                        EC.presence_of_element_located((By.ID, name)),
                        message='not find this ID').click()
                    break
                except Exception as e :
                    driver.swipe(int(width)/2, int(height)/2, int(width)/2, int(height)/8, duration=3000)
                    i = i + 1
        elif select == 'xpath':
            i = 0
            while i < 10:
                try:
                    WebDriverWait(driver, timeout).until(
                        EC.presence_of_element_located((By.XPATH, name)),
                        message='not find this xpath').click()
                    break
                except Exception as e :
                    driver.swipe(int(width) / 2, int(height) / 2, int(width) / 2, int(height) / 8, duration=3000)
                    i = i + 1


    """选择控件输入"""
    def find_element_sendkeys(driver, timeout, select, name, something):
        """滑动寻找控件输入"""
        width = driver.get_window_size().get('width')
        height = driver.get_window_size().get('height')
        if select == 'ID':
            i = 0
            while i < 10:
                try:
                    WebDriverWait(driver, timeout).until(
                        EC.presence_of_element_located((By.ID, name)),
                        message='not find this ID').send_keys(something)
                    break
                except Exception as e:
                    driver.swipe(int(width) / 2, int(height) / 2, int(width) / 2, int(height) / 8, duration=3000)
                    i = i + 1

        elif select == 'xpath':
            i = 0
            while i < 10:
                try:
                    WebDriverWait(driver, timeout).until(
                        EC.presence_of_element_located((By.XPATH, name)),
                        message='not find this xpath').send_keys(something)
                    break
                except Exception as e:
                    driver.swipe(int(width) / 2, int(height) / 2, int(width) / 2, int(height) / 8, duration=3000)
                    i = i + 1

    def find_uiautomator_tager_click(driver, tager, time, wait):
        """使用uiautomator根据tager点击

               driver:设备
               tager:目标元素
               time:滑动次数
               wait:等待时间(秒)
        """
        width = driver.get_window_size().get('width')
        height = driver.get_window_size().get('height')
        boss = 0
        while time > boss:
            try:
                   operation.element_exit_is(driver, tager, wait)
                   if driver.find_element_by_android_uiautomator(tager):
                        driver.find_element_by_android_uiautomator(tager).click()
                        print("找到目标:"+tager)
                        break
            except Exception as e:
                    driver.swipe(int(width) / 2, int(height) / 2, int(width) / 2, int(height) / 8, duration=3000)
                    boss = boss + 1
                    print("-----------------找不到目标:"+tager+",滚吧!+"+str(boss))
                    # if boss == time - 1:
                    #     driver.get_screenshot_as_file('D:/screenshot/error.png')


    def find_uiautomator_tager_send_keys(driver, tager, time, something, wait):
        """使用uiautomator根据tager输入文本

               driver:设备
               tager:目标元素
               time:滑动次数
               something: 输入文本内容
               wait:等待时间(秒)
        """
        width = driver.get_window_size().get('width')
        height = driver.get_window_size().get('height')
        boss = 0
        while time > boss:
            try:
                operation.element_exit_is(driver, tager, wait)
                if driver.find_element_by_android_uiautomator(tager):
                    driver.find_element_by_android_uiautomator(tager).send_keys(something)
                    print("找到目标:"+tager)
                    break
            except Exception as e:
                driver.swipe(int(width) / 2, int(height) / 2, int(width) / 2, int(height) / 8, duration=3000)
                boss = boss + 1
                print("------------找不到目标:"+tager+",滚吧!+"+str(boss))

    def element_exit_is(driver , tager, wait):
        """指定时间内检测元素是否存在

            driver:设备
            tager:目标指向
            wait:等待时间
        """
        star = datetime.datetime.now()
        key = True
        while key:
            try:
                if driver.find_element_by_android_uiautomator(tager):
                    print("找到了")
                    key = False
            except Exception as e:
                print("---------等一下吧，兄dai")
                time.sleep(0.5)
                end = datetime.datetime.now()
                check_time = end - star
                if  check_time.total_seconds() > wait:
                    print("大于"+str(wait)+"秒找不到了")
                    key = False

    def touch(driver, x, y):
        """根据坐标点击屏幕

            driver:设备
            x :根据uiautomator定位的x
            y :根据uiantomator定位的y
        """
        try:
            TouchAction(driver).tap(x=x, y=y).perform()
        except Exception as e:
            print("----------------点击无效")


    def photo(driver):
        """拍照"""
        iv_photo = 'resourceId("cn.smartinspection.combine:id/iv_photo_item")'
        shutter = 'resourceId("cn.smartinspection.combine:id/view_capture_button")'
        confirm = 'text("确定")'
        try:
            driver.find_element_by_android_uiautomator(iv_photo).click()
            time.sleep(0.5)
            driver.find_element_by_android_uiautomator(shutter).click()
            time.sleep(0.5)
            driver.find_element_by_android_uiautomator(confirm).click()
        except Exception as e:
            print("-------------拍照失败")



    def take_photo(driver, wait, time):
        """集成拍照"""
        width = driver.get_window_size().get('width')
        height = driver.get_window_size().get('height')
        boss = 0
        tager = 'resourceId("cn.smartinspection.combine:id/iv_photo_item")'
        while time > boss:
            try:
                operation.element_exit_is(driver, tager, wait)
                if driver.find_element_by_android_uiautomator(tager):
                    operation.photo(driver)
                    break
            except Exception as e:
                driver.swipe(int(width) / 2, int(height) / 2, int(width) / 2, int(height) / 8, duration=3000)
                boss = boss + 1
                print("------------找不到目标:"+tager+",滚吧!+"+str(boss))

    def access_visit_permissions(driver):
        """登录时获取访问权限(真机调试用)"""
        i = 0
        while i < 5:
            try:
                operation.find_uiautomator_tager_click(driver, 'text("始终允许")', 3, 3)
            except Exception as e:
                print("---------------------获取权限失败")
            i = i + 1

    def wait_loading(driver, tager, b_tager):
        """等待同步加载(没有toast情况下)

        driver:设备
        tager:同步检测的过程中的文本
        b_tager:同步检测前的文本
        """
        i = 0.5
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

    def is_toast_exist(driver, text, timeout=300, poll_frequency=0.5):
        """检测toast是否存在

        driver：设备
        text：toast弹框内容
        timeout：超时时间
        poll_frequency：间隔查询时间
        """
        try:
            message_loc = ("xpath", "//*[contains(@text,'%s')]" % text)
            WebDriverWait(driver, timeout, poll_frequency).until(EC.presence_of_element_located(message_loc))
            print("成功")
            return True
        except:
            print("--------------任务失败或者有什么别的麻烦吧")
            return False

    def get_excel_value(sheet_name):
        """execl读取操作"""
        filePath = os.path.split(os.path.dirname(__file__))[0]
        cls = []
        excel_path = filePath + '/data/testCase.xls'
        workbook = xlrd.open_workbook(excel_path)
        sheet = workbook.sheet_by_name(sheet_name)
        nrows = sheet.nrows
        for i in range(nrows):
            if sheet.row_values(i)[0] != 'case_Name':
                cls.append(sheet.row_values(i))
        return cls