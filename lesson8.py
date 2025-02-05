
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try:
    link = "https://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    num1_element = browser.find_element(By.CSS_SELECTOR, '#num1')
    num1 = num1_element.text
    num2_element = browser.find_element(By.CSS_SELECTOR, '#num2')
    num2 = num2_element.text
    print(num1,num2)
    sum = int(num1) + int(num2)
    print(sum)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(sum))
    button = browser.find_element(By.CSS_SELECTOR, '.btn-default')
    c
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()




