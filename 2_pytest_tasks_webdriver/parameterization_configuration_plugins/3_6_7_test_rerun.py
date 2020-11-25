# pytest -v --tb=line --reruns 1 --browser_name=chrome pytest_tasks_webdriver\parameterization_configuration_plugins\3_6_7_test_rerun.py

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")

def test_guest_should_see_login_link_fail(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#magic_link")
    