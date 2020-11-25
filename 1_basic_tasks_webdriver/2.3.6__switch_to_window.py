from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import os
import pytest

link = "http://suninjuly.github.io/redirect_accept.html"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)

    button1 = browser.find_element_by_class_name("trollface").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    answer = browser.find_element_by_id("answer").send_keys(y)
    submit = browser.find_element_by_class_name("btn").click()



finally:
    # закрываем браузер после всех манипуляций
    time.sleep(5)
    browser.quit()
