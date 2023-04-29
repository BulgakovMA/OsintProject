import full_scripts.ip_address as add
import full_scripts.site_location as loc
import full_scripts.whois_data as whois
import full_scripts.ns as ns
import full_scripts.mx_data as mx
import full_scripts.reverse_dns as rev_dns
import full_scripts.get_robots as robots
import full_scripts.site_map as sitemap
import full_scripts.reverse_ip as rev_ip
from colorama import Fore


def main_func():
    while True:
        try:
            num = int(input('Enter option number: '))
        except:
            print("Enter numbers 0 to 10")
        else:
            if num not in range(1, 11):
                print('Enter numbers 0 to 10')
            else:
                second_func(num)


def second_func(num):
    user_text = input("Enter domain or ip: ")
    if num == 10:
        print_or_return = False
        file_writing(user_text, print_or_return)
    else:
        print_or_return = True
        all_func.get(num)(user_text, print_or_return)


def file_writing(user_text, print_or_return):
    with open("check_domain.txt", "w") as file_output:
        if "".join(user_text.split(".")).isdigit():
            for i in ip:
                file_output.write(f"\n{'-' * 35}\n{menu[i]}\n{'-' * 35}\n")
                file_output.write(all_func.get(i)(user_text, print_or_return) + "\n")
        else:
            for i in domain:
                file_output.write(f"\n{'-' * 35}\n{menu[i]}\n{'-' * 35}\n")
                file_output.write(all_func.get(i)(user_text, print_or_return))
        print("Done!")


if __name__ == "__main__":
    logo = '''
      ___  ____ ___ _   _ _____   ____   _____  __
     / _ \/ ___|_ _| \ | |_   _| | __ ) / _ \ \/ /
    | | | \___ \| ||  \| | | |   |  _ \| | | \  / 
    | |_| |___) | || |\  | | |   | |_) | |_| /  \ 
     \___/|____/___|_| \_| |_|   |____/ \___/_/\_\
    '''
    print(Fore.GREEN, logo, Fore.RESET)
    menu = {
    0: "Exit program",
    1: "Host IP",
    2: "Site location",
    3: "Whois",
    4: "NsLookup",
    5: "DNS MX record",
    6: "Reverse DNS",
    7: "robots.txt",
    8: "sitemap.xml",
    9: "Reverse ip lookup",
    10: "All items"
    }
    for key, value in menu.items():
        print(f'{Fore.GREEN}{key} - {value}{Fore.RESET}')

    all_func = {1: add.get_ip, 2: loc.get_location, 3: whois.get_whois, 4: ns.ns_lookup,
                5: mx.get_mx_record, 6: rev_dns.get_host_by_ip, 7: robots.robots, 8: sitemap.get_sitemap,
                9: rev_ip.get_domains_on_ip}
    text = []
    print_or_return = None
    ip = [2, 6]
    domain = [1, 3, 4, 5, 7, 8, 9]
    main_func()
