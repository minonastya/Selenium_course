import math
from selenium import webdriver
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    elements1 = browser.find_element_by_id("answer")
    elements1.send_keys(y)

    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()
    button = browser.find_element_by_class_name("btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    option2 = browser.find_element_by_id("robotsRule")
    option2.click()

    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()