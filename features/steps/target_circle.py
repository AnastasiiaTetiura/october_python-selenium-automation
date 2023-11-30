from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

TARGET_CIRCLE = (By. CSS_SELECTOR, "[data-test*='/UtilityHeader/TargetCircle']")
BENEFITS_BOXES = (By.CSS_SELECTOR, "[class='styles__BenefitCard-sc-9mx6dj-2 lgQxFm']")


@when("Click Target Circle")
def click_target_circle(context):
    context.driver.find_element(*TARGET_CIRCLE).click()


@then("Verify there are {number} boxes")
def verify_benefit_boxes(contex, number):
    number = int(number)
    boxes = contex.driver.find_elements(*BENEFITS_BOXES)
    assert len(boxes) == number, f"Expected {number} of benefits boxes, but got {len(boxes)}"

@given("Open Circle page")
def open_circle(context):
    context.app.circle_page.open_circle()


@then("Verify that clicking through tabs works")
def verify_can_click_tabs(context):
    context.app.circle_page.verify_can_click_tabs()
