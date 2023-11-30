from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@when('Click on Cart icon')
def click_cart(context):
    context.app.main_page.click_cart()


@then('Verify "Your cart is empty" message is shown')
def verify_cart_empty_message(context):
    context.app.cart_page.verify_cart_empty_text()


