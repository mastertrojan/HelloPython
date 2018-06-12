import datetime

def print_header():
    print('--------------------------')
    print('        Birthday App')
    print('--------------------------')
    print()
    return input("Whats your name? ")


def get_birthday_from_user():
    print("Enter your birthday")
    year = int(input('Year [YYYY]: '))
    month = int(input('Month [MM]: '))
    day = int(input('Day [DD]: '))

    bday = datetime.date(year, month, day)
    return bday

def compute_days_between_dates(original_date, target_date):
    this_year = datetime.date(target_date.year, original_date.month, original_date.day)
    dt = this_year - target_date
    return dt.days

def days_on_earth(date, date1):
    dt = date - date1
    return dt.days


def print_birthday_information(days):
    if days < 0:
        print('You had your birthday {} days ago this year.'.format(-days))
    elif days > 0:
        print('Your birthday is in {}  days !'.format(days))
    else:
        print('Happy birthday!')


def main():
    print_header()
    birthday = get_birthday_from_user()
    now = datetime.date.today()
    print(compute_days_between_dates(birthday, now))
    print_birthday_information()


if __name__ == '__main__':
    main()