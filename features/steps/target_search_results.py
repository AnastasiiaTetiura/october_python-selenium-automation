from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@then("Verify search worked for {product}")
def verify_search(context, product):
    context.app.search_results_page.verify_search_result(product)
    #search_result_header = context.driver.find_element(By.CSS_SELECTOR, "[data-test='resultsHeading']").text
    #assert product in search_result_header, f'Expected text {product} not in {search_result_header}'


@then("Verify {expected_keyword} in search results url")
def verify_search_url(context, expected_keyword):
    context.app.search_results_page.verify_search_url(expected_keyword)
    #assert expected_keyword in context.driver.current_url, \
        #f"Expected {expected_keyword} not in {context.driver.current_url}"



