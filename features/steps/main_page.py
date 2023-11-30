from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


SEARCH_FIELD = (By.ID, 'search')
SEARCH_BTN = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
HEADER = (By.CSS_SELECTOR, '[class*="styles__UtilityHeaderWrapper"]')
HEADER_LINKS = (By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader']")


@given("Open target main page")
def open_target(context):
    context.app.main_page.open_main()
    #context.driver.get('https://www.target.com/')


@when('Search for {product}')
def search_product(context, product):
    context.app.main_page.search(product)
    #context.driver.find_element(*SEARCH_FIELD).send_keys(product)
    #context.driver.find_element(*SEARCH_BTN).click()
    #sleep(6)


@then('Verify header is present')
def verify_header_present(context):
    context.driver.find_element(*HEADER) #partial match


@then('Verify header has {number} links')
def verify_header_links(context, number):
    print(type(number))
    number = int(number) #becasue we put 5 in the steps and it pucharm takes it as a string and our assertion will fail
    print(type(number))
    links = context.driver.find_elements(*HEADER_LINKS)
    print(links)
    assert len(links) == number, f"Expected {number} links, but got {len(links)}"
