from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v85.dom import get_attributes
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button = browser.find_element(By.ID, "book")
    button.click()
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    print(x)
    y = calc(x)
    y_element = browser.find_element(By.CSS_SELECTOR, '.form-control')
    print(y)
    y_element.send_keys(y)
    button2 = browser.find_element(By.ID, "solve")
    button2.click()





finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()