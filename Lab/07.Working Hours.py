hour = int(input())
day = input()

if day == 'Sunday':
    print('closed')
else:
    if 10 <= hour <= 18:
        print('open')
    else:
        print('closed')
