from utils import data as d


def test_create_account_negative_data(create_account):
    create_account.open_page()
    create_account.consent()
    create_account.iframe_window()
    create_account.create_account_fill(d.first_name, d.last_name, d.invalid_email, d.password, d.confirm_password)
    create_account.submit()
    create_account.check_email_address_error()
    create_account.create_account_fill(d.first_name, d.last_name, d.email, d.password, d.invalid_confirm_password)
    create_account.submit()
    create_account.check_invalid_confirm_password()
    create_account.create_account_fill(d.first_name, d.last_name, d.email, d.weak_password, d.weak_password)
    create_account.submit()
    create_account.check_weak_password_error()


def test_empty_required_fill(create_account):
    create_account.open_page()
    create_account.consent()
    create_account.iframe_window()
    create_account.create_account_fill(d.first_name, d.last_name, d.email, d.password, d.confirm_password)
    create_account.check_empty_required_fill()


def test_create_account(create_account):
    create_account.open_page()
    create_account.consent()
    create_account.iframe_window()
    create_account.create_account_fill(d.first_name, d.last_name, d.email, d.password, d.confirm_password)
    create_account.submit()
    create_account.check_success_create(d.first_name, d.last_name, d.email)
