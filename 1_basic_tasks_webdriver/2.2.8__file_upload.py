from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import os
import pytest

link = "http://suninjuly.github.io/file_input.html"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)

    f_name = browser.find_element_by_name("firstname").send_keys("Roman")
    l_name = browser.find_element_by_name("lastname").send_keys("Shpak")
    email = browser.find_element_by_name("email").send_keys("r@sh.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 

    upload_button = browser.find_element_by_id("file").send_keys(file_path)
    submit = browser.find_element_by_tag_name("button").click()

finally:
    # закрываем браузер после всех манипуляций
    time.sleep(5)
    browser.quit()
