from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

servFF = FirefoxService(GeckoDriverManager().install())
driver = webdriver.Firefox(service = servFF)

# Откройте страницу
driver.get("http://uitestingplayground.com/dynamicid")

# Поиск элемента "Кнопка"
button = driver.find_element(By.CLASS_NAME, "btn-primary")

# Нажимаем на кнопку
button.click()
