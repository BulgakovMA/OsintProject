import socket


def get_ip(user_text, print_or_return):
    if "://" in user_text:
        user_text = user_text.split("://")[1]
    user_text = user_text.replace("/", "")
    try:
        remote_ip = socket.gethostbyname(user_text)
    except socket.gaierror:
        print("Enter correct hostname")
    except TimeoutError:
        print("Cannot connect to hostname")
    else:
        return result(user_text, print_or_return, remote_ip)


def result(user_text, print_or_return, remote_ip):
    if print_or_return == True:
        print('-' * 35, '1 - Host IP', '-' * 35, sep='\n')
        print(f"IP Address of {user_text} is {remote_ip}")
    elif print_or_return == False:
        return str(f"IP Address of {user_text} is {remote_ip}")
