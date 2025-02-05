
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    print(x)
    y = calc(x)
    y_element = browser.find_element(By.CSS_SELECTOR, '.form-control')
    print(y)
    y_element.send_keys(y)
    option1 = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    option1.click()
    option2 = browser.find_element(By.CSS_SELECTOR,  '#robotsRule')
    option2.click()
    button = browser.find_element(By.CSS_SELECTOR, '.btn-default')
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()