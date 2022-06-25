import time

def test_items(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    time.sleep(30)
    btn = browser.find_element_by_css_selector(".btn-add-to-basket").is_enabled()
    assert btn, "button is missing"