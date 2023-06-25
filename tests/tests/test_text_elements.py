import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def window_scrolling(browser, pos):
    browser.execute_script(f"window.scrollTo(0, {pos})")


def test_elements_button(browser):
    url = "https://demoqa.com/"
    browser.get(url)
    browser.find_element(By.XPATH, "//*/div/*[@viewBox='0 0 448 512']").click()
    elements_text = browser.find_element(By.XPATH, "//*/div[@class='main-header']").text
    assert elements_text == "Elements"


def test_text_box_input(browser):
    test_name = "testusername"
    url = "https://demoqa.com/text-box"
    browser.get(url)
    browser.find_element(By.ID, "userName").send_keys(test_name)
    browser.find_element(By.ID, "userEmail").send_keys("test@mail.ru")
    browser.find_element(By.ID, "currentAddress").send_keys("testaddress")
    browser.find_element(By.ID, "permanentAddress").send_keys("testpermaddress")
    window_scrolling(browser, 100)
    button = WebDriverWait(browser, 100).until(EC.element_to_be_clickable((By.ID, "submit")))
    button.click()
    result = browser.find_element(By.ID, "name").text
    assert result[5:] == test_name, f'expected {test_name}, actual {result}'


invalid_email_list = ["a", "a@", "a@mail", "amail.ru"]


@pytest.mark.parametrize("email", invalid_email_list)
def test_email_validation_input(browser, email):
    url = "https://demoqa.com/text-box"
    browser.get(url)
    browser.find_element(By.ID, "userEmail").send_keys(email)
    window_scrolling(browser, 100)
    button = WebDriverWait(browser, 100).until(EC.element_to_be_clickable((By.ID, "submit")))
    button.click()
    error_attr_result = browser.find_element(By.ID, "userEmail").get_attribute("class")
    assert error_attr_result == "mr-sm-2 field-error form-control"
