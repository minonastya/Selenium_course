import math
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id("num1")
    y = browser.find_element_by_id("num2")

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(int(x.text)+int(y.text)))
    button = browser.find_element_by_class_name("btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()