# number = int(input())
#
# if 100 <= number <= 200 or number == 0:
#     pass
# else:
#     print("invalid")

num = int(input())
output = str()

if not 100 <= num <= 200 or not num == 0:
    output = 'invalid'

print(output)