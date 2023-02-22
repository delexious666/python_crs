# a = 1 
#
# if a == 1:
#    print('blablabla')
#
# while a == 1:
#    print('blablabla')
#
# Если запустить такой код, то из-за while print blablabla будет выводится бесконечно
# "Бесконечный цикл"

# a = 1   -  счётчик (с него начинается отсчёт)
#
# while a <= 10:  - тело цикла будет повторяться до момента, пока условие(a <= 10) не будет верным: пока while не станет true(когда будет а == 10 )
# внутри цикла 
#    print(a) - чтобы видеть число, которое выводится на экран
#    a +=1 #

# a = 5
# b = 13
# c = 18
# d = 0
#
# while not b and a >= c:
#     if a != c:
#         a+=1
#         print('abc')
#     print(c)           
# 
# конструкция не верная

# a = False
# b = 6
# c = 18
# d = 12
# while not a and b <= d <= c:
#     if c == d:
#         print('first')
#     else:
#         print(c - d)
#     d += 1       

# a = 30
# b = 40
# while a < b:
#     print(a)
#     a += 3

# a = 'bird'
# while a:
#     print(a, end=" ") 
#     a = a [:-1]

# end=" "  - выводит значения в одну строку(с пробелом внутри ковычек, иначе результат выведется вообще без пробелов)


# a = 0
# while True:
#     if a == 10:
#         break
#     print(a)
#     a+=1

# a = 0
# while True:
#     if a == 10:
#         continue
#     print(a)
#     a+=1

# a = 10
# while a:
#     a -= 1
#     if a % 2 != 0:
#         continue
#     print(a, end=" ")
