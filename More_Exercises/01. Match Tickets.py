# ticket prices
VIP = 499.99
NORM = 249.99

budget = float(input())
ticket_type = input()
tickets = int(input())

bill = 0

# ticket price
if ticket_type == "Normal":
    bill += tickets * NORM
elif ticket_type == "VIP":
    bill += tickets * VIP

# budget reserved for travel exp
if 1 <= tickets <= 4:
    budget -= budget * 0.75
elif 5 <= tickets <= 9:
    budget -= budget * 0.60
elif 10 <= tickets <= 24:
    budget -= budget * 0.50
elif 25 <= tickets <= 49:
    budget -= budget * 0.40
elif 50 <= tickets:
    budget -= budget * 0.25

result = budget - bill

if result >= 0:
    print(f'Yes! You have {result:.2f} leva left.')
else:
    print(f'Not enough money! You need {abs(result):.2f} leva.')
