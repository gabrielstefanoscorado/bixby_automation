from lib2to3.pgen2 import driver
from appium.webdriver.webdriver import WebDriver
from hashlib import new
from appium import webdriver
from pyclbr import Class
from appium.webdriver import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.actions import *
from time import sleep
from selenium.webdriver.common.actions import interaction
from appium.webdriver.common.touch_action import TouchAction
from page_objects.home_page import home_page_object
from page_objects.utilities import utilities_object

class gradingAutomation():
        
        driver = utilities_object.capabilities()

        utilities_object.capabilities(driver)

        
        home_page_object.bixby_click(driver)
        utilities_object.function_to_wait(driver)
        home_page_object.keyboard_click(driver)
        home_page_object.input_text_and_send(driver, "Hi bixby")
        home_page_object.run_button_click(driver)
        sleep(5)
        utilities_object.home_button(driver)
        utilities_object.function_to_wait(driver)
        home_page_object.bixby_click(driver)
        home_page_object.long_press_button(driver)
        sleep(1)
        utilities_object.back_button(driver)
        home_page_object.click_log_of_utterance(driver)
        home_page_object.swipe_screen(driver)
        home_page_object.get_conversation_id(driver)
        utilities_object.switch_app_button(driver)
        home_page_object.close_all_button(driver)

       