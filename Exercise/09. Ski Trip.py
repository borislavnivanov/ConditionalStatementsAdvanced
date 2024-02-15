ROOM_FOR_ONE_PERSON = 18.00
APARTMENT = 25.00
PRESIDENTIAL_SUIT = 35.00

# discounts
apartment_less_10 = 30 / 100
apartment_10_to_15 = 35 / 100
apartment_more_15 = 50 / 100
presidential_less_10 = 10 / 100
presidential_10_to_15 = 15 / 100
presidential_more_15 = 20 / 100

days_stay = int(input())
type_accommodation = input()
score = input()

nights = days_stay - 1

bill = float()

if type_accommodation == 'room for one person':
    bill = nights * ROOM_FOR_ONE_PERSON

elif type_accommodation == 'apartment':
    bill = nights * APARTMENT

    if nights < 10:
        bill -= bill * apartment_less_10
    elif 10 <= nights <= 15:
        bill -= bill * apartment_10_to_15
    elif nights > 15:
        bill -= bill * apartment_more_15

elif type_accommodation == 'president apartment':
    bill = nights * PRESIDENTIAL_SUIT

    if nights < 10:
        bill -= bill * presidential_less_10
    elif 10 <= nights <= 15:
        bill -= bill * presidential_10_to_15
    elif nights > 15:
        bill -= bill * presidential_more_15

if score == 'positive':
    bill += bill * 0.25
elif score == 'negative':
    bill -= bill * 0.10

print(f'{bill:.2f}')
