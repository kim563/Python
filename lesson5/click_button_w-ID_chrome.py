from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

servChrom = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service = servChrom)

# Откройте страницу
driver.get("http://uitestingplayground.com/dynamicid")

# Поиск элемента "Кнопка"
button = driver.find_element(By.CLASS_NAME, "btn-primary")

# Нажимаем на кнопку
button.click()
