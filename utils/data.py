import time

# for Create account page
first_name = 'Dart'
last_name = 'Vader'
email = f'dart_vader{int(time.time())}@gmail.com'
invalid_email = 'dart_vader.gmail.com'
password = 'W12345678*'
confirm_password = 'W12345678*'
weak_password = '1234'
invalid_confirm_password = 'W12345678'

success_registration_expected_text = 'Thank you for registering with Main Website Store.'
email_address_error_expected_text = 'Please enter a valid email address (Ex: johndoe@domain.com).'
confirm_password_error_expected_text = 'Please enter the same value again.'
weak_password_error_expected_text = ('Minimum length of this field must be equal or greater than 8 symbols. '
                                     'Leading and trailing spaces will be ignored.')
empty_required_fill_expected_text = 'This is a required field.'

# for Sale page
sale_main = 'https://magento.softwaretestingboard.com/pub/media/wysiwyg/sale/sale-main.jpg'
sale_mens = 'https://magento.softwaretestingboard.com/pub/media/wysiwyg/sale/sale-mens.jpg'
sale_gear = 'https://magento.softwaretestingboard.com/pub/media/wysiwyg/sale/sale-gear.jpg'
sale_promo20 = 'https://magento.softwaretestingboard.com/pub/media/wysiwyg/sale/sale-20-off.png'
sale_promo_free = 'https://magento.softwaretestingboard.com/pub/media/wysiwyg/womens/womens-t-shirts.png'
finish_page_title_data = ['Women Sale', 'Men Sale', 'Gear', 'Tees']

# for Orders page
subtitle_empty_text = 'You have no items in your shopping cart.'
success_order_text = 'You added Ana Running Short to your shopping cart.'
