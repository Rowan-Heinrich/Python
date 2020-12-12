#print out a date given year, month, and day as numbers
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
    'December']

#A list with ending for each number from 1 to 31:
endings = ['st', 'nd', 'rd'] + 17*['th'] \
          + ['st', 'nd', 'rd'] +7*['th'] \
          + ['st']

year = input('Year: ')
month = input('Month: ')
day = input('day: ')

month_number=int(month)-1
day_number = int(day)

month_name=months[month_number]
ordinal = day + endings[day_number-1]

print ("Date Entered: " + ordinal + ' ' + month_name + ' ' + year)
print (month_name + ' '+ ordinal + ', ' +year)
