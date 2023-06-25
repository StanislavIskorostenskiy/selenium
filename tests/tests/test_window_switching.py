from selenium.webdriver.common.by import By


def test_switch_to_new_window(browser):
    url = "https://demoqa.com/browser-windows"
    browser.get(url)
    browser.find_element(By.ID, "windowButton").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    result = browser.find_element(By.XPATH, "//*/body").text
    assert result == "This is a sample page"
