from asyncio import sleep
from lib2to3.pgen2 import driver
from selenium.webdriver.common.actions import *
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput


class HomePage():
    bixby_button = "Bixby"
    keyboard_button = "Keyboard"
    text_field = "//*[@text = 'Type to Bixby']"
    run_button = "Run command"
    log_utterance = "//*[contains(@text,'2022')]"
    conversation_id = "//*[contains(@text,'tr-')]"
    close_all = "//*[@text = 'Close all']"
    
    
    def bixby_click(self, driver):
        driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=HomePage.bixby_button).click()
        driver.implicitly_wait(5)

    def keyboard_click(self, driver):
        driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=HomePage.keyboard_button).click()

    def input_text_and_send(self, driver, Utterance):
        driver.find_element(by=AppiumBy.XPATH, value=HomePage.text_field).send_keys(Utterance)

    def run_button_click(self, driver):
        driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=HomePage.run_button).click()
        sleep(5)

    def long_press_button(self, driver):
        actions = TouchAction(driver)
        actions.long_press(driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value= HomePage.keyboard_button))
        actions.perform()
    
    def click_log_of_utterance(self, driver):
        driver.find_element(by=AppiumBy.XPATH, value=HomePage.log_utterance).click()

    def swipe_screen(self, driver):
        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(475, 2114)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(483, 373)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

    def get_conversation_id(self, driver):
        conversation = driver.find_element(by=AppiumBy.XPATH, value=HomePage.conversation_id)
        conversation_string = conversation.text
        print(conversation_string)
        return conversation_string

    def close_all_button(self, driver):
        driver.find_element(by=AppiumBy.XPATH, value=HomePage.close_all).click()


home_page_object = HomePage()
    



