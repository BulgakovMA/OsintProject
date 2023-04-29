import requests

def robots(user_text, print_or_return):
    head = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
            '(KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36'}
    if user_text[-1] != '/':
        user_text += "/"
    try:
        page = requests.get(user_text + 'robots.txt', headers=head)
    except requests.exceptions.MissingSchema:
        print("Enter correct hostname")
    except TimeoutError:
        print("Connection error")
    else:
        return result(page, print_or_return)


def result(page, print_or_return):
    if page.status_code != 404:
        if print_or_return == True:
            print('-' * 35, '7 - Robots.txt', '-' * 35, sep='\n')
            print(page.text)
        elif print_or_return == False:
            return str(page.text)
    else:
        print('File robots.txt not found')
        return 'File robots.txt not found'
