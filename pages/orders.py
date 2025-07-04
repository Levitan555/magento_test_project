from pages.base_page import BasePage
from pages.locators import order_locator as loc
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Orders(BasePage):
    page_url = '/collections/eco-friendly.html'

    def add_to_cart(self):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(loc.size_loc)).click()
        self.find(loc.color_loc).click()
        self.find(loc.button_add_to_cart_loc).click()
        WebDriverWait(
            self.driver, 10).until(ec.text_to_be_present_in_element(loc.counter_number_loc, '1')
                                   )
        assert self.find(loc.counter_number_loc).text == '1', 'Incorrect quantity of goods'
        assert self.find(loc.success_order_text_loc).text == 'You added Ana Running Short to your shopping cart.'

    def remove_item_from_cart(self):
        self.find(loc.counter_number_loc).click()
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(loc.remove_item_loc)).click()
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(loc.remove_modal_window_loc)).click()
        subtitle_empty = WebDriverWait(
            self.driver, 10).until(ec.visibility_of_element_located(loc.subtitle_empty_loc)
                                   )
        assert subtitle_empty.text == 'You have no items in your shopping cart.'

    def count_product_on_page(self):
        items = self.finds(loc.product_item_loc)
        assert len(items) == 12, 'The number of elements does not meet the requirements'

    def filter_color_blue(self):
        self.driver.execute_script('window.scrollTo(0, 200);')
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(loc.filter_color_loc)).click()
        button = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(loc.color_blue_loc))
        self.driver.execute_script("arguments[0].click();", button)
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(loc.product_item_loc))
        items = self.finds(loc.product_item_loc)
        for item in items:
            assert WebDriverWait(self.driver, 10).until(
                ec.visibility_of_element_located(loc.check_color_blue_loc)).get_attribute('aria-checked') == 'true'
