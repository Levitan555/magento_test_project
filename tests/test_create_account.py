from utils import data as d


def test_create_account_with_negative_data(account_creation_page):
    account_creation_page.open_page()
    account_creation_page.approve_window_consent()
    account_creation_page.closing_iframe_window()
    account_creation_page.create_account_fill(d.first_name, d.last_name, d.invalid_email, d.password, d.confirm_password)
    account_creation_page.submit()
    account_creation_page.check_email_address_error()
    account_creation_page.create_account_fill(d.first_name, d.last_name, d.email, d.password, d.invalid_confirm_password)
    account_creation_page.submit()
    account_creation_page.check_invalid_confirm_password()
    account_creation_page.create_account_fill(d.first_name, d.last_name, d.email, d.weak_password, d.weak_password)
    account_creation_page.submit()
    account_creation_page.check_weak_password_error()


def test_empty_required_fill(account_creation_page):
    account_creation_page.open_page()
    account_creation_page.approve_window_consent()
    account_creation_page.closing_iframe_window()
    account_creation_page.create_account_fill(d.first_name, d.last_name, d.email, d.password, d.confirm_password)
    account_creation_page.check_empty_required_fill()


def test_create_account(account_creation_page):
    account_creation_page.open_page()
    account_creation_page.approve_window_consent()
    account_creation_page.closing_iframe_window()
    account_creation_page.create_account_fill(d.first_name, d.last_name, d.email, d.password, d.confirm_password)
    account_creation_page.submit()
    account_creation_page.check_success_create(d.first_name, d.last_name, d.email)
