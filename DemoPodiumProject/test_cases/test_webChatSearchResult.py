import pytest
from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

"""Validates that the web chat search results can be selected and open chat."""

def test_webchat_search_result():
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

    location_address = driver.find_element(By.CLASS_NAME, 'SendSmsPage__CurrentLocationAddress')
    assert location_address.text == "Scoreboard Sports - Orem"
    sleep(3)

    print ("Test Case Passed successfully.")
    driver.quit()
