from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Откройте страницу
driver.get("http://the-internet.herokuapp.com/inputs") 

# Нашли элемент поля ввода и записали в переменную
input = driver.find_element(By.TAG_NAME, "input")


input.send_keys("1000") #Ввод 1000
sleep(2)
input.clear() #Очистили поле
sleep(2)
input.send_keys("999") #Ввод 999
sleep(2)