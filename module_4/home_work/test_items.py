import pytest
import time


""" ДЗ 4 часть 1  
pytest --language=es test_items.py"""
def test_guest_should_see_login_link(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    time.sleep(30)
    assert len(browser.find_elements_by_css_selector('#add_to_basket_form button')) == 1, 'Кнопки нет'
    print(browser.find_element_by_css_selector('button.btn-add-to-basket').text)
