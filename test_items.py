import time
from selenium.webdriver.common.by import By


def test_add_to_cart_button_exists(browser):

    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)

    cart_button = browser.find_elements(By.CSS_SELECTOR, 'button.btn-add-to-basket')
    assert len(cart_button) != 0, 'Cart button didnt found'
    assert len(cart_button) == 1, 'Cart button selector isnt unique'
    time.sleep(10) #Ожидание для визуальной проверки языка на странице