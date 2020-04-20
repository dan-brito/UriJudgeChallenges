age_in_days = int(input())

years = age_in_days //365
months = (age_in_days % 365) // 30
days = age_in_days - (years*365) - (months*30)

print('%.f ano(s)\n%.f mes(es)\n%.f dia(s)' % (years, months, days))
