
def test_user_can_add_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    add_to_basket = browser.find_element_by_id("add_to_basket_form")
    assert add_to_basket, "Looks like button doens't exist"
