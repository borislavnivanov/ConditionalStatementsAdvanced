h_exam = int(input())
m_exam = int(input())
h_arrival = int(input())
m_arrival = int(input())

exam_in_minutes = m_exam + (h_exam * 60)
arrival_in_minutes = m_arrival + (h_arrival * 60)

arrival_difference = exam_in_minutes - arrival_in_minutes

if 0 <= arrival_difference <= 30:
    print('On time')
    if arrival_difference != 0:
        print(f'{arrival_difference} minutes before the start')

elif 30 < arrival_difference < 60:
    print('Early')
    print(f'{arrival_difference} minutes before the start')

elif 60 <= arrival_difference:
    print('Early')
    print(f'{arrival_difference // 60}:{arrival_difference % 60:02} hours before the start')

elif 0 > arrival_difference > -60:
    print('Late')
    print(f'{abs(arrival_difference)} minutes after the start')

elif -60 >= arrival_difference:
    print('Late')
    print(f'{abs(arrival_difference) // 60}:{abs(arrival_difference) % 60:02} hours after the start')
