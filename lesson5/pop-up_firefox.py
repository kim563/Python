from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

servFF = FirefoxService(GeckoDriverManager().install())
driver = webdriver.Firefox(service = servFF)

# Откройте страницу
driver.get("http://the-internet.herokuapp.com/entry_ad")
sleep(2)

# Нашли элемент по CSS селектору
button = driver.find_element(By.CSS_SELECTOR, ".modal-footer > p")

# Нажимаем на кнопку
button.click()
sleep(5)
