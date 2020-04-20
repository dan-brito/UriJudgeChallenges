employees_name = str(input())
fixed_salary = float(input())
month_total_sales = float(input())

commission = month_total_sales * 0.15
final_salary = fixed_salary + commission

print('TOTAL = R$ %0.2f' % final_salary)
