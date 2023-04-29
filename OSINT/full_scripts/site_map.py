import requests
from bs4 import BeautifulSoup


def get_sitemap(user_text, print_or_return):
    head = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
            '(KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36'}
    if user_text[-1] != '/':
        user_text += "/"
    try:
        page = requests.get(user_text + 'sitemap.xml')
    except requests.exceptions.MissingSchema:
        print("Enter correct hostname")
    except TimeoutError:
        print("Connection error")
    else:
        return result(page, print_or_return)


def result(page, print_or_return):
    if page.status_code == 200:
        res = BeautifulSoup(page.text, 'html.parser')
        sitemap_line = res.find_all('loc')
        if print_or_return == True:
            print('-' * 35, '8 - Sitemap.xml', '-' * 35, sep='\n')
            for i in sitemap_line:
                print(i.text)
        elif print_or_return == False:
            for i in sitemap_line:
                return str(i.text)
    else:
        print('File sitemap.xml not found')
        return 'File sitemap.xml not found'
