from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


COLOR_OPTIONS = (By.CSS_SELECTOR, "[class*='styles__ButtonWrapper-sc-519sqw-1'] img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[class*='StyledVariationSelectorImage'] [class*='CellVariationHeaderWrapper']")


@given('Open target product A-88618172')
def open_target(context):
    context.driver.get('https://www.target.com/p/women-s-seamless-jersey-t-shirt-a-new-day/-/A-88618172')
    sleep(6)


@then('Verify user can click through colors')
def click_and_verify_colors(context):
    expected_colors = ['Black', 'Green', 'Lime Green', 'Olive', 'White', 'Brown', 'Burgundy', 'Teal']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)
    for color in colors:
        color.click()
        selected_colors = context.driver.find_element(*SELECTED_COLOR).text.split('\n')[1]
        actual_colors.append(selected_colors)

    print(actual_colors)


@given('Open target product A-89191279')
def open_target_(context):
    context.driver.get('https://www.target.com/p/A-89191279')
    sleep(6)


@given('Open target product A-88345426')
def open_target_(context):
    context.driver.get('https://www.target.com/p/A-88345426')
    sleep(6)

