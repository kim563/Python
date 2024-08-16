import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Form_PageObject import FormPage


list_filds_locator = [
    "input[name='first-name']",
    "input[name='last-name']",
    "input[name='address']",
    "input[name='e-mail']",
    "input[name='phone']",
    "input[name='city']",
    "input[name='country']",
    "input[name='job-position']",
    "input[name='company']"
]

list_filds_name = [
    "Иван",
    "Петров",
    "Ленина, 55-3",
    "test@skypro.com",
    "+7985899998787",
    "Москва",
    "Россия",
    "QA",
    "SkyPro"
]

red_color = "rgba(248, 215, 218, 1)"
green_color = "rgba(209, 231, 221, 1)"


def start_test(site: FormPage):
    with allure.step("Заполнение полей значениеми"):
        for i in range(9):
            site.send_field(list_filds_locator[i], list_filds_name[i])

    with allure.step("Подтверждение отправки формы"):
        site.submit_form()


@allure.title("Проверка цвета поля zip-code")
@allure.description("Тест проверяет правильность цвета \
                    валидации поля zip-code.")
@allure.feature("Форма")
@allure.severity(allure.severity_level.CRITICAL)
def test_zip_code():
    with allure.step("Подключение веб драйвера"):
        servChrom = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=servChrom)

    with allure.step("Создаем обьект PageObject"):
        site = FormPage(driver)

    start_test(site)

    with allure.step("Записываем цвет поля 'zip-code'"):
        zip_code = site.check_color("#zip-code")

    with allure.step("Сравниваем цвет поля 'zip_code' с красным цветом"):
        assert zip_code == red_color

    with allure.step("Закрытие браузера"):
        driver.quit()


@allure.title("Проверка цветов всех полей")
@allure.description("Тест проверяет правильность цветов \
                    валидации всех полей формы.")
@allure.feature("Форма")
@allure.severity(allure.severity_level.CRITICAL)
def test_elements():
    with allure.step("Подключение веб драйвера"):
        servChrom = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=servChrom)

    with allure.step("Создаем обьект PageObject"):
        site = FormPage(driver)

    start_test(site)

    with allure.step("Создаем список новых локаторов"):
        list_locators = [
            "#first-name",
            "#last-name",
            "#address",
            "#e-mail",
            "#phone",
            "#city",
            "#country",
            "#job-position",
            "#company"
        ]
    with allure.step("Создание пустого списка цветов элементов"):
        list_colors = []

    with allure.step("Записываем цвета элементов в список"):
        for x in list_locators:
            list_colors.append(site.check_color(x))

    with allure.step("Сравниваем цвета элементов с зеленым"):
        for x in list_colors:
            assert x == green_color

    with allure.step("Закрытие браузера"):
        driver.quit()
