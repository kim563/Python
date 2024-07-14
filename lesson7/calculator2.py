from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from calculator_PageObject import CalculatorPage

servChrom = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service = servChrom)

site = CalculatorPage(driver)

site.set_delay(45)

button_seven = "//span[text()='7']"
button_plus = "//span[text()='+']"
button_eight = "//span[text()='8']"
button_equals = "//span[text()='=']"

site.click_button(button_seven)
site.click_button(button_plus)
site.click_button(button_eight)
site.click_button(button_equals)

site.wait_spinner()

result = site.get_result()

driver.quit()

def test_result():
    assert result == "15"
