RENT_SPRING = 3000
RENT_SUMMER_AUTUMN = 4200
RENT_WINTER = 2600

budget = int(input())
season = input()
qty = int(input())

bill = 0.00

if season == 'Spring':
    bill = RENT_SPRING
elif season == 'Summer' or season == 'Autumn':
    bill = RENT_SUMMER_AUTUMN
elif season == 'Winter':
    bill = RENT_WINTER

if qty <= 6:
    bill -= bill * 0.10
elif 7 <= qty <= 11:
    bill -= bill * 0.15
elif qty >= 12:
    bill -= bill * 0.25

if qty % 2 == 0 and season != 'Autumn':
    bill -= bill * 0.05

if bill <= budget:
    print(f'Yes! You have {budget - bill:.2f} leva left.')
else:
    print(f'Not enough money! You need {abs(budget - bill):.2f} leva.')
