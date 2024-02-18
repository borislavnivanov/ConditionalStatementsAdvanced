budget = float(input())
season = input()

destination = str()
accommodation = str()
cost = float()

if season == 'Summer':
    destination = 'Alaska'
    if budget <= 1000:
        accommodation = 'Camp'
        cost = budget * 0.65
    elif 1000 < budget <= 3000:
        accommodation = 'Hut'
        cost = budget * 0.80
    elif budget > 3000:
        accommodation = 'Hotel'
        cost = budget * 0.90
elif season == 'Winter':
    destination = 'Morocco'
    if budget <= 1000:
        accommodation = 'Camp'
        cost = budget * 0.45
    elif 1000 < budget <= 3000:
        accommodation = 'Hut'
        cost = budget * 0.60
    elif budget > 3000:
        accommodation = 'Hotel'
        cost = budget * 0.90

print(f'{destination} - {accommodation} - {cost:.2f}')
