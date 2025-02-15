from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
import math

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x1 = int(browser.find_element(By.CSS_SELECTOR, '#num1').text)
    x2 = int(browser.find_element(By.CSS_SELECTOR, '#num2').text)
    answer = x1 + x2

    dropdown = Select(browser.find_element(By.CSS_SELECTOR, '#dropdown'))
    dropdown.select_by_value(str(answer))

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()