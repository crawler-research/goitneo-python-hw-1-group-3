from collections import defaultdict
from datetime import datetime, timedelta

[{"name": "Bill Gates", "birthday": datetime(1955, 10, 28)}]
def get_birthdays_per_week(users):
    today = datetime.today().date()
    birthdays = defaultdict(list)

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)
        # print(today, birthday_this_year, birthday_this_year - today)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days

        if delta_days < 7:
            day_of_week = birthday_this_year.weekday()
            if day_of_week >= 5:  # if it's weekend then move to Monday
                day_of_week = 0
            birthdays[day_of_week].append(name)
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    for i, day in enumerate(days_of_week):
        if birthdays[i]:
            print(f"{day}: {', '.join(birthdays[i])}")

if __name__ == "__main__":
    users = [
        {"name": "Alice", "birthday": datetime(2023, 3, 1)},
        {"name": "Bob", "birthday": datetime(1995, 3, 2)},
        {"name": "Charlie", "birthday": datetime(2024, 2, 24)},
        {"name": "David", "birthday": datetime(2022, 3, 10)},
        {"name": "Eve2", "birthday": datetime(1998, 2, 25)},
        {"name": "Eve3", "birthday": datetime(1998, 2, 26)},
        {"name": "Eve4", "birthday": datetime(1998, 2, 27)},
        {"name": "Eve5", "birthday": datetime(1998, 2, 28)},
    ]

    get_birthdays_per_week(users)
