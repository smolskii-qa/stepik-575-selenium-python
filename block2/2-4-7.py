import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'http://suninjuly.github.io/wait1.html'

try:

    browser = webdriver.Chrome()
    browser.get(url)

    button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, 'verify')))
    button.click()
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text

finally:
    time.sleep(5)
    browser.quit()