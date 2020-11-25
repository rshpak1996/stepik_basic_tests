# pytest -v pytest_tasks_webdriver\parameterization_configuration_plugins\3_6_3_TASK_parametrize_links.py    
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import math
import pytest


@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()



links = ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1", "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1", "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"]

class TestStepik():
    @pytest.mark.parametrize('link', links)
    def test_opt_feedback(self, browser, link):
        browser.implicitly_wait(5)
        browser.get(link)

        answer = math.log(int(time.time()))
        input_answer = browser.find_element_by_tag_name("textarea").send_keys(str(answer))
        submit_answer = browser.find_element_by_class_name("submit-submission").click()

        opt_feedback = browser.find_element_by_class_name("smart-hints__hint").text
        assert "Correct!" in opt_feedback, f"{opt_feedback}"

