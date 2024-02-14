budget = float(input())
season = input()

where = str()
accommodation = str()
price = float(0)

if budget <= 100:
    where = "Bulgaria"
    if season == 'summer':
        accommodation = "Camp"
        price = budget * (30 / 100)
    elif season == 'winter':
        accommodation = "Hotel"
        price = budget * (70 / 100)
elif budget <= 1000:
    where = "Balkans"
    if season == 'summer':
        accommodation = "Camp"
        price = budget * (40 / 100)
    elif season == 'winter':
        accommodation = "Hotel"
        price = budget * (80 / 100)
elif budget > 1000:
    where = "Europe"
    accommodation = "Hotel"
    price = budget * (90 / 100)

print(f'Somewhere in {where}\n{accommodation} - {price:.2f}')
