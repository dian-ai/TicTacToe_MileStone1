print('\n'*100)
import random
def display_board(board):
    print(board[7],'|',board[8],'|',board[9])
    print('__', '__', '__')
    print(board[4],'|',board[5],'|',board[6])
    print('__', '__', '__')
    print(board[1],'|',board[2],'|',board[3])

test_board =['X']*10
display_board(test_board)

def player_input():
    marker = []
    possible_list =['X','O']
    while marker not in possible_list:
        marker = input('What is your marker? X or O ')
        break
    player_1_marker = marker
    possible_list.remove(marker)
    player_2_marker = possible_list
    return (player_1_marker, player_2_marker[0])

player_1_marker, player_2_marker = player_input()
print(player_1_marker, player_2_marker)

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



place_marker(test_board, 8, player_1_marker)
display_board(test_board)

def win_check(board, marker):
    if ([board[1]==marker,board[4]==marker, board[7]==marker] or
            [board[2]==marker,board[5]==marker, board[8]==marker] or
            [board[3]==marker,board[6]==marker, board[9]==marker] or
            [board[1]==marker,board[5]==marker, board[9]==marker] or
            [board[3]==marker,board[5]==marker, board[7]==marker]):
        print('this player has won')
win_check(test_board,'X')

def choose_first():
    players_list = [player_1, player_2]
    return random.choice(players_list)

def space_check(board, position):
    if board[position] in ['X','O']:
        return False
    else:
        return True


    
    
