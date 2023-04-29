import requests

def get_domains_on_ip(user_text, print_or_return):
    if '://' in user_text:
        user_text = user_text.split('://')[1]
    user_text = user_text.replace('/', '')
    url = 'https://api.viewdns.info/reverseip/?host=' + user_text + '&apikey=cd397331cf0bf0648f32bd3695707df4f5107b90&output=json'
    try:
        result = requests.get(url)
        final_res = result.json()['response']['domains']
    except KeyError:
        print("Enter correct ip or domain")
    except TimeoutError:
        print("Connection error")
    else:
        return res(print_or_return, final_res)


def res(print_or_return, final_res):
    if print_or_return == True:
        print('-' * 35, '9 - Reverse IP lookup', '-' * 35, sep='\n')
        for domain in final_res:
            print(domain['name'])
    elif print_or_return == False:
        for domain in final_res:
            return str(domain['name'])
