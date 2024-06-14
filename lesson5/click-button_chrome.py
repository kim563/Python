from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

servChrom = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service = servChrom)

# Откройте страницу
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

# Цикл в 5 итераций
for x in range(5):
    driver.find_element(By.TAG_NAME, "button").click()

# Нашли элементы по классу и положили их в список
delButtons = driver.find_elements(By.CLASS_NAME, "added-manually")

# Выводим в консоль длинну списка
print(len(delButtons))
