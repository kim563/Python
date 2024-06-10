from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Откройте страницу
driver.get("http://uitestingplayground.com/dynamicid")

driver.find_element(By.CLASS_NAME, "btn-primary").click() # Нажимаем на кнопку btn-primary