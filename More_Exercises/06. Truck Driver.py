season = input()
distance_km = float(input())

salary = float()

if season == 'Spring' or season == 'Autumn':
    if distance_km <= 5000:
        salary = distance_km * 0.75
    elif 5000 < distance_km <= 10000:
        salary = distance_km * 0.95
    elif 10000 < distance_km <= 20000:
        salary = distance_km * 1.45
elif season == 'Summer':
    if distance_km <= 5000:
        salary = distance_km * 0.90
    elif 5000 < distance_km <= 10000:
        salary = distance_km * 1.10
    elif 10000 < distance_km <= 20000:
        salary = distance_km * 1.45
elif season == 'Winter':
    if distance_km <= 5000:
        salary = distance_km * 1.05
    elif 5000 < distance_km <= 10000:
        salary = distance_km * 1.25
    elif 10000 < distance_km <= 20000:
        salary = distance_km * 1.45

salary = salary * 4
salary = salary * 0.90

print(f'{salary:.2f}')
