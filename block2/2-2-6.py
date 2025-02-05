import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    link = "https://suninjuly.github.io/execute_script.html"
    browser.get(link)

    x = int(browser.find_element(By.CSS_SELECTOR, '#input_value').text)
    answer = math.log(abs(12 * math.sin(x)))

    answer_input = browser.find_element(By.CSS_SELECTOR, '#answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer_input)
    answer_input.send_keys(str(answer))

    browser.find_element(By.CSS_SELECTOR, '#robotCheckbox').click()
    browser.find_element(By.CSS_SELECTOR, '#robotsRule').click()


    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script('return arguments[0].scrollIntoView(true);', button)
    # time.sleep(3)
    button.click()
finally:
    time.sleep(5)
    browser.quit()