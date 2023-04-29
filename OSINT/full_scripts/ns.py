from nslookup import Nslookup

def ns_lookup(user_text, print_or_return):
    if "://" in user_text:
        user_text = user_text.split("://")[1]
    user_text = user_text.replace("/", "")
    dns_query = Nslookup(dns_servers=["1.1.1.1"])
    ips_record = dns_query.dns_lookup(user_text)
    return result(print_or_return, ips_record, dns_query, user_text)


def result(print_or_return, ips_record, dns_query, user_text):
    if print_or_return == True:
        print('-' * 35, '4 - Nslookup', '-' * 35, sep='\n')
        for i in ips_record.response_full:
            print(i)

    elif print_or_return == False:
        for i in ips_record.response_full:
            return str(i)

    return result_2(dns_query, user_text, print_or_return)


def result_2(dns_query, user_text, print_or_return):
    soa_record = dns_query.soa_lookup(user_text)
    if print_or_return == True:
        for i in soa_record.response_full:
            print(i)

    elif print_or_return == False:
        for i in soa_record.response_full:
            return str(i)
