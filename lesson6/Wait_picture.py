from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

servChrom = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service = servChrom)

# Перейдите на страницу
driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
)

# Создание обьекта waiter
waiter = WebDriverWait(driver, 40)

# Условие до появлениея 4 картинки
waiter.until(
    EC.presence_of_element_located((By.ID, "landscape"))
)

# Нахождение 3 картинки
img = driver.find_element(By.ID, "award")

# Получаем значение атрибута src
url = img.get_attribute("src")

# Вывод в консоль
print(url)
