import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from online_store_PageObject import OnlineStorePage


@allure.title("Тестирование покупки товаров в интернет-магазине")
@allure.description("Проверка процесса добавления товаров \
                    в корзину, заполнения формы и итоговой цены.")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_price():

    with allure.step("Подключение веб драйвера"):
        servChrom = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=servChrom)

    with allure.step("Создаем обьект PageObject"):
        site = OnlineStorePage(driver)

    with allure.step("Авторизация пользователя"):
        site.auth("standard_user", "secret_sauce")

    with allure.step("Поиск локаторов для: рюкзака, футболки, комбинезона"):
        backpack = "#add-to-cart-sauce-labs-backpack"
        tshirt = "#add-to-cart-sauce-labs-bolt-t-shirt"
        onesie = "#add-to-cart-sauce-labs-onesie"

    with allure.step("Добавление рюкзака в корзину"):
        site.add_to_cart(backpack)
    with allure.step("Добавление футболки в корзину"):
        site.add_to_cart(tshirt)
    with allure.step("Добавление комбинезона в корзину"):
        site.add_to_cart(onesie)

    with allure.step("Переход в корзину"):
        site.go_to_cart()

    with allure.step("Оформление заказа"):
        site.checkout_cart()

    with allure.step("Заполнение поля 'Имя'"):
        site.send_field("#first-name", "Anastasia")
    with allure.step("Заполнение поля 'Фамилия'"):
        site.send_field("#last-name", "Titova")
    with allure.step("Заполнение поля 'Почтовый индекс'"):
        site.send_field("#postal-code", "6000654")

    with allure.step("Отправка формы"):
        site.submit_form()

    with allure.step("Получение итоговой цены"):
        result = site.get_price()

    with allure.step("Закрытие браузера"):
        driver.quit()

    with allure.step("Проверка итоговой цены"):
        assert result == "$58.29"
