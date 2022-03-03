import pytest
from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver import ActionChains

"""Validates that the policy page opens."""

def test_policy_page():
    driver = webdriver.Chrome()
    driver.get("https://demo.podium.tools/qa-webchat-lorw/")
    driver.maximize_window()
    sleep(3)
    driver.switch_to.default_content()
    # # Switch to Iframe Chat Bubble
    driver.switch_to.frame("podium-bubble")
    # Click Chat Button
    webchat_button = driver.find_element(By.TAG_NAME, 'button')
    webchat_button.click()
    sleep(3)
    driver.switch_to.default_content()
    # Switch to Iframe Podium Modal
    driver.switch_to.frame("podium-modal")
    # Click Policy Link
    policy_link = driver.find_element(By.CSS_SELECTOR, '#main div.LocationSelector__PodiumPower a')
    policy_link.click()

    driver.get("https://www.podium.com/acceptable-use-policy/")
    driver.maximize_window()
    
    title = "Acceptable Use Policy - Podium"
    assert title == driver.title

    policy_header = driver.find_element(By.XPATH, "//*[@id='panel-2513-0-0-0']/div/div/h2")
    assert policy_header.text == "Podium Acceptable Use Policy"
    print ("Test Case Passed successfully.")
    driver.quit()

# test_policy_page()
