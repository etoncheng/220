"""
Name: Eton Cheng
lab10.py

Problem: Tic-Tac-Toe

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


board = {'1': ' ', '2': ' ', '3': ' ',
         '4': ' ', '5': ' ', '6': ' ',
         '7': ' ', '8': ' ', '9': ' '}

player = 1
total_moves = 0
end_check = 0


def check():
    # Player 1
    if board['1'] == 'X' and board['2'] == 'X' and board['3'] == 'X':
        print('Player 1 Wins!')
        return 1
    if board['4'] == 'X' and board['5'] == 'X' and board['6'] == 'X':
        print('Player 1 Wins!')
        return 1
    if board['7'] == 'X' and board['8'] == 'X' and board['9'] == 'X':
        print('Player 1 Wins!')
        return 1
    if board['1'] == 'X' and board['5'] == 'X' and board['9'] == 'X':
        print('Player 1 Wins!')
        return 1
    if board['1'] == 'X' and board['4'] == 'X' and board['7'] == 'X':
        print('Player 1 Wins!')
        return 1
    if board['2'] == 'X' and board['5'] == 'X' and board['8'] == 'X':
        print('Player 1 Wins!')
        return 1
    if board['3'] == 'X' and board['6'] == 'X' and board['9'] == 'X':
        print('Player 1 Wins!')
        return 1

    # Player 2
    if board['1'] == 'O' and board['O'] == 'X' and board['3'] == 'O':
        print('Player 2 Wins!')
        return 1
    if board['4'] == 'O' and board['5'] == 'O' and board['6'] == 'O':
        print('Player 2 Wins!')
        return 1
    if board['7'] == 'O' and board['8'] == 'O' and board['9'] == 'O':
        print('Player 2 Wins!')
        return 1
    if board['1'] == 'O' and board['5'] == 'O' and board['9'] == 'O':
        print('Player 2 Wins!')
        return 1
    if board['1'] == 'O' and board['4'] == 'O' and board['7'] == 'O':
        print('Player 2 Wins!')
        return 1
    if board['2'] == 'O' and board['5'] == 'O' and board['8'] == 'O':
        print('Player 2 Wins!')
        return 1
    if board['3'] == 'O' and board['6'] == 'O' and board['9'] == 'O':
        print('Player 2 Wins!')
        return 1


print('1|2|3')
print('------')
print('4|5|6')
print('------')
print('7|8|9')

while True:
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('------')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('------')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    end_check = check()
    if total_moves == 9 or end_check == 1:
        break
    while True:
        if player == 1:
            player1_input = input('Player 1')
            if player1_input.upper() in board and board[player1_input.upper()] == ' ':
                board[player1_input.upper()] = 'X'
                player = 2
                break
            else:
                print('Invalid Input, Try Again')
                continue
        else:
            player2_input = input('Player 2')
            if player2_input.upper() in board and board[player2_input.upper()] == ' ':
                board[player2_input.upper()] = 'O'
                player = 1
                break
            else:
                print('Invalid Input, Try Again')
                continue
    total_moves += 1
    print()
