from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

servChrom = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service = servChrom)

# Откройте страницу
driver.get("http://the-internet.herokuapp.com/entry_ad")
sleep(2)

# Нашли элемент по CSS селектору
button = driver.find_element(By.CSS_SELECTOR, ".modal-footer > p")

# Нажимаем на кнопку
button.click()
sleep(5)
