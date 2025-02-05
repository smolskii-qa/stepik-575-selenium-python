from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/huge_form.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    inputs = browser.find_elements(By.CSS_SELECTOR, ".first_block input")
    for i in inputs:
        i.send_keys('qwerty')

    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()

    alert = browser.switch_to.alert
    print(alert.text.split()[-1])


finally:
    # закрываем браузер после всех манипуляций
    browser.quit()