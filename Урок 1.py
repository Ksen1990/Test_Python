task1 = 'Я живу на планете "Земля"'
print (task1)

task2 = input ('Введите произвольную строку из 3 слов: ')
task21 = task2.replace (' ', '!')
print (task21)

task3 = 'Информатика'
task31 = task3[0:4]
task32 = task3[2:7]
task33 = task3[-4:10]
print (task31,',',task32,',',task33)

a = int(input('Введите число А: '))
b = int(input('Введите число B: '))
c = int(input('Введите число C: '))
abc1 = a*a+b*b+c*c+(2*a*b)+(2*a*c)+(2*b*c)
abc2 = a*a+b*b+c*c-(2*a*b)-(2*a*c)+(2*b*c)
print ('Квадрат суммы равен ', abc1)
print ('Квадрат разности равен ', abc2)
