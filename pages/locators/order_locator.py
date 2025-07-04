from selenium.webdriver.common.by import By

size_loc = (By.XPATH, '//div[@class="swatch-opt-2017"]//div[@id="option-label-size-143-item-171"]')
color_loc = (By.XPATH, '//div[@class="swatch-opt-2017"]//div[@id="option-label-color-93-item-56"]')
button_add_to_cart_loc = (By.CSS_SELECTOR, '[data-product-sku="WSH10"] [type="submit"]')
counter_number_loc = (By.CSS_SELECTOR, 'div[data-block="minicart"] span.counter-number')
success_order_text_loc = (By.CSS_SELECTOR, '[role="alert"] [data-bind^="html"]')
product_item_loc = (By.CSS_SELECTOR, '[class="product-item-info"]')
remove_item_loc = (By.CSS_SELECTOR, '[title="Remove item"]')
remove_modal_window_loc = (By.CSS_SELECTOR, '[class="action-primary action-accept"]')
subtitle_empty_loc = (By.CSS_SELECTOR, '[class="subtitle empty"]')
filter_color_loc = (By.XPATH, '//div[text()="Color"]')
color_blue_loc = (
    By.XPATH, '//div[@id="narrow-by-list"]//div[contains(@class, "swatch-option") '
              'and contains(@class, "color") and @option-label="Blue"]'
)
check_color_blue_loc = (By.CSS_SELECTOR, '[aria-checked="true"][aria-label="Blue"]')
