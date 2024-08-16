from selenium import webdriver
import allure
from selenium.webdriver.common.by import By


class FormPage:
    """Класс предоставляет методы для работы с формой на странице"""

    def __init__(self, driver: webdriver.Chrome):
        """
        Инициализация объекта

        args:
        driver - драйвер веб-браузера.
        """
        self._driver = driver
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )
        self._driver.implicitly_wait(4)

    @allure.step("Ввод текста {text} в поле ввода с локатором: {loc}")
    def send_field(self, loc: str, text: str):
        """
        Ввод текста в поле ввода.

        args:
        loc - локатор поля ввода,
        text - текст, который нужно ввести.
        """
        field = self._driver.find_element(By.CSS_SELECTOR, loc)
        field.send_keys(text)

    @allure.step("Отправка формы")
    def submit_form(self):
        """
        Поиск кнопки submit,
        Подтверждение отправки формы.

        """
        button_submit = self._driver.find_element(
            By.XPATH, "//button[text()='Submit']"
        )
        button_submit.submit()

    @allure.step("Проверка цвета фона элемента с локатором: {loc}")
    def check_color(self, loc: str):
        """
        Нахождение элемента, цвет фона которого нужно проверить,
        Находим значение цвета у элемента.

        args:
        loc - локатор элемента.

        return:
        Цвет фона элемента.
        """
        element = self._driver.find_element(By.CSS_SELECTOR, loc)
        background = element.value_of_css_property("background-color")
        return background
