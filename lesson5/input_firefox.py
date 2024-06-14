from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

servFF = FirefoxService(GeckoDriverManager().install())
driver = webdriver.Firefox(service = servFF)

# Откройте страницу
driver.get("http://the-internet.herokuapp.com/inputs")

# Нашли элемент поля ввода и записали в переменную
input = driver.find_element(By.TAG_NAME, "input")

#Ввод 1000
input.send_keys("1000")
sleep(2)

#Очистили поле
input.clear()
sleep(2)

#Ввод 999
input.send_keys("999")
sleep(2)
