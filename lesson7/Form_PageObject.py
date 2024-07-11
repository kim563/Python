from selenium.webdriver.common.by import By

class FormPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )
        self._driver.implicitly_wait(4)
    
    def send_field(self, loc, text):
        # Поиск поля ввода
        field = self._driver.find_element(By.CSS_SELECTOR, loc)
        # Ввод текста в поле ввода
        field.send_keys(text)

    def submit_form(self):
        # Поиск кнопки submit
        button_submit = self._driver.find_element(
            By.XPATH, "//button[text()='Submit']"
        )
        # Подтверждение отправки формы
        button_submit.submit()

    def check_color(self, loc):
        # Нахождение элемента, цвет фона которого нужно проверить
        element = self._driver.find_element(By.CSS_SELECTOR, loc)
        # Находим значение цвета у элемента
        background = element.value_of_css_property("background-color")
        return background
