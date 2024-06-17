from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

servChrom = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service = servChrom)

driver.implicitly_wait(20)
# Перейдите на страницу
driver.get("http://uitestingplayground.com/ajax")

# Поиск кнопки
button = driver.find_element(By.CSS_SELECTOR, "#ajaxButton")
# Нажмите на синюю кнопку
button.click()

# Поиск плашки
block = driver.find_element(By.CSS_SELECTOR, ".bg-success")
# Получение текста из зеленой плашки
txt = block.text

# Вывод в консоль
print(txt)
