from appium import webdriver
import Device
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

"----登录类"
class Loginel:
    "马上登录"
    loginNow = 'cn.smartinspection.combine:id/btn_go_to_login'

    "用户名"
    user_name = 'cn.smartinspection.combine:id/et_login_username'

    "密码"
    pwd = 'cn.smartinspection.combine:id/et_login_pwd'

    "企业编码"
    business_code = 'cn.smartinspection.combine:id/et_enterprise_id'

    "隐私协议"
    agree = 'cn.smartinspection.combine:id/cb_select'

    "登录"
    loginButoon = 'cn.smartinspection.combine:id/btn_login'

    "注册"
    register = 'cn.smartinspection.combine:id/tv_register'

    "重置密码"
    reset_pwd = 'cn.smartinspection.combine:id/tv_reset_password'

    "手机验证码登录"
    code = 'cn.smartinspection.combine:id/tv_reset_password'

    test = '123'

    "输入用户名"
    def sendUsename(self,username):
        driver = Device.Setting.driver
        timeout = 3
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.ID,self.user_name)),
            message='not find this ID').clear()
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.ID, self.user_name)),
            message='not find this ID').send_keys(username)
    "输入密码"
    def sendPwd(self,password):
        driver = Device.Setting.driver
        timeout = 3
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.ID, self.pwd)),
            message='not find this ID').clear()
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.ID, self.pwd)),
            message='not find this ID').send_keys(password)

    "输入企业编码"
    def sendBusinesscode(self,code):
        driver = Device.Setting.driver
        timeout = 3
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.ID, self.pwd)),
            message='not find this ID').clear()
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.ID, self.pwd)),
            message='not find this ID').send_keys(code)

    "勾选隐私协议"
    def checkAgree(self):
        driver = Device.Setting.driver
        timeout = 3
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.ID, self.agree)),
            message='not find this ID').click()

    "点击登录按钮"
    def clickLoginButoon(self):
        driver = Device.Setting.driver
        timeout = 3
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.ID, self.loginButoon)),
            message='not find this ID').click()

    "点击注册"
    def clickRegister(self):
        driver = Device.Setting.driver
        timeout = 3
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.ID, self.register)),
            message='not find this ID').click()

    "点击重置密码"
    def clickResetpwd(self):
        driver = Device.Setting.driver
        timeout = 3
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.ID, self.reset_pwd)),
            message='not find this ID').click()

    "点击手机验证码登录"
    def clickCode(self):
        driver = Device.Setting.driver
        timeout = 3
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.ID, self.code)),
            message='not find this ID').click()



#     def test2(self):
#
#         print(self.test)
#
# if __name__ == '__main__':
#     t = Loginel()
#     t.test2()
