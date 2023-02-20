#Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

ticket = int(input('Введите номер билета(6 цифр): '))
sum1 = 0
sum2 = 0
t = int(ticket / 1000) #получение трех первых цифр из номера билета
while t >= 1:
    temp1 = int(ticket % 10)
    sum1 = sum1 + temp1
    ticket = ticket / 10
    temp2 = int(t % 10)
    sum2 = sum2 + temp2
    t = t / 10
if sum1 == sum2:
    print('Ваш билет счастливый!')
else:
    print('Билет как билет.')