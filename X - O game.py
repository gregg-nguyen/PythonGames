board = ['$'] + [' '] * 9


def print_board(board):

    print('|' + board[1] + '|' + board[2] + '|' + board[3] + '|')
    print('-------')
    print('|' + board[4] + '|' + board[5] + '|' + board[6] + '|')
    print('-------')
    print('|' + board[7] + '|' + board[8] + '|' + board[9] + '|')


# Ask if player chooses X or O:
def marker():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Pick your letter: ').upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


# Ask player to choose their positions & Check position's availability:
def placement(marker):
    position = 0
    while position not in range(1, 10) or board[position] != ' ':
        position = int(input('Please choose your position: '))
        if position in range(1, 10) and board[position] == ' ':
            board[position] = marker
            break
        else:
            print('Cannot place here! Please choose another position!!!')
            continue


# Determine when to win:
def winning_rule(board, marker):
    if (board[1] == board[4] == board[7] == marker or
            board[2] == board[5] == board[8] == marker or
            board[3] == board[6] == board[9] == marker or
            board[1] == board[2] == board[3] == marker or
            board[4] == board[5] == board[6] == marker or
            board[7] == board[8] == board[9] == marker or
            board[1] == board[5] == board[9] == marker or
            board[3] == board[5] == board[7] == marker):
        return True


# Determine if board is full:
def full_board_check(board):
    for x in board:
        if x == ' ':
            return False
    else:
        return True

    # Check if players want to play again:


def replay():
    replay = ' '
    while replay[0] != 'Y':
        replay = input('Do you want another round?: ').upper()
        if replay[0] == 'Y':
            return True
            break
        else:
            break


# RUN THE GAME:
print('Welcome to Tik Tak Toe!!!')

while True:
    # Defining game rules outside of loop:

    board = ['$'] + [' '] * 9
    print_board(board)
    p1, p2 = marker()
    turn = p1
    print(f'{p1} will go first this time!')

    # Ask if players wanna start:
    question = input('Do you wanna start now? ').upper()
    if question[0] == 'Y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'X':
            print_board(board)
            if winning_rule(board, 'X'):
                print_board(board)
                print('X is the winner!')
                break
            else:
                if full_board_check(board):
                    print('This game is a DRAW!')
                    break
                else:
                    placement('X')
                    print_board(board)
                    if winning_rule(board, 'X'):
                        print_board(board)
                        print('X is the winner!')
                        break
                    else:
                        turn = 'O'


        else: # turn = 'O'
            print_board(board)
            if winning_rule(board, 'O'):
                print_board(board)
                print('O is the winner!')
                break
            else:
                if full_board_check(board):
                    print('This game is a DRAW!')
                    break
                else:
                    placement('O')
                    print_board(board)
                    if winning_rule(board, 'O'):
                        print_board(board)
                        print('O is the winner!')
                        break
                    else:
                        turn = 'X'

    if not replay():
        break

