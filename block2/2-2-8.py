import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://suninjuly.github.io/file_input.html'

try:
    # current_dir = os.path.abspath(os.path.dirname(__file__))
    current_dir = os.getcwd()
    # file_path = os.path.join(current_dir, 'test.txt')
    file_path = current_dir + '/' + 'test.txt'

    browser = webdriver.Chrome()
    browser.get(url)

    fname = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
    fname.send_keys('Vlad')

    lname = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
    lname.send_keys('Secret')

    email = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    email.send_keys('apple@apple.com')

    upload = browser.find_element(By.CSS_SELECTOR, '[type="file"]')
    upload.send_keys(file_path)

    submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit.click()


finally:
    time.sleep(5)
    browser.quit()