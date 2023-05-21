Задание 18.8.19. 
sum_tickets = 0
qnt_tickets = int(input("Введите, пожалуйста, количество билетов : =  "))
for age in range(qnt_tickets):
    age = int(input("Введите, пожалуйста, возраст посетителя: =  "))
    if age < 18:
        sum_tickets += 0
    elif 18 <= age <= 25:
        sum_tickets += 990
    elif age > 25:
        sum_tickets += 1390
print("Стоимость Ваших билетов: ", sum_tickets,"руб.",)
if qnt_tickets > 3:
    sum_tickets = int(sum_tickets - (sum_tickets*10)/100)
print("Сумма к оплате с учетом скидки: = ", sum_tickets, "руб.")
print(" Спасибо за проявленный интерес к нашей онлайн конференции!! Будем рады видеть Вас снова!")