ROSE = 5.00
DAHLIA = 3.80
TULIP = 2.80
NARCISSUS = 3.00
GLADIOLUS = 2.50

type_flower = input()
qty = int(input())
budget = int(input())

bill = 0.00

if type_flower == 'Roses':
    bill = qty * ROSE
    if qty > 80:
        bill -= bill * 0.10
elif type_flower == 'Dahlias':
    bill = qty * DAHLIA
    if qty > 90:
        bill -= bill * 0.15
elif type_flower == 'Tulips':
    bill = qty * TULIP
    if qty > 80:
        bill -= bill * 0.15
elif type_flower == 'Narcissus':
    if qty < 120:
        bill = qty * (NARCISSUS * 1.15)
    else:
        bill = qty * NARCISSUS
elif type_flower == 'Gladiolus':
    if qty < 80:
        bill = qty * (GLADIOLUS * 1.20)
    else:
        bill = qty * GLADIOLUS

if bill <= budget:
    print(f'Hey, you have a great garden with {qty} {type_flower} and {budget - bill:.2f} leva left.')
else:
    print(f'Not enough money, you need {abs(budget - bill):.2f} leva more.')
