def test_availability_of_images(sale):
    sale.open_page()
    sale.consent()
    sale.iframe_window()
    sale.check_images()


def test_checking_links(sale):
    sale.open_page()
    sale.consent()
    sale.iframe_window()
    sale.check_correctness_links()


def test_scroll_page(sale):
    sale.open_page()
    sale.consent()
    sale.iframe_window()
    sale.scroll_page()
