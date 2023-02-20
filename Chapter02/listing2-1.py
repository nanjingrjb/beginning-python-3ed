# Print out a date, given year, month, and day as numbers
import traceback
months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]

# A list with one ending for each number from 1 to 31
endings = ['st', 'nd', 'rd'] + 17 * ['th'] \
        + ['st', 'nd', 'rd'] +  7 * ['th'] \
        + ['st']

year    = input('Year: ')
month   = input('Month  (1-12): ')
day     = input('Day (1-31): ')

try:
    month_number = int(month)
except Exception as e:
    print('month error ,using default 12')
    traceback.print_exc()
    month_number =12

try:
    day_number = int(day)
except Exception as e:
    print('day error ,using default 30')
    traceback.print_exc()
    day_number =30

# Remember to subtract 1 from month and day to get a correct index
<<<<<<< HEAD
try:
    month_name = months[month_number-1]
except :
    month_number=12
    month_name = months[month_number-1]
=======
month_name = months[month_number-1]
ordinal = str(day_number) + endings[day_number-1]
>>>>>>> 60c4f6405fe454c1488f5f570eb6eef8887b9f47

try:
    ordinal = str(day_number) + endings[day_number-1]
except :
    day_number=30
    ordinal = str(day_number) + endings[day_number-1]
print(month_name + ' ' + ordinal + ', ' + year)
