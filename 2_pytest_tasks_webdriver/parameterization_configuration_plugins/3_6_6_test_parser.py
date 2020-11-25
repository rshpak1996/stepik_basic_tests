# pytest -s -v --browser_name=firefox pytest_tasks_webdriver\parameterization_configuration_plugins\3_6_6_test_parser.py
# pytest -s -v --browser_name=chrome pytest_tasks_webdriver\parameterization_configuration_plugins\3_6_6_test_parser.py 
link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")