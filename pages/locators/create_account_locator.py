from selenium.webdriver.common.by import By

first_name_loc = (By.ID, 'firstname')
last_name_loc = (By.ID, 'lastname')
email_loc = (By.ID, 'email_address')
password_loc = (By.ID, 'password')
confirm_password_loc = (By.ID, 'password-confirmation')
submit_loc = (By.CSS_SELECTOR, '[class="action submit primary"]')
success_text_loc = (By.CSS_SELECTOR, '[data-bind="html: $parent.prepareMessageForHtml(message.text)"]')
contact_inform_loc = (By.XPATH, '//div[@class="box box-information"]//div[@class="box-content"]/child::p')
email_address_error_loc = (By.ID, 'email_address-error')
confirm_password_error_loc = (By.ID, 'password-confirmation-error')
weak_password_error_loc = (By.ID, 'password-error')

# for test_empty_required_fill
error_locator_dict = {
    (By.ID, 'firstname-error'): first_name_loc,
    (By.ID, 'lastname-error'): last_name_loc,
    (By.ID, 'email_address-error'): email_loc,
    (By.ID, 'password-error'): password_loc,
    (By.ID, 'password-confirmation-error'): confirm_password_loc
}
