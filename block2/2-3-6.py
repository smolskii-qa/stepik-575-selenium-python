import time
import os
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://suninjuly.github.io/redirect_accept.html'

try:
    browser = webdriver.Chrome()
    browser.get(url)

    button = browser.find_element(By.CSS_SELECTOR,'.btn.trollface')
    button.click()

    page2 = browser.window_handles[1]
    browser.switch_to.window(page2)

    x = int(browser.find_element(By.CSS_SELECTOR,'#input_value').text)
    answer = math.log(abs(12 * math.sin(x)))

    form = browser.find_element(By.CSS_SELECTOR, '#answer')
    form.send_keys(answer)

    submit = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
    submit.click()

    alert2 = browser.switch_to.alert.text
    print(alert2.split(': ')[-1])


finally:
    time.sleep(5)
    browser.quit()