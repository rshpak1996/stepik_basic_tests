from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select # для випадаючих меню
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # для конкретних очікуваних подій
import time
import math
import os
import pytest

link = "    "


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)


finally:
    # закрываем браузер после всех манипуляций
    time.sleep(5)
    browser.quit()
