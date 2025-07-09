def test_availability_of_images(sale_page):
    sale_page.open_page()
    sale_page.approve_window_consent()
    sale_page.closing_iframe_window()
    sale_page.check_images()


def test_checking_links(sale_page):
    sale_page.open_page()
    sale_page.approve_window_consent()
    sale_page.closing_iframe_window()
    sale_page.check_correctness_links()


def test_scroll_page(sale_page):
    sale_page.open_page()
    sale_page.approve_window_consent()
    sale_page.closing_iframe_window()
    sale_page.scroll_page()
