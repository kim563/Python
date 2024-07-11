from selenium.webdriver.common.by import By

class OnlineStorePage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")

    def auth(self, login, password):
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
    
    def add_to_cart(self, loc):
        button = self._driver.find_element(By.CSS_SELECTOR, loc)
        button.click()
    
    def go_to_cart(self):
        button_cart = self._driver.find_element(
            By.CSS_SELECTOR, ".shopping_cart_link"
        )
        button_cart.click()

    def checkout_cart(self):
        button_checkout = self._driver.find_element(
            By.CSS_SELECTOR, "#checkout"
        )
        button_checkout.click()

    def send_field(self, loc, text):
        form = self._driver.find_element(By.CSS_SELECTOR, loc)
        form.send_keys(text)

    def submit_form(self):
        button_form = self._driver.find_element(By.CSS_SELECTOR, "#continue")
        button_form.submit()
    
    def get_price(self):
        total = self._driver.find_element(
            By.CSS_SELECTOR, ".summary_total_label"
        )
        txt = total.text
        txt = txt.rsplit("Total: ", 1)
        return txt[1]
