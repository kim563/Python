from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from online_store_PageObject import OnlineStorePage

servChrom = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service = servChrom)

site = OnlineStorePage(driver)

site.auth("standard_user", "secret_sauce")

backpack = "#add-to-cart-sauce-labs-backpack"
tshirt = "#add-to-cart-sauce-labs-bolt-t-shirt"
onesie = "#add-to-cart-sauce-labs-onesie"

site.add_to_cart(backpack)
site.add_to_cart(tshirt)
site.add_to_cart(onesie)

site.go_to_cart()

site.checkout_cart()

site.send_field("#first-name", "Anastasia")
site.send_field("#last-name", "Titova")
site.send_field("#postal-code", "6000654")

site.submit_form()

result = site.get_price()

driver.quit()

def test_price():
    assert result == "$58.29"
