from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

servChrom = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service = servChrom)
# Перейдите на страницу
driver.get("https://www.saucedemo.com/")

# Поиск поля ввода
Username = driver.find_element(By.CSS_SELECTOR, "input[name='user-name']")
# Ввод текста в поле ввода
Username.send_keys("standard_user")

# Поиск поля ввода
Password = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
# Ввод текста в поле ввода
Password.send_keys("secret_sauce")

# Поиск кнопки login
button_login = driver.find_element(
    By.CSS_SELECTOR, "input[name='login-button']"
)

# Подтвердить отправку формы
button_login.submit()

# Поиск кнопки товара
button_backpack = driver.find_element(
    By.ID, "add-to-cart-sauce-labs-backpack"
)
button_backpack.click()

# Поиск кнопки товара
button_tshirt = driver.find_element(
    By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"
)
button_tshirt.click()

# Поиск кнопки товара
button_onesie = driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
button_onesie.click()

# Нажать на кнопку корзины
button_cart = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
button_cart.click()

# Нажать на кнопку checkout
button_checkout = driver.find_element(By.ID, "checkout")
button_checkout.click()

# Поиск поля ввода
first_name = driver.find_element(By.ID, "first-name")
# Ввод текста в поле ввода
first_name.send_keys("Anastasia")

# Поиск поля ввода
last_name = driver.find_element(By.ID, "last-name")
# Ввод текста в поле ввода
last_name.send_keys("Titova")

# Поиск поля ввода
zip_code = driver.find_element(By.ID, "postal-code")
# Ввод текста в поле ввода
zip_code.send_keys("6000654")

# Поиск кнопки continue
button_form = driver.find_element(By.ID, "continue")
# Подтвердить отправку формы
button_form.submit()

# Поиск элемента total
total = driver.find_element(By.CLASS_NAME, "summary_total_label")
# Читаем текст из элемента
txt = total.text
# Преобразуем текст в список
txt = txt.rsplit("Total: ", 1)

driver.quit()

# Функция для проверки
def test_total_assert(): 
    assert txt[1] == "$58.29"
