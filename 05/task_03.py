# Создайте программу для игры в ''Крестики-нолики''.
def draw_board(board):
    print ('-' * 13)
    for i in range(3):
        print ('|', board[0+i*3], '|', board[1+i*3], '|', board[2+i*3], '|')
        print ('-' * 13)

def take_input(player_label):
    status = False
    while not status:
        player_answer = input(f'Введите цифру с поля(которая не занята) {player_label}? ')
        try:
            player_answer = int(player_answer)
        except:
            print ('Некорректный ввод. Вы уверены, что ввели число?')
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer-1]) not in 'XO'):
                board[player_answer-1] = player_label
                status = True
            else:
                print ('Эта клетка уже занята')
        else:
            print ('Некорректный ввод. Введите число от 1 до 9 чтобы продолжить игру.')

def check_win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for combo in win_coord:
        if board[combo[0]] == board[combo[1]] == board[combo[2]]:
            return board[combo[0]]
    return False

def main(board):
    count = 0
    win = False
    while not win:
        draw_board(board)
        if count % 2 == 0:
            take_input('\033[32mX\033[0m')
        else:
            take_input('\033[33mO\033[0m')
        count += 1
        if count > 4:
            check = check_win(board)
            if check:
                print (check, 'выиграл!')
                win = True
                break
        if count == 9:
            print ('Ничья!')
            break
    draw_board(board)

board = list(range(1,10))
main(board)