
time_on_travel = int(input())
average_speed = int(input())
fuel_by_kilometers = 12
total_kilometers = time_on_travel * average_speed

fuel_spend = total_kilometers/fuel_by_kilometers
print('%0.3f' % fuel_spend)
