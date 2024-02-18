chrysanthemums = int(input())
rose = int(input())
tulips = int(input())
season = input()
is_holiday = True if input() == 'Y' else False

sum_chrysanthemums = float()
sum_roses =  float()
sum_tulips =  float()

if season == 'Spring' or season == 'Summer':
    sum_chrysanthemums += chrysanthemums * 2.00
    sum_roses += rose * 4.10
    sum_tulips += tulips * 2.50
elif season == 'Autumn' or season == 'Winter':
    sum_chrysanthemums += chrysanthemums * 3.75
    sum_roses += rose * 4.50
    sum_tulips += tulips * 4.15

bill = sum_chrysanthemums + sum_roses + sum_tulips

if is_holiday:
    bill = bill * 1.15

if tulips > 7 and season == 'Spring':
    bill -= bill * 0.05

if rose >= 10 and season == 'Winter':
    bill -= bill * 0.10

if (chrysanthemums + tulips + rose) > 20:
    bill -= bill * 0.20

bill += 2.00

print(f'{bill:.2f}')
