import dns.resolver


def get_mx_record(user_text, print_or_return):
    if "://" in user_text:
        user_text = user_text.split("://")[1]
    user_text = user_text.replace("/", "")
    my_resolver = dns.resolver.Resolver(configure=False)
    my_resolver.nameservers = ["8.8.8.8", "1.1.1.1"]
    try:
        answers = my_resolver.resolve(user_text, "MX")
    except dns.resolver.NoAnswer:
        print("Enter correct host")
    except dns.resolver.NXDOMAIN:
        print("Enter correct host")
    else:
        return result(print_or_return, answers)


def result(print_or_return, answers):
    if print_or_return == True:
        print('-' * 35, '5 - DNS MX record', '-' * 35, sep='\n')
        for rdata in answers:
            print(f'MX Record: {rdata.exchange}')

    elif print_or_return == False:
        for rdata in answers:
            return str(f'MX Record: {rdata.exchange}')
