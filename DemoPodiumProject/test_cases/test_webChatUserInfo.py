import pytest
from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

"""Validates that the use can enter and submit their valid user information and receive a message."""

def test_webchat_user_info():
    driver = webdriver.Chrome()
    driver.get("https://demo.podium.tools/qa-webchat-lorw/")
    driver.maximize_window()
    sleep(3)

    # Switch to Iframe Chat Bubble
    driver.switch_to.default_content()
    driver.switch_to.frame("podium-bubble")
    # Click Chat Button
    webchat_button = driver.find_element(By.TAG_NAME, 'button')
    webchat_button.click()
    sleep(3)

    # Switch to Iframe Chat Modal
    driver.switch_to.default_content()
    driver.switch_to.frame("podium-modal")
    # Click Orem Location
    webchat_orem_location = driver.find_element(By.XPATH, "//*[@id='main']/div/div/div/div/div/div/div/div[2]/div/button[4]")
    webchat_orem_location.click()
    sleep(3)

    #Enter User Information and Submit 
    user_name = driver.find_element(By.ID, "Name")
    user_name.click()
    user_name.send_keys("Frodo")
    # user_name.send_keys(Keys.TAB)

    user_phone = driver.find_element(By.ID, "Mobile Phone")
    user_phone.click()
    user_phone.send_keys("8016045533")

    user_message = driver.find_element(By.ID, "Message")
    user_message.click()
    user_message.send_keys("SAAMMM")

    # Validate the message was received
    submit_button = driver.find_element(By.CSS_SELECTOR, '#ComposeMessage div.SendSmsPage__Center button')
    submit_button.click()
    sleep(5)
    
    message_received_phone = driver.find_element(By.CLASS_NAME, 'ConfirmationMessage__PhoneNumber')
    assert message_received_phone.text == "+1 385 304 3267"
    
    print ("Test Case Passed successfully.")
    driver.quit()
