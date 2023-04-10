# a = [1, 2, 3]
# b = [3, 2, 1]

# for i in a:
#     for j in b:
#         print(i, j)



# Таблица умножения
# for i in range(1, 2):
#     for j in range(1, 11):
#         print(i, 'X', j, '=', i*j)



# for i in range(1, 2):
#     for j in range(1, 11):
#         if i == j:
#             continue
#         print(i, 'X', j, '=', i*j)


# Крестики-нолики

# maps = [1, 2, 3,
#         4, 5, 6,
#         7, 8, 9]

# victories = [[0, 1, 2], 
#              [3, 4, 5], 
#              [6, 7, 8],
#              [0, 3, 6],
#              [1, 4, 7],
#              [2, 5, 8],
#              [0, 4, 8],
#              [2, 4, 6]]

# def print_maps():
#     print(maps[0], end=" ")
#     print(maps[1], end=" ")
#     print(maps[2])

#     print(maps[3], end=" ")
#     print(maps[4], end=" ")
#     print(maps[5])

#     print(maps[6], end=" ")
#     print(maps[7], end=" ")
#     print(maps[8])

# def step_maps(step, symbol):
#     ind = maps.index(step)
#     maps[ind] = symbol

# def get_result():
#     win = ""

#     for i in victories:
#         if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
#             win = "X"
#         if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
#             win = "O"

#     return win



# game_over = False
# player1 = True

# while game_over == False:

#     print_maps()

#     if player1 == True:
#         symbol = "X"
#         step = int(input("fishdude 1,  your turn: "))
#     else:
#         symbol = "O"
#         step = int(input("fishdude 2,  your turn: "))

#     step_maps(step, symbol)
#     win = get_result()
#     if win != "":
#         game_over = True
#     else:
#         game_over = False

#     player1 = not(player1)

# print_maps()
# print(win, 'WON')