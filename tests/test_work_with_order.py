def test_add_and_remove_to_cart(order_page):
    order_page.open_page()
    order_page.approve_window_consent()
    order_page.closing_iframe_window()
    order_page.add_to_cart()
    order_page.remove_item_from_cart()


def test_count_product_on_page(order_page):
    order_page.open_page()
    order_page.approve_window_consent()
    order_page.closing_iframe_window()
    order_page.count_product_on_page()


def test_item_color_blue(order_page):
    order_page.open_page()
    order_page.approve_window_consent()
    order_page.closing_iframe_window()
    order_page.filter_color_blue()
