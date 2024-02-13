product = input()
day = input()
qty = float(input())

bill = 0

if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
    if product == 'banana':
        bill += 2.5
    elif product == 'apple':
        bill += 1.2
    elif product == 'orange':
        bill += 0.85
    elif product == 'grapefruit':
        bill += 1.45
    elif product == 'kiwi':
        bill += 2.7
    elif product == 'pineapple':
        bill += 5.5
    elif product == 'grapes':
        bill += 3.85
    else:
        bill = 'error'
elif day == 'Saturday' or day == 'Sunday':
    if product == 'banana':
        bill += 2.7
    elif product == 'apple':
        bill += 1.25
    elif product == 'orange':
        bill += 0.90
    elif product == 'grapefruit':
        bill += 1.60
    elif product == 'kiwi':
        bill += 3
    elif product == 'pineapple':
        bill += 5.6
    elif product == 'grapes':
        bill += 4.2
    else:
        bill = 'error'
else:
    bill = 'error'

if bill != 'error':
    bill = bill * qty
    print(f'{bill:.2f}')
else:
    print(bill)
