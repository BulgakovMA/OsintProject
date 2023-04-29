import whois


def get_whois(user_text, print_or_return):
    if "://" in user_text:
        user_text = user_text.split("://")[1]
    user_text = user_text.replace("/", "")
    domain = whois.query(user_text)
    try:
        res = domain.__dict__
    except whois.exceptions.UnknownTld:
        print("Enter correct domain")
    except AttributeError:
        print("Enter correct domain")
    else:
        return result(print_or_return, res)


def result(print_or_return, res):
    if print_or_return == True:
        print('-' * 35, '3 - Whois', '-' * 35, sep='\n')
        for i in res:
            print(f'{i}: {res[i]}')

    elif print_or_return == False:
         for i in res:
            return str(f'{i}: {res[i]}')
