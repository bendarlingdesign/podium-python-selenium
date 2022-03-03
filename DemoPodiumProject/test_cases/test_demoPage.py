import pytest
from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

"""Validates the title and header text."""

def test_text_validation():
  driver = webdriver.Chrome()
  driver.get("https://demo.podium.tools/qa-webchat-lorw/")
  driver.maximize_window()
  sleep(3)
    
  title = "QA Webchat LORW – Demo Tools"
  assert title == driver.title
  
  header_text = driver.find_element(By.XPATH, "/html/body/div[1]/h1")
  
  assert header_text.text == "All we have to decide is what to do with the time that is given us."
  print ("Test Case Passed successfully.")
  driver.quit()
