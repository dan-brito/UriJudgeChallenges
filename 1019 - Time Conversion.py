total_time_seconds = int(input())

hours = total_time_seconds // 3600
minutes = (total_time_seconds % 3600) // 60
seconds = total_time_seconds - (hours * 3600) - (minutes * 60)

print('%.f:%.f:%.f' % (hours, minutes, seconds))
#print(f'{hours}:{minutes}:{seconds}')