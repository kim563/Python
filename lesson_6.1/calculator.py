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
    "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
)

# Поиск поля ввода
input = driver.find_element(By.CSS_SELECTOR, "#delay")
input.clear()
# Ввод в поле ввода
input.send_keys(45)

# Поиск кнопки 7
button_seven = driver.find_element(By.XPATH, "//span[text()='7']")
button_seven.click()

# Поиск кнопки +
button_plus = driver.find_element(By.XPATH, "//span[text()='+']")
button_plus.click()

# Поиск кнопки 8
button_eight = driver.find_element(By.XPATH, "//span[text()='8']")
button_eight.click()

# Поиск кнопки =
button_equals = driver.find_element(By.XPATH, "//span[text()='=']")
button_equals.click()

# Создание обьекта waiter
waiter = WebDriverWait(driver, 50)

# Задаем условие ожидания
waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
)

# Функия для проверки
def test_result():
    result = driver.find_element(By.CSS_SELECTOR, ".screen").text
    assert result == "15"
