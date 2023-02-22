#
#for i in range(1,11 ):  
#    print(i)
#
# for - цикл | i - item | in - месторасположения | 
# range -функция. диапазон(от, до) до не включительно |

# range(stop)
# range(start,stop)
# range(start,stop,step) 

# start - первый элемент последовательности
# stop - последний элемент последовательности
# step - шаг

#for i in range(13): | это range(stop)
#    print(i)

# for i in range(13, 15): | это range(start,stop) 
#     print(i)

# for i in range(13,100, 13): | это range(start,stop,step)
#     print(i)

# for i in range(1,13):
#     if i == 7:   | 7 не видно в принте, потому что после того, как i стала ==7, сработал break, прервал дальнейшее действие и остановил цикл |
#         break
#     print(i)

# for i in range(1,13):
#     if i == 7:   |  не видно в принте, потому что после того, как i стала ==7, сработал continue, прервал текущую итерацию (print(i) для 7) и продолжил цикл |
#         continue
#     print(i)

# for i in range(1,13):
#     if i == 7:
#         continue
#     print(i)
# else:        | else в циклах используется редко
#     print(2)

# myList = ['extensions','EXTENS','EXTENSIOUSLY','EX']
# | print(myList) для списка не подходит, т.к. он выводит все элементы списка(скобки и т.д.)
# for i in myList:
#     print(i, end=" ")

# NB - HOMEWORK - need meke print result == S.T.A.LK.ER.
# a = 'STALKER'
# for i in a:
#     print(i, end=".")






