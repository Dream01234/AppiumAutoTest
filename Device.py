from appium import webdriver

class Setting:
    caps = {}
    caps["platformName"] = "Android"
    caps["platformVersion"] = "7.1.2"
    caps["deviceName"] = "MI_9"
    caps["appPackage"] = "cn.smartinspection.combine"
    caps["appActivity"] = "cn.smartinspection.login.ui.activity.WelcomeGuideActivity"
    caps["ensureWebviewsHavePages"] = True

    driver = webdriver.Remote("http://localhost:4723/wd/hub",caps)
