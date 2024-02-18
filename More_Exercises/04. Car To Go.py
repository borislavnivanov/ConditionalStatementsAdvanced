budget = float(input())
season = input()

car_class = str()
car = str()
price = float()

if season == 'Winter':
    if budget <= 100:
        car_class = 'Economy class'
        car = 'Jeep'
        price = budget * 0.65
    elif 100 < budget <= 500:
        car_class = 'Compact class'
        car = 'Jeep'
        price = budget * 0.80
    elif budget > 500:
        car_class = 'Luxury class'
        car = 'Jeep'
        price = budget * 0.90
elif season == 'Summer':
    if budget <= 100:
        car_class = 'Economy class'
        car = 'Cabrio'
        price = budget * 0.35
    elif 100 < budget <= 500:
        car_class = 'Compact class'
        car = 'Cabrio'
        price = budget * 0.45
    elif budget > 500:
        car_class = 'Luxury class'
        car = 'Jeep'
        price = budget * 0.90

print(f'{car_class}\n{car} - {price:.2f}')
