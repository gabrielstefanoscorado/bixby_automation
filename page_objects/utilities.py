from appium import webdriver
from appium import webdriver
from time import sleep

class utilities():

    def capabilities(self, driver):
            caps = {}
            caps["platformName"] = "Android"
            caps["platformVersion"] = "12"
            driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
            return driver

    def function_to_wait(self, driver):
        driver.implicitly_wait(5)

    def home_button(self, driver):
        driver.press_keycode(3)

    def back_button(self, driver):
        driver.back()

    def switch_app_button(self, driver):
        driver.press_keycode(187)

    def function_to_sleep(self):
        sleep (1)

    def screenshot(self, driver):
        sleep(5)
        
utilities_object = utilities()