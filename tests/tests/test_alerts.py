import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://demoqa.com/alerts"


@pytest.mark.skip
def test_simple_alert(browser):
    browser.get(url)
    browser.find_element(By.ID, "alertButton").click()
    browser.switch_to.alert.accept()


@pytest.mark.skip
def test_alert_with_delay(browser):
    browser.get(url)
    browser.find_element(By.ID, "timerAlertButton").click()
    WebDriverWait(browser, 30).until(EC.alert_is_present())
    browser.switch_to.alert.accept()


def test_cancel_alert(browser):
    browser.get(url)
    browser.find_element(By.ID, "confirmButton").click()
    browser.switch_to.alert.dismiss()
