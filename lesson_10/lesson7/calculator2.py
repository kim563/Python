import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from calculator_PageObject import CalculatorPage


@allure.title("Проверка сложения двух чисел")
@allure.description("Тест проверяет корректность \
                    сложения двух чисел на калькуляторе.")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator():

    with allure.step("Подключение веб драйвера"):
        servChrom = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=servChrom)

    with allure.step("Создаем обьект PageObject"):
        site = CalculatorPage(driver)

    with allure.step("Установка задержки для страницы калькулятора"):
        site.set_delay(45)

    with allure.step("Находим по XPATH кнопку '7'"):
        button_seven = "//span[text()='7']"
    with allure.step("Находим по XPATH кнопку '+'"):
        button_plus = "//span[text()='+']"
    with allure.step("Находим по XPATH кнопку '8'"):
        button_eight = "//span[text()='8']"
    with allure.step("Находим по XPATH кнопку '='"):
        button_equals = "//span[text()='=']"

    with allure.step("Нажимаем кнопку '7'"):
        site.click_button(button_seven)
    with allure.step("Нажимаем кнопку '+'"):
        site.click_button(button_plus)
    with allure.step("Нажимаем кнопку '8'"):
        site.click_button(button_eight)
    with allure.step("Нажимаем кнопку '='"):
        site.click_button(button_equals)

    with allure.step("Ожидание завершения спиннера"):
        site.wait_spinner()

    with allure.step("Получаем результат сложения"):
        result = site.get_result()

    with allure.step("Закрытие браузера"):
        driver.quit()

    with allure.step("Проверяем, что результат равен '15'"):
        assert result == "15"
