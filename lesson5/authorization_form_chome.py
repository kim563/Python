from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

servChrom = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service = servChrom)

# Открыть страницу
driver.get("http://the-internet.herokuapp.com/login")

# Нашли элемент поля ввода и записали в переменную
username = driver.find_element(By.ID, "username")

#Ввод tomsmith
username.send_keys("tomsmith")
sleep(3)

# Нашли элемент поля ввода и записали в переменную
password = driver.find_element(By.ID, "password")

#Ввод SuperSecretPassword!
password.send_keys("SuperSecretPassword!")
sleep(3)

button = driver.find_element(By.CLASS_NAME, "radius")
button.click()
sleep(3)
