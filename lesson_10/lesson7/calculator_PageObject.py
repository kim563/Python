import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """Класс предоставляет методы для работы с калькулятором"""

    def __init__(self, driver: webdriver.Chrome):
        """
        Инициализация обьекта

        args:
        driver - драйвер веб браузера.
        """
        self._driver = driver
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-\
                java/slow-calculator.html"
        )

    @allure.step("Установка задержки в поле ввода задержки: {numb}")
    def set_delay(self, numb: int):
        """
        Установка задержки в поле ввода задержки.

        args:
        numb - значение для поля ввода задержки (время ожидания в секундах).
        """
        delay_input = self._driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(numb)

    @allure.step("Нажатие на кнопку с локатором: {loc}")
    def click_button(self, loc: str):
        """
        Поиск кнопки по локатору,
        Нажатие на конопку.

        args:
        log - локатор кнопки
        """
        button = self._driver.find_element(By.XPATH, loc)
        button.click()

    @allure.step("Ожидание окончания загрузки (спиннера)")
    def wait_spinner(self):
        """
        Задаем условие ожидания, окончания загрузки (спиннера)

        """
        waiter = WebDriverWait(self._driver, 50)
        waiter.until(
            EC.invisibility_of_element_located((By.ID, "spinner"))
        )

    @allure.step("Получение результата калькулятора")
    def get_result(self):
        """
        Получает результат из экрана калькулятора.

        Возвращает:
        text: str - строковое значение результата.
        """
        return self._driver.find_element(By.CSS_SELECTOR, ".screen").text
