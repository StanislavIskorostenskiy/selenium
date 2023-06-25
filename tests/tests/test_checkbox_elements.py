import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_checkbox_using(browser):
    url = "https://demoqa.com/checkbox"
    browser.get(url)
    browser.find_element(By.XPATH, "//*/li[@class='rct-node rct-node-parent rct-node-collapsed']//button").click()
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*/span[contains(text(), 'Desktop')]"))).click()
    result = browser.find_element(By.ID, "result").text
    assert result.replace("\n", " ") == "You have selected : desktop notes commands"
