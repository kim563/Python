from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


servFF = FirefoxService(GeckoDriverManager().install())
driver = webdriver.Firefox(service = servFF)

# Откройте страницу
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

# Цикл в 5 итераций
for x in range(5):
    driver.find_element(By.TAG_NAME, "button").click()

# Нашли элементы по классу и положили их в список
delButtons = driver.find_elements(By.CLASS_NAME, "added-manually")

# Выводим в консоль длинну списка
print(len(delButtons))
