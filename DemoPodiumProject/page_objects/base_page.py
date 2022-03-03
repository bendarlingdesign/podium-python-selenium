""" This file contains all of the selenium webdriver methods"""
import pytest
from selenium import webdriver
import sys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep


class BasePage:
    """constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # """By locators"""
    NAME = (By.ID, "Name")
    PHONE = (By.ID, "Mobile Phone")
    MESSAGE = (By.ID, "Message")

    # """Page actions"""
    # def do_search

    # def do_user_message(self, Name, Mobile Phone, Message):
    #     self.do_send_keys(self.NAME, Name)
    #     self.do_send_keys(self.PHONE, Mobile Phone)
    #     self.do_send_keys(self.MESSAGE, Message)
    #     self.do_click(self.SEND, submit)

class locators:
    
    def __init__(self, driver):
        self.driver = driver

        self.header = driver.find_element(By.XPATH, locators.header)
        self.webchat_button = driver.find_element(By.XPATH, locators.webchat_button)
        self.webchat_search = driver.find_element(By.XPATH, locators.webchat_search)
        self.webchat_location_orem = driver.find_element(By.XPATH, locators.webchat_location_orem)
        self.webchat_window = driver.find_element(By.XPATH, locators.webchat_button)
        self.webchat_close_button = driver.find_element(By.XPATH, locators.webchat_close_button)
        self.text_input_name = driver.find_element(By.XPATH, locators.text_input_name)
        self.text_input_phone = driver.find_element(By.XPATH, locators.text_input_phone)
        self.text_input_message = driver.find_element(By.XPATH, locators.text_input_message)
        self.back_arrow = driver.find_element(By.XPATH, locators.back_arrow)
        self.terms_link = driver.find_element(By.XPATH, locators.terms_link)
        self.confirmation_message = driver.find_element(By.XPATH, locators.confirmation_message)
        self.confirmation_phone = driver.find_element(By.XPATH, locators.confirmation_phone)


    def getHeader(self):
        return self.header
 
    def getWebChatButton(self):
        return self.webchat_button
 
    def getWebChatSearch(self):
        return self.webchat_search

    def getWebChatOrem(self):
        return self.webchat_location_orem

    def getWebChatWindow(self):
        return self.webchat_window

    def getWebChatClose(self):
        return self.webchat_close_button

    def getTextInputName(self):
        return self.text_input_name

    def getTextInputPhone(self):
        return self.text_input_phone

    def getTextInputMessage(self):
        return self.text_input_message

    def getBackArrow(self):
        return self.back_arrow

    def getSendButton(self):
        return self.send_button

    def getTermsLink(self):
        return self.terms_link

    def getConfirmationMessage(self):
        return self.confirmation_message

    def getConfirmationPhone(self):
        return self.confirmation_phone
        
        

    def wait_for_presence_of_all_elements(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        list_of_elements = wait.until(EC.presence_of_all_elements_located((locator_type, locator)))
        return list_of_elements

    def wait_until_element_is_clickable(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return element

    def do_click(self, locator_type):
        WebDriverWait(self.driver, 10).until(BasePage.visibility_of_element_located(locator_type)).click()

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def get_element_text(self, locator_type, text):
        element = WebDriverWait(self.driver, 10).until(BasePage.visibility_of_element_located(locator_type)).send_keys(text)
        return element.text

    def is_enabled(self, locator_type):
        element = WebDriverWait(self.driver, 10).until(BasePage.visibility_of_element_located(locator_type)).send_keys()
        return bool(element)