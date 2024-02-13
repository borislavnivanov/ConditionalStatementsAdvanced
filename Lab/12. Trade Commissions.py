city = input()
revenue = float(input())

coefficient = 0

if city == "Sofia":
    if 0 <= revenue <= 500:
        coefficient = 5
    elif 500 < revenue <= 1000:
        coefficient = 7
    elif 1000 < revenue <= 10000:
        coefficient = 8
    elif revenue > 10000:
        coefficient = 12
    elif revenue <= 0:
        coefficient = 'error'
elif city == 'Varna':
    if 0 <= revenue <= 500:
        coefficient = 4.5
    elif 500 < revenue <= 1000:
        coefficient = 7.5
    elif 1000 < revenue <= 10000:
        coefficient = 10
    elif revenue > 10000:
        coefficient = 13
    elif revenue <= 0:
        coefficient = 'error'
elif city == 'Plovdiv':
    if 0 <= revenue <= 500:
        coefficient = 5.5
    elif 500 < revenue <= 1000:
        coefficient = 8
    elif 1000 < revenue <= 10000:
        coefficient = 12
    elif revenue > 10000:
        coefficient = 14.5
    elif revenue <= 0:
        coefficient = 'error'
else:
    coefficient = "error"


if coefficient != 'error':
    result = revenue * ( coefficient / 100)
    print(f'{result:.2f}')
else:
    print(coefficient)
