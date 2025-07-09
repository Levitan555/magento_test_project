from pages.base_page import BasePage
from pages.locators import create_account_locator as loc
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from utils.data import success_registration_expected_text
from utils.data import email_address_error_expected_text
from utils.data import confirm_password_error_expected_text
from utils.data import weak_password_error_expected_text
from utils.data import empty_required_fill_expected_text


class CreateAccount(BasePage):
    page_url = '/customer/account/create/'

    def create_account_fill(self, first_name, last_name, email, password, confirm_password):
        first_name_fill = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(loc.first_name_loc))
        last_name_fill = self.find(loc.last_name_loc)
        email_fill = self.find(loc.email_loc)
        password_fill = self.find(loc.password_loc)
        confirm_password_fill = self.find(loc.confirm_password_loc)
        first_name_fill.send_keys(first_name)
        last_name_fill.send_keys(last_name)
        email_fill.send_keys(email)
        password_fill.send_keys(password)
        confirm_password_fill.send_keys(confirm_password)

    def check_success_create(self, first_name, last_name, email):
        success_text = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(loc.success_text_loc))
        assert success_text.text == success_registration_expected_text
        contact_inform = self.find(loc.contact_inform_loc)
        assert contact_inform.text == f'{first_name} {last_name}\n{email}'

    def check_email_address_error(self):
        email_address_error = self.find(loc.email_address_error_loc)
        assert email_address_error.text == email_address_error_expected_text
        self.clear_fills()

    def check_invalid_confirm_password(self):
        confirm_password_error = self.find(loc.confirm_password_error_loc)
        assert confirm_password_error.text == confirm_password_error_expected_text
        self.clear_fills()

    def check_weak_password_error(self):
        weak_password_error = self.find(loc.weak_password_error_loc)
        assert weak_password_error.text == weak_password_error_expected_text
        self.clear_fills()

    def check_empty_required_fill(self):
        for error_locator, field_locator in loc.error_locator_dict.items():
            field_text = self.find(field_locator).get_attribute('value')
            self.clear_fill(field_locator)
            self.submit()
            error_text = self.find(error_locator)
            assert error_text.text == empty_required_fill_expected_text, \
                f'Expected error message not found for {error_locator}'
            self.find(field_locator).send_keys(field_text)

    def clear_fills(self):
        self.find(loc.first_name_loc).clear()
        self.find(loc.last_name_loc).clear()
        self.find(loc.email_loc).clear()
        self.find(loc.password_loc).clear()
        self.find(loc.confirm_password_loc).clear()

    def clear_fill(self, locator):
        self.find(locator).clear()

    def submit(self):
        self.find(loc.submit_loc).click()
