number_of_days = int(input('Enter number of days in month: '))
first_weekday = input('First weekday of the month: ')

weekdays = {'Su': 0, 'M': 1, 'T': 2, 'W': 3, 'Th': 4, 'F': 5, 'Sa': 6}
print('{:>3}{:>4}{:>4}{:>4}{:>4}{:>4}{:>4}'
      .format('Su', 'M', 'T', 'W', 'Th', 'F', 'Sa'))

print (weekdays[first_weekday]*4*' ' + '{:>3}'.format(1), end=' ')
for current_day in range(1, number_of_days+1):
    if (weekdays[first_weekday] + current_day) % 7 == 0:
        print ()
    print ('{:>3}'.format(current_day ), end=' ')