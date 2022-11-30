def open_browser(browser_name):
    change_name_func(open_browser, browser_name)


def change_name_func(name, arg):
    print(name.__name__.upper().replace('_', ' '),arg.upper())


open_browser('Chrome')


def go_to_companyname_homepage(page_url):
    my_func_2(go_to_companyname_homepage, page_url)


def my_func_2(name, url):
    print(name.__name__.capitalize().replace('_', ' '), url[8:-1])


go_to_companyname_homepage('https://yandex.ru/')


def find_registration_button_on_login_page(page_url, button_text):
    my_func_3(find_registration_button_on_login_page, page_url, button_text)


def my_func_3(name, url, text):
    print(name.__name__.capitalize().replace('_', ' '), url, text)


find_registration_button_on_login_page('https://google.com/', 'submit')
