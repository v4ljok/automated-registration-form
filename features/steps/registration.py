from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php'

@given('Users launch chrome browser')
def step_impl(context):
    print('Users launch chrome browser')

    options = webdriver.ChromeOptions()
    context.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

@when('Users open form webpage')
def step_impl(context):
    print('Users open form webpage')
    
    context.driver.get(url)

@then('Users enter user name')
def step_impl(context):
    print('Users enter user name')
    
    name_field = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'name')))
    name_field.send_keys('Valentin')

@then('Users enter email')
def step_impl(context):
    print('Users enter email')
    
    email_field = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'email')))
    email_field.send_keys('v4ljok.c@gmail.com')

@then('Users choose Gender')
def step_impl(context):
    print('Users choose Gender')

    male_radio_option = context.driver.find_element(By.ID, 'gender')
    male_radio_option.click()

@then('Users Enter mobile number')
def step_impl(context):
    print('Users Enter mobile number')

    mobile_field = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'mobile')))
    mobile_field.send_keys('+372 4567890')

@then('Users choose date of birth')
def step_impl(context):
    print('Users choose date of birth')

    dob_field = context.driver.find_element(By.ID,'dob')
    dob_field.send_keys('01-01-2002')

@then('Users Enter subject')
def step_impl(context):
    print('Users Enter subject')

    subject_field = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'subjects')))
    subject_field.send_keys('Software Testing')

@then('Users choose hobbies')
def step_impl(context):
    print('Users choose hobbies')

    hobby_checkbox = context.driver.find_element(By.ID, "hobbies")
    hobby_checkbox.click()

@then('Users choose file')
def step_impl(context):
    print('Users choose file')
    
    file_field = context.driver.find_element(By.ID, 'picture')
    file_field.send_keys('C:\\Users\\Unluc\\Desktop\\automated-registration-form\\img\\avatar.png')

@then('Users Enter current address')
def step_impl(context):
    print('Users Enter current address')

    address_field = context.driver.find_element(By.TAG_NAME,'textarea')
    address_field.send_keys('3805 Larchmont Ln')

@then('Users choose state and city')
def step_impl(context):
    print('Users choose state and city')

    state_dropdown = context.driver.find_element(By.NAME, 'state')
    state_dropdown.send_keys('NCR')

    city_dropdown = context.driver.find_element(By.ID, 'city')
    city_dropdown.send_keys('Agra')

@then('Users click the login button')
def step_impl(context):
    print('Users click the login button')

    login_button = context.driver.find_element(By.XPATH, "//input[@value='Login']")
    login_button.click()

    context.driver.quit()