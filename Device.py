from appium import webdriver

class Setting:
    caps = {}
    caps["platformName"] = "Android"
    caps["platformVersion"] = "7.1.2"
    caps["deviceName"] = "MI_9"
    caps["appPackage"] = "cn.smartinspection.combine"
    caps["appActivity"] = "cn.smartinspection.login.ui.activity.WelcomeGuideActivity"
    caps["ensureWebviewsHavePages"] = True
    caps["automationName"] = "Uiautomator2"
    driver = webdriver.Remote("http://localhost:4723/wd/hub",caps)

    caps2 = {}
    caps2["platformName"] = "Android"
    caps2["platformVersion"] = "9"
    caps2["deviceName"] = "MHA_AL00"
    caps2["appPackage"] = "cn.smartinspection.combine"
    caps2["appActivity"] = "cn.smartinspection.login.ui.activity.CustomSplashActivity"
    caps2["ensureWebviewsHavePages"] = True
    caps["automationName"] = "Uiautomator2"
    driver2 = webdriver.Remote("http://localhost:4723/wd/hub",caps2)

