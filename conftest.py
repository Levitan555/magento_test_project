import pytest
from selenium import webdriver
from pages.create_account import CreateAccount
from pages.orders import Orders
from pages.sale import Sale


@pytest.fixture(scope="session")
def driver():
    chrome_driver = webdriver.Chrome()
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture()
def account_creation_page(driver):
    return CreateAccount(driver)


@pytest.fixture()
def order_page(driver):
    return Orders(driver)


@pytest.fixture()
def sale_page(driver):
    return Sale(driver)
