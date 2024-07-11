from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

    def set_delay(self, numb):
        # Поиск поля ввода
        delay_input = self._driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(numb)

    def click_button(self, loc):
        # Поиск кнопки
        button = self._driver.find_element(By.XPATH, loc)
        # Нажатие кнопки
        button.click()

    def wait_spinner(self):
        # Создание обьекта waiter
        waiter = WebDriverWait(self._driver, 50)

        # Задаем условие ожидания
        waiter.until(
            EC.invisibility_of_element_located((By.ID, "spinner"))
        )

    def get_result(self):
        #Получает результат из экрана калькулятора
        return self._driver.find_element(By.CSS_SELECTOR, ".screen").text
