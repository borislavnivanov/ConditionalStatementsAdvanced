season = input()
type_group = input()
pc_students = int(input())
nights = int(input())

cost = float()
sport = str()

if season == 'Winter':
    if type_group == 'boys':
        cost = pc_students * nights * 9.60
        sport = 'Judo'
    elif type_group == 'girls':
        cost = pc_students * nights * 9.60
        sport = 'Gymnastics'
    elif type_group == 'mixed':
        cost = pc_students * nights * 10.00
        sport = 'Ski'
elif season == 'Spring':
    if type_group == 'boys':
        cost = pc_students * nights * 7.20
        sport = 'Tennis'
    elif type_group == 'girls':
        cost = pc_students * nights * 7.20
        sport = 'Athletics'
    elif type_group == 'mixed':
        cost = pc_students * nights * 9.50
        sport = 'Cycling'
elif season == 'Summer':
    if type_group == 'boys':
        cost = pc_students * nights * 15
        sport = 'Football'
    elif type_group == 'girls':
        cost = pc_students * nights * 15
        sport = 'Volleyball'
    elif type_group == 'mixed':
        cost = pc_students * nights * 20
        sport = 'Swimming'

if 10 <= pc_students < 20:
    cost -= cost * 0.05
elif 20 <= pc_students < 50:
    cost -= cost * 0.15
elif 50 <= pc_students:
    cost -= cost / 2

print(f'{sport} {cost:.2f} lv.')
