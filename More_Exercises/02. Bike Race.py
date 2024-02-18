juniors = int(input())
seniors = int(input())
track = input()

raised = float(0)

if track == "trail":
    raised += juniors * 5.50
    raised += seniors * 7.00
elif track == 'cross-country':
    raised += juniors * 8.00
    raised += seniors * 9.50
    if (juniors + seniors) >= 50:
        raised -= raised * 0.25
elif track == 'downhill':
    raised += juniors * 12.25
    raised += seniors * 13.75
elif track == 'road':
    raised += juniors * 20.00
    raised += seniors * 21.50

raised -= raised * 0.05

print(f'{raised:.2f}')
