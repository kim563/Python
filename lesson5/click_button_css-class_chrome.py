from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Откройте страницу
driver.get("http://uitestingplayground.com/classattr")

driver.find_element(By.CLASS_NAME, "btn-primary").click() # Нажимаем на кнопку btn-primary

sleep(5)
