from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Откройте страницу
driver.get("http://the-internet.herokuapp.com/entry_ad")

sleep(2)

driver.find_element(By.CSS_SELECTOR, ".modal-footer > p").click() # Нажимаем на кнопку btn-primary

sleep(5)