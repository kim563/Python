from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Form_PageObject import FormPage

servChrom = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service = servChrom)

site = FormPage(driver)

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

for o in range(9):
    site.send_field(list_filds_locator[o] , list_filds_name[o])

site.submit_form()

zip_code = site.check_color("#zip-code")

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

list_colors = []
    
for x in list_locators:
    list_colors.append(site.check_color(x))

driver.quit()

def test_zip_code():
    assert zip_code == "rgba(248, 215, 218, 1)"

def test_elements():
    for x in list_colors:
        assert x == "rgba(209, 231, 221, 1)"  
