from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Откройте страницу
driver.get("http://the-internet.herokuapp.com/login")

# Нашли элемент поля ввода и записали в переменную
username = driver.find_element(By.ID, "username")
username.send_keys("tomsmith") #Ввод tomsmith
sleep(3)

# Нашли элемент поля ввода и записали в переменную
password = driver.find_element(By.ID, "password")
password.send_keys("SuperSecretPassword!") #Ввод SuperSecretPassword!
sleep(3)

button = driver.find_element(By.CLASS_NAME, "radius")
button.click()
sleep(3)