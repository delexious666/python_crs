# def 5

# def 6

# def 1

# def 2

# def 3


# 1()
# 2()
#     3()




##Postman
##data-in options

# print('Name')
# print('Type')
# print('Size')
# print('Weight')
# print('Cost')

##manual data typing(exemple)

# print('Aliexpress')
# print('Box')
# print('100')
# print(1)
# print(100)

##or 

# def print_box():
#     print('Name')
#     print('Type')
#     print('Size')
#     print('Weight')
#     print('Cost')

# print_box()




#EXP below

# def my_function(x, y):
#     a = x * y
#     return a

# # my_function(3, 4)  - doesn't work. right option below
# print(my_function(3, 4))

# def my_function(x, y):
#     a = x * y
#     return a
# print(my_function(3, 4) + 12)


# #don't right
# hi()

# def hi():
#     print('test1')

# #right
# def hi():
#     print('test1')

# hi()



#​​visibility area LOCAL

# def Loc():
#     print('test1')

# def hell():
#     a = 5
#     def hallo():
#         b += 1 
#         return b


# print(hallo())


# def Loc():
#     print('test1')

# def hell():
#     a = 5
#     print(a)

#     def hallo():
#         b += 1 
#         return b
#     return hallo()

# print(hell())


# def Loc():
#     print('test1')

# def hell():
#     a = 5
#     print(a)

#     def hallo():
#         nonlocal a
#         a += 1 
#         return a
#     return hallo()

# print(hell())



#​​visibility area GLOBAL

# a = 13

# def beer(x):
#     result = a + x
#     return result

# print(beer(666))

# a = 13

# def beer(q, w, e, r, t, y, u):
#     result = a + q + w + r + e + t + y + u
#     return result

# print(beer(1, 2, 3, 4, 5, 6, 7))


# def hi(q, w, e):
#     print(q, w, e)

# hi(q = 666, w = 111, e = 13)