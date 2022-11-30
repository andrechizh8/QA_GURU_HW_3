def open_browser(browser_name):
    my_func_1(open_browser, browser_name)


def my_func_1(open_browser, browser_name):
    print(open_browser.__name__.upper().replace('_', ' '), browser_name.upper())


open_browser('Chrome')


def go_to_companyname_homepage(page_url):
    my_func_2(go_to_companyname_homepage, page_url)


def my_func_2(go_to_companyname_homepage, page_url):
    print(go_to_companyname_homepage.__name__.capitalize().replace('_', ' '), page_url[8:-1])


go_to_companyname_homepage('https://yandex.ru/')


def find_registration_button_on_login_page(page_url, button_text):
    my_func_3(page_url, button_text)


def my_func_3(page_url, button_text):
    print(find_registration_button_on_login_page.__name__.capitalize().replace('_', ' '), page_url, button_text)


find_registration_button_on_login_page('https://google.com/', 'submit')
