from appium import webdriver

class Setting:
    caps = {}
    caps["platformName"] = "Android"
    caps["platformVersion"] = "10"
    caps["deviceName"] = "nova 8"
    caps["appPackage"] = "cn.smartinspection.combine"
    caps["appActivity"] = "cn.smartinspection.login.ui.activity.CustomSplashActivity"
    caps["ensureWebviewsHavePages"] = True
    caps["automationName"] = "Uiautomator2"
    driver = webdriver.Remote("http://localhost:4723/wd/hub",caps)

