def open_browser(browser_name):
    my_func_1(open_browser, browser_name)


def my_func_1(x, y):
    print(x.__name__.upper().replace('_', ' '), y.upper())


open_browser('Chrome')


def go_to_companyname_homepage(page_url):
    my_func_2(go_to_companyname_homepage, page_url)


def my_func_2(x, y):
    print(x.__name__.capitalize().replace('_', ' '), y[8:-1])


go_to_companyname_homepage('https://yandex.ru/')


def find_registration_button_on_login_page(page_url, button_text):
    my_func_3(find_registration_button_on_login_page, page_url, button_text)


def my_func_3(x, y, z):
    print(x.__name__.capitalize().replace('_', ' '), y, z)


find_registration_button_on_login_page('https://google.com/', 'submit')
