import pytest
from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

"""Validates that the web chat button can be selected and search by zip code."""

def test_webchat_zip_validation():
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
    # Click X button to Clear Zip
    webchat_xbutton = driver.find_element(By.CLASS_NAME, 'SearchInput__Reset')
    webchat_xbutton.click()

    # Click into Search Container to Enter Zip
    webchat_search_container = driver.find_element(By.NAME, 'Search Locations')
    webchat_search_container.click()
    webchat_search_container.send_keys("84663")
    sleep(3)

    print ("Test Case Passed successfully.")
    driver.quit()

    