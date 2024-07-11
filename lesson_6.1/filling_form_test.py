from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

servChrom = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service = servChrom)

# Перейдите на страницу
driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
)

# Поиск поля ввода
first_name = driver.find_element(By.CSS_SELECTOR, "input[name='first-name']")
# Ввод текста в поле ввода
first_name.send_keys("Иван")

# Поиск поля ввода
last_name = driver.find_element(By.CSS_SELECTOR, "input[name='last-name']")
# Ввод текста в поле ввода
last_name.send_keys("Петров")

# Поиск поля ввода
address = driver.find_element(By.CSS_SELECTOR, "input[name='address']")
# Ввод текста в поле ввода
address.send_keys("Ленина, 55-3")

# Поиск поля ввода  
email = driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']")  
# Ввод текста в поле ввода  
email.send_keys("test@skypro.com")
  
# Поиск поля ввода
phone_number = driver.find_element(By.CSS_SELECTOR, "input[name='phone']")  
# Ввод текста в поле ввода
phone_number.send_keys("+7985899998787")

# Поиск поля ввода
city = driver.find_element(By.CSS_SELECTOR, "input[name='city']")
# Ввод текста в поле ввода
city.send_keys("Москва")

# Поиск поля ввода
country = driver.find_element(By.CSS_SELECTOR, "input[name='country']")
# Ввод текста в поле ввода
country.send_keys("Россия")

# Поиск поля ввода
job_position = driver.find_element(
    By.CSS_SELECTOR, "input[name='job-position']"
)
# Ввод текста в поле ввода
job_position.send_keys("QA")

# Поиск поля ввода
company = driver.find_element(By.CSS_SELECTOR, "input[name='company']")
# Ввод текста в поле ввода
company.send_keys("SkyPro")

# Поиск кнопки submit
button_submit = driver.find_element(By.XPATH, "//button[text()='Submit']")
# Подтверждение отправки формы
button_submit.submit()

# Функция для проверки
def test_zip_code():
    # Нахождение элемента, цвет фона которого нужно проверить
    element = driver.find_element(By.ID, "zip-code")
    # Находим значение цвета у элемента
    background = element.value_of_css_property("background-color")
    # Проверяем цвет
    assert background == "rgba(248, 215, 218, 1)"

# Нахождение элементов
first_name = driver.find_element(By.ID, "first-name")
last_name = driver.find_element(By.ID, "last-name")
address = driver.find_element(By.ID, "address")
email = driver.find_element(By.ID, "e-mail")
phone_number = driver.find_element(By.ID, "phone")
city = driver.find_element(By.ID, "city")
country = driver.find_element(By.ID, "country")
job_position = driver.find_element(By.ID, "job-position")
company = driver.find_element(By.ID, "company")

# Создаем список элементов
list = [
    first_name,
    last_name,
    address,
    email,
    phone_number,
    city,
    country,
    job_position,
    company
]

# Функция для проверки
def test_elements():
    for element in list:
        backgroud = element.value_of_css_property("background-color")
        assert backgroud == "rgba(209, 231, 221, 1)"
