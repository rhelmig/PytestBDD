from pytest_bdd import scenarios, given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

'''
pytest -v -s --html=report.html
'''

# Constants

cw = 'http://sandbox.clinicwise.net/'

# Scenarios

scenarios('../Features/pytest_bdd.feature')

# Fixtures


# @pytest.fixture(scope='session')
# def driver():
#     driver = webdriver.Chrome()
#     driver.get(cw)
#     yield driver
#
#     # Teardown
#     print(" Teardown complete")

# Given Steps:


@given("an admin user is on the login page")
def login_page(driver):
    expected = "http://sandbox.clinicwise.net/"
    actual = driver.current_url
    print(actual)
    assert expected == actual


# When Steps:

@when("the user logs into Clinic Wise")
def admin_login(driver):
    driver.find_element_by_id("username").send_keys("admin")
    driver.find_element_by_id("password").send_keys("test")
    driver.find_element_by_id("signin_button").click()


# Then Steps:

@then("the user is taken to the dashboard page")
def dashboard_view(driver):
    result = driver.current_url
    print(result)
    assert result == "http://sandbox.clinicwise.net/dashboard"

#################################################


@given("an admin user is on the Clients page")
def clients_view(driver):
    driver.find_element_by_xpath("//a[@id='nav_clients']/span[@class='menu-text']").click()
    result = driver.current_url
    print(result)
    assert result == "http://sandbox.clinicwise.net/clients"


@when("the user searches by last Name")
def search_last(driver):
    driver.find_element_by_id("last_name").clear()
    driver.find_element_by_id("last_name").send_keys("Ham")


@then("a client match should be returned")
def client_listed(driver):
    WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'p')))
    assert ('Sam Hamilton' in driver.page_source)
    print(" success")
###########################################################


@given("the user has a client in view")
def client_view(driver):
    assert ('Sam Hamilton' in driver.page_source)


@when("the selects a client")
def select_client(driver):
    client = driver.find_element_by_xpath("//*[@id='client_0']")
    client.click()


@then("the client details page is returned")
def client_details(driver):
    WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'p')))
    assert driver.current_url == "http://sandbox.clinicwise.net/clients/5?search=true"
