import datetime


def get_days_from_today(date):
    try:
        datetime_object = datetime.datetime.strptime(date, "%Y.%m.%d")
    except ValueError:
        return "Invalid date"

    return (datetime.datetime.today() - datetime_object).days


date = input("Print date (YYYY.MM.DD): ")
days = get_days_from_today(date)
print(days)
