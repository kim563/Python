import allure
from selenium import webdriver
from selenium.webdriver.common.by import By


class OnlineStorePage:
    """Класс предоставляет методы для работы с онлайн-магазином."""

    def __init__(self, driver: webdriver.Chrome):
        """
        Инициализация объекта

        args:
        driver - драйвер веб-браузера.
        """
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")

    @allure.step("Авторизация на сайте с логином {login} и паролем {password}")
    def auth(self, login: str, password: str):
        """
        Авторизация на сайте.

        args:
        login - логин пользователя,
        password - пароль пользователя.
        """
        Username = self._driver.find_element(
            By.CSS_SELECTOR, "input[name='user-name']"
        )
        Username.send_keys(login)

        Password = self._driver.find_element(
            By.CSS_SELECTOR, "input[name='password']"
        )
        Password.send_keys(password)

        button_login = self._driver.find_element(
            By.CSS_SELECTOR, "input[name='login-button']"
        )
        button_login.submit()

    @allure.step("Добавление товара в корзину с локатором: {loc}")
    def add_to_cart(self, loc: str):
        """
        Добавление товара в корзину.

        args:
        loc - локатор кнопки добавления в корзину.
        """
        button = self._driver.find_element(By.CSS_SELECTOR, loc)
        button.click()

    @allure.step("Переход в корзину")
    def go_to_cart(self):
        """
        Переход в корзину.
        """
        button_cart = self._driver.find_element(
            By.CSS_SELECTOR, ".shopping_cart_link"
        )
        button_cart.click()

    @allure.step("Оформление заказа")
    def checkout_cart(self):
        """
        Оформление заказа из корзины.
        """
        button_checkout = self._driver.find_element(
            By.CSS_SELECTOR, "#checkout"
        )
        button_checkout.click()

    @allure.step("Ввод текста '{text}' в поле с локатором: {loc}")
    def send_field(self, loc: str, text: str):
        """
        Ввод текста в поле ввода.

        args:
        loc - локатор поля ввода,
        text - текст, который нужно ввести.
        """
        form = self._driver.find_element(By.CSS_SELECTOR, loc)
        form.send_keys(text)

    @allure.step("Отправка формы")
    def submit_form(self):
        """
        Подтверждение и отправка формы.
        """
        button_form = self._driver.find_element(By.CSS_SELECTOR, "#continue")
        button_form.submit()

    @allure.step("Получение итоговой суммы")
    def get_price(self):
        """
        Получение итоговой суммы заказа.

        return:
        Итоговая сумма заказа.
        """
        total = self._driver.find_element(
            By.CSS_SELECTOR, ".summary_total_label"
        )
        txt = total.text
        txt = txt.rsplit("Total: ", 1)
        return txt[1]
