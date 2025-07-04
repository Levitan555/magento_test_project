def test_add_to_cart(order):
    order.open_page()
    order.consent()
    order.iframe_window()
    order.add_to_cart()
    order.remove_item_from_cart()


def test_count_product_on_page(order):
    order.open_page()
    order.consent()
    order.iframe_window()
    order.count_product_on_page()


def test_item_color_blue(order):
    order.open_page()
    order.consent()
    order.iframe_window()
    order.filter_color_blue()
