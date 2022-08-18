print("[Прайс]: \n [до 18 лет] - бесплатно \n [18-25] - 990 руб. \n [25 и старше] - 1390 руб. "
      "\n [При приобритении более 3х билетов, действует скидка 10% на сумму всей покупки]")
cost = 0.0
while True:
    try:
        ticket = int(input('Введите количество билетов: '))
        if type(ticket) == int:
            break
    except ValueError:
        print('Введите целое число')
for i in range(ticket):
    while True:
        try:
            age = int(input('Укажите возраст: '))
            if age < 18:
                cost += 0
            elif 18 <= age < 25:
                cost += 990
            else:
                cost = cost + 1390
            if type(age) == int:
                break
        except ValueError:
            print('Укажите корректный возраст: ')
if ticket > 3:
    cost = cost * 0.9
    print('Итого с учетом скидки 10%: ' + str('%.2f' % round(cost)) + ' ' + 'руб')
else:
    print('Итого: ' + str('%.2f' % round(cost)) + ' ' + 'руб')
