print('Введите количество билетов, которые желаете приобрести')
ticket = int(input())
print('Введите возраст всех посетителей через пробел')
age = list(map(int, input().split( )))
ticket_price = 0
for i in range(ticket):
    if 1 <= age[i] < 18:
        ticket_price = ticket_price
    elif 18 <= age[i] < 25:
        ticket_price += 990
    elif age[i] >= 25:
        ticket_price += 1390
    elif age[i] <= 0:
        print('Некорректная запись возраста')
if ticket > 3:
    print(ticket_price - ((ticket_price * 10) / 100))
else:
    print(ticket_price)
