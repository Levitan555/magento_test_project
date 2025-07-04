from selenium.webdriver.common.by import By

sale_main_img_loc = (By.XPATH, '//a[@class="block-promo sale-main"]/child::img')
sale_mens_img_loc = (By.XPATH, '//a[@class="block-promo sale-mens"]/child::img')
sale_gear_img_loc = (By.XPATH, '//a[@class="block-promo sale-women"]/child::img')
sale_promo20_img_loc = (By.XPATH, '//a[@class="block-promo sale-20-off"]/span[@class="image"]/child::img')
sale_promo_free_img_loc = (By.XPATH, '//a[@class="block-promo sale-womens-t-shirts"]/span[@class="image"]/child::img')

sale_link_data_loc = [
    (By.CSS_SELECTOR, '[class="block-promo sale-main"]'),
    (By.CSS_SELECTOR, '[class="block-promo sale-mens"]'),
    (By.CSS_SELECTOR, '[class="block-promo sale-women"]'),
    (By.CSS_SELECTOR, '[class="block-promo sale-womens-t-shirts"]')
]
page_title_loc = (By.CSS_SELECTOR, '[data-ui-id="page-title-wrapper"]')
