month = input()
nights = int(input())

# studio prices
studio_may_oct = 50.00
studio_jun_sep = 75.20
studio_jul_aug = 76.00
# apartment prices
apartment_may_oct = 65.00
apartment_jun_sep = 68.70
apartment_jul_aug = 77.00
# discounts (more than shown days)
discount_studio_may_oct_7 = 5 / 100
discount_studio_may_oct_14 = 30 / 100
discount_studio_jun_sep_14 = 20 / 100
discount_apartment_all_14 = 10 / 100

studio_price = float(0)
apartment_price = float(0)

if month == "May" or month == "October":
    studio_price = studio_may_oct * nights
    apartment_price = apartment_may_oct * nights

    if nights > 14:
        studio_price -= studio_price * discount_studio_may_oct_14
        apartment_price -= apartment_price * discount_apartment_all_14
    elif nights > 7:
        studio_price -= studio_price * discount_studio_may_oct_7

elif month == "June" or month == "September":
    studio_price = studio_jun_sep * nights
    apartment_price = apartment_jun_sep * nights

    if nights > 14:
        studio_price -= studio_price * discount_studio_jun_sep_14
        apartment_price -= apartment_price * discount_apartment_all_14

elif month == 'July' or month == "August":
    studio_price = studio_jul_aug * nights
    apartment_price = apartment_jul_aug * nights

    if nights > 14:
        apartment_price -= apartment_price * discount_apartment_all_14

print(f'Apartment: {apartment_price:.2f} lv.\nStudio: {studio_price:.2f} lv.')
