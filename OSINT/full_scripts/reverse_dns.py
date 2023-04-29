from dns import reversename, resolver


def get_host_by_ip(user_text, print_or_return):
    try:
        rev_name = reversename.from_address(user_text)
        reverse_dns = str(resolver.resolve(rev_name, "PTR")[0])
    except Exception as error:
        print(error)
    else:
        return result(print_or_return, reverse_dns)


def result(print_or_return, reverse_dns):
    if print_or_return == True:
        print('-' * 35, '5 - DNS MX record', '-' * 35, sep='\n')
        print(reverse_dns)
    elif print_or_return == False:
        return str(reverse_dns)
