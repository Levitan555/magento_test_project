from pages.base_page import BasePage
from pages.locators import sale_locator as loc
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from utils import data as d


class Sale(BasePage):
    page_url = '/sale.html'

    def check_images(self):
        assert self.find(loc.sale_main_img_loc).get_attribute('src') == d.sale_main
        assert self.find(loc.sale_mens_img_loc).get_attribute('src') == d.sale_mens
        assert self.find(loc.sale_gear_img_loc).get_attribute('src') == d.sale_gear
        assert self.find(loc.sale_promo20_img_loc).get_attribute('src') == d.sale_promo20
        assert self.find(loc.sale_promo_free_img_loc).get_attribute('src') == d.sale_promo_free

    def scroll_page(self):
        element = WebDriverWait(self.driver, 3).until(
            ec.visibility_of_element_located(loc.sale_promo_free_img_loc)
        )
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    def check_correctness_links(self):

        for element, text in zip(loc.sale_link_data_loc, d.finish_page_title_data):
            self.iframe_window()
            link = self.driver.find_element(*element).get_attribute("href")
            WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(element)).click()

            try:
                WebDriverWait(self.driver, 5).until(
                    ec.text_to_be_present_in_element(loc.page_title_loc, text)
                )
            except TimeoutException:
                if "#google_vignette" in self.driver.current_url:
                    print("Vignette caught the click, navigating manually!")
                    self.driver.get(link)
                    WebDriverWait(self.driver, 5).until(
                        ec.text_to_be_present_in_element(loc.page_title_loc, text)
                    )
                else:
                    raise

            element_text = self.driver.find_element(*loc.page_title_loc)
            assert element_text.text == text, f'Ожидается: {text}, Получено: {element_text.text}'
            self.driver.back()
