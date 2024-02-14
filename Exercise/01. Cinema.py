PREMIERE = 12.00
NORMAL = 7.50
DISCOUNT = 5.00

screening_type = input()
rows = int(input())
columns = int(input())

capacity = rows * columns
income = 0

if screening_type == 'Premiere':
    income = PREMIERE * capacity
elif screening_type == 'Normal':
    income = NORMAL * capacity
elif screening_type == 'Discount':
    income = DISCOUNT * capacity

print(f'{income:.2f}')
