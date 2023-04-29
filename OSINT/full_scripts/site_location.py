import pygeoip, os


def get_location(user_text, print_or_return):
    if os.path.exists("full_scripts/GeoIPCity.dat"):
        gi = pygeoip.GeoIP("full_scripts/GeoIPCity.dat")
        try:
            city = gi.record_by_addr(user_text)
        except OSError:
            print("Enter correct ip")
        else:
            return result(print_or_return, city)
    else:
        print("Dir does not exist")
        return "Dir does not exist"


def result(print_or_return, city):
    if print_or_return == True:
        print('-' * 35, '2 - Site location', '-' * 35, sep='\n')
        for key in city:
            if city[key] is None or city[key] == 0:
                continue
            print(f'{key}: {city[key]}')

    elif print_or_return == False:
        for key in city:
            if city[key] is None or city[key] == 0:
                continue
            return str(f'{key}: {city[key]}')

