from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

class results:

    def is_element_exist(driver, timeout, select, name):
        if select == 'ID':
                if WebDriverWait(driver, timeout).until(
                        expected_conditions.presence_of_element_located((By.ID, name))):
                    return True
                else :
                    return False

        elif select == 'xpath':
                    if WebDriverWait(driver, timeout).until(
                            expected_conditions.presence_of_element_located((By.XPATH, name)),
                                message='not find this XPATH'):
                        return True
                    else:
                        return False


    def is_exist(driver, tager):
        """判断元素是否存在"""
        if driver.find_element_by_android_uiautomator(tager):
            return True
        else:
            return False



