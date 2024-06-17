from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

servChrom = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service = servChrom)

# Перейдите на страницу
driver.get("http://uitestingplayground.com/textinput")

# Поиск поля ввода
input = driver.find_element(By.CSS_SELECTOR, "#newButtonName")

# Поиск кнопки
button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")

# Ввод текста в поле ввода
input.send_keys("SkyPro")

# Нажатие кнопки
button.click()

# Получение текста из кнопки
txt = button.text

# Вывод в консоль
print(txt)
