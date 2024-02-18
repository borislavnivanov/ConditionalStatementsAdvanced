card_number = input()

verification_sum = int(0)

try:
    verification_number = int(card_number)
except:
    print('Only whole numbers allowed')
    exit()


def get_last_digit_odd(number):
    last_digit = number % 10

    return last_digit


def get_last_digit_even(number):
    last_digit = number % 10
    last_digit *= 2
    summed_digit = int(0)

    if last_digit > 9:
        summed_digit += last_digit % 10
        summed_digit += last_digit // 10
    else:
        summed_digit += last_digit % 10

    return summed_digit


def remove_last_digit(number):
    shaved_number = number // 10

    return shaved_number


i = 0
while i < len(card_number):
    verification_sum += get_last_digit_odd(verification_number)
    verification_number = remove_last_digit(verification_number)
    i += 1
    verification_sum += get_last_digit_even(verification_number)
    verification_number = remove_last_digit(verification_number)
    i += 1

if verification_sum % 10 == 0:
    print('CARD IS VALID')
else:
    print('CARD IS NOT VALID')
