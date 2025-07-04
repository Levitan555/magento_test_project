from selenium.webdriver.remote.webdriver import WebDriver
from .locators import consent_frame_locator as loc
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com'
    page_url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page(self):
        if self.page_url:
            self.driver.get(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplemented('Pages can not be opened')

    def find(self, locator):
        return self.driver.find_element(*locator)

    def finds(self, locator):
        return self.driver.find_elements(*locator)

    def consent(self):
        try:
            button_consent = WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(loc.consent_loc))
            button_consent.click()
        except Exception as e:
            print('The consent window did not appear', e)

    def iframe_window(self):
        try:
            WebDriverWait(self.driver, 2).until(
                ec.frame_to_be_available_and_switch_to_it(loc.iframe_loc)
            )
            WebDriverWait(self.driver, 2).until(
                ec.element_to_be_clickable(loc.frame_close_loc)
            ).click()
        except Exception:
            self.driver.switch_to.default_content()
            # Эту часть кода я нагло слизал с нейронки, потому что просто замучился отключать рекламу другими способами
            self.driver.execute_script("""
                // Удаляем hash, overlay и все рекламные элементы
                if (window.location.hash === "#google_vignette") {
                    history.replaceState(null, "", window.location.pathname + window.location.search);
                }
                document.querySelectorAll(
                    'ins.adsbygoogle, .adsbygoogle, #google_vignette, .google_vignette, 
                    .grecaptcha-badge, div[id^="aswift"], iframe[id^="aswift"]'
                ).forEach(e => e.remove());
                var host = document.getElementById('aswift_1_host');
                if (host) host.remove();
            """)
        finally:
            self.driver.switch_to.default_content()
