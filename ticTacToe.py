data = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def draw_pattern():
    print(data[0], '|', data[1], '|', data[2])
    print('----------')
    print(data[3], '|', data[4], '|', data[5])
    print('----------')
    print(data[6], '|', data[7], '|', data[8])
    print('----------')


def computer():
    if (data[0] == data[1] == 'X' or data[5] == data[8] == 'X' or data[4] == data[6] == 'X') and (data[2] == ' '):
        data[2] = 'O'
    elif (data[1] == data[2] == 'X' or data[3] == data[6] == 'X' or data[4] == data[8] == 'X') and (data[0] == ' '):
        data[0] = 'O'
    elif (data[0] == data[2] == 'X' or data[4] == data[7] == 'X') and (data[1] == ' '):
        data[1] = 'O'
    elif (data[0] == data[6] == 'X' or data[4] == data[5] == 'X') and (data[3] == ' '):
        data[3] = 'O'
    elif (data[1] == data[7] == 'X' or data[3] == data[5] == 'X' or data[0] == data[8] == 'X' or data[2] == data[
        6] == 'X') and (data[4] == ' '):
        data[4] = 'O'
    elif (data[3] == data[4] == 'X' or data[2] == data[8] == 'X') and (data[5] == ' '):
        data[5] = 'O'
    elif (data[7] == data[8] == 'X' or data[0] == data[3] == 'X' or data[2] == data[4] == 'X') and (data[6] == ' '):
        data[6] = 'O'
    elif (data[1] == data[4] == 'X' or data[6] == data[8] == 'X') and (data[7] == ' '):
        data[7] = 'O'
    elif (data[6] == data[7] == 'X' or data[5] == data[2] == 'X' or data[0] == data[4] == 'X') and (data[8] == ' '):
        data[8] = 'O'
    elif data[4] == 'X':
        for i in [0, 2, 6, 8]:
            if data[i] == ' ':
                data[i]='O'
    elif data[0] == 'X' or data[2] == 'X' or data[6] == 'X' or data[8] == 'X':
        data[4] = 'O'
    else:
        for i in range(0, 9):
            if data[i] == ' ':
                data[i] = 'O'
                break


def user_restriction(choice):
    if data[choice] == 'O':
        return False
    else:
        return True


def winner():
    for i in ['X', 'O']:
        if data[0] == data[1] == data[2] == i:
            return i
        elif data[0] == data[3] == data[6] == i:
            return i
        elif data[1] == data[4] == data[7] == i:
            return i
        elif data[2] == data[5] == data[8] == i:
            return i
        elif data[3] == data[4] == data[5] == i:
            return i
        elif data[6] == data[7] == data[8] == i:
            return i
        elif data[0] == data[4] == data[8] == i:
            return i
        elif data[2] == data[4] == data[6] == i:
            return i


def game():
    playing = True
    count = 0
    while playing:
        user_choice = int(input('enter the position : '))-1
        user_restriction(user_choice)
        if user_restriction(user_choice):
            data[user_choice] = 'X'
            if count > 0:
                computer()
            else:
                for i in range(0, 9):
                    if data[i] == ' ':
                        data[i] = 'O'
                        break

            draw_pattern()
        else:
            print('already filled: ')
        n = []
        for i in range(0, 9):
            n.append(data[i])
        if n.count(' ') == 0:
            print('draw')
            playing = False

        count += 1
        if count == 9:
            playing = False
        win = winner()

        if win:
            if win == 'X':
                print('you won')
            else:
                print('computer won')
            playing = False


game()
