numbers = list()

while True:
    var = float(input())
    numbers.append(var)
    if var < 0:
        break

f = len(numbers)
for i in numbers:
    if i >= 0:
        print(f'Result: {i * 2:.2f}')
    else:
        print('Negative number!')
