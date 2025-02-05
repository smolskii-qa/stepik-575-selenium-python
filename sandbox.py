import math
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://suninjuly.github.io/explicit_wait2.html'

try:

    browser = webdriver.Chrome()
    browser.get(url)

    button = browser.find_element(By.CSS_SELECTOR, 'button#book')
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    button.click()


    x = WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.ID, 'input_value')))
    browser.execute_script("return arguments[0].scrollIntoView(true);", x)
    x = int(x.text)
    print(x)
    # x = int(browser.find_element(By.CSS_SELECTOR,'#input_value').text)
    answer = math.log(abs(12 * math.sin(x)))

    form = browser.find_element(By.CSS_SELECTOR, 'input.form-control')
    form.send_keys(answer)

    button_answer = browser.find_element(By.CSS_SELECTOR, 'button#solve')
    button_answer.click()

    alert2 = browser.switch_to.alert.text
    print(alert2.split(': ')[-1])

finally:
    time.sleep(5)
    browser.quit()