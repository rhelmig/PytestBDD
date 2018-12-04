from selenium import webdriver
from pytest import fixture

cw = 'http://sandbox.clinicwise.net/'


@fixture(scope='session')
def driver():
    driver = webdriver.Chrome()
    driver.get(cw)
    yield driver

    # Teardown
    print(" Teardown complete")
