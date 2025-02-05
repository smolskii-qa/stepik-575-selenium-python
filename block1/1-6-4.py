from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    in1 = browser.find_element(By.NAME, "first_name")
    in1.send_keys('Vlad')
    in2 = browser.find_element(By.NAME, "last_name")
    in2.send_keys('Smolskii')
    in3 = browser.find_element(By.CLASS_NAME, "city")
    in3.send_keys('SPB')
    in4 = browser.find_element(By.ID, "country")
    in4.send_keys('Russia')
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    alert = browser.switch_to.alert
    print(alert.text.split()[-1])


finally:
    # закрываем браузер после всех манипуляций
    browser.quit()