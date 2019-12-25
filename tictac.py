print('\n' * 100)
import random


def display_board(board):
    print(board[7], '|', board[8], '|', board[9])
    print('__', '__', '__')
    print(board[4], '|', board[5], '|', board[6])
    print('__', '__', '__')
    print(board[1], '|', board[2], '|', board[3])


#test_board = ['X'] * 10
#display_board(test_board)


def player_input():
    marker = []
    possible_list = ['X', 'O']
    while marker not in possible_list:
        marker = input('What is your marker? X or O ')
        break
    player_1_marker = marker
    possible_list.remove(marker)
    player_2_marker = possible_list
    return (player_1_marker, player_2_marker[0])


#player_1_marker, player_2_marker = player_input()
#print(player_1_marker, player_2_marker)

##def place_marker(board):
##    i = 0
##    marker = []
##    while i not in range(1,10):
##        i = int(input('where to place your marker? '))
##
##    while marker not in ['X','O']:
##        marker = input('What is your marker? X or O? ')
##
##    board[i]= marker
##    return board


def place_marker(board, position, marker):
    board[position] = marker


#place_marker(test_board, 8, player_1_marker)
#display_board(test_board)


def win_check(board, marker):
    if ((board[1] == marker and board[4] == marker and board[7] == marker) or
        (board[2] == marker and board[5] == marker and board[8] == marker) or
        (board[3] == marker and board[6] == marker and board[9] == marker) or
        (board[1] == marker and board[5] == marker and board[9] == marker) or
        (board[3] == marker and board[5] == marker and board[7] == marker)):
        print('this player has won')
        return True


#win_check(test_board, 'X')


def choose_first():
    players_list = ['player_1', 'player_2']
    return random.choice(players_list)


def space_check(board, position):
    if board[position] in ['X', 'O']:
        return False
    else:
        return True


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    i = 0
    g = True
    while g:
        while i not in range(1, 10):
            i = int(input('Where do you like to place your marker? '))
            if space_check(board, i):
                g = False
                return i
            else:
                print('The place is taken already, try another position.')
                i = 0


def replay():
    x = input('Do you want to play again? ').capitalize()
    if x == 'Yes':
        return True


#' ' '
#Here is how we creat the game with the functions that has been defined before
#' ' '

print('Welcome to Tic Tac Toe!')
flag = True
while flag:
    #first we try to build up the platform of the game
    print('\n' * 100)
    board = [' '] * 10
    display_board(board)

    #players should pick their marker and order of start

    player_1_marker, player_2_marker = player_input()
    player = choose_first()

    #now the game begins, 1st I tried to clarify which player is going to play first and what is the marker

    game_on = True
    while game_on:
        print(player + ' is playing')
        if player == 'player_1':
            marker = player_1_marker
            player = 'player_2'
        else:
            marker = player_2_marker
            player = 'player_1'

        #I am going to ask the 1st player to pick their position in the board,
        # then it will assign the players marker into the board, if the position is still free
        while not full_board_check(board):
            position = player_choice(board)
            if space_check(board, position):
                place_marker(board, position, marker)
                display_board(board)
                if win_check(board, marker):
                    print('you won')
                    break
                else:
                    break
        # if the board fills up, the game is over, so I ask the players if they like to play again or not
        if full_board_check(board):
            if not replay():
                game_on = False
                flag = False
            else:
                game_on = False
