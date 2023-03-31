def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def digit_sum(date):
    return sum(int(digit) for digit in str(date) if digit.isdigit())


year = int(input("Введите год: "))

month_days = {
    1: 31,
    2: 29 
    if is_leap_year(year) else 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}

month_sums = []

for month in month_days:
    month_sum = 0
    for day in range(1, month_days[month] + 1):
        date = day + month * 100
        month_sum += digit_sum(date)
    month_sums.append(month_sum)
    print("Тест",date)


for i, month_sum in enumerate(month_sums, 1):
    print(f"{i}: {month_sum}")


