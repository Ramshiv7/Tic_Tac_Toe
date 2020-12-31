import random 

def play_symbol():
    all_symbol = ['X', 'O']
    x1 = ''
    x2 = ''
    while x1 not in all_symbol:
        x1 = input('Player 1, Please choose your symbol X or O: ').upper()

        if x1 not in all_symbol:
            print('Invalid Symbol Choosen !')
        else:
            if x1 == 'X':
                x2 = 'O'
            else:
                x2 = 'X'


    print('''
Player Symbols''')
    print(f'Player 1: {x1}')
    print(f'Player 2: {x2}')


    return x1, x2

def whos_first():

    if random.randint(0,1) == 0:
        print('Player 2 Goes First !!!')
        player = 1

    else:
        print('Player 1 Goes First !!!' )
        player = 0


    return player


def game_inputs(x1, x2, player):


    p1 = ''
    p2 = ''
    p3 = ''
    p4 = ''
    p5 = ''
    p6 = ''
    p7 = ''
    p8 = ''
    p9 = ''

    game_won = False
    pos = 0



    print(f''' 
         {p7} | {p8} | {p9}
        ----------------
         {p4} | {p5} | {p6}
        ----------------
         {p1} | {p2} | {p3}
              ''')

    while game_won == False:


        dict = {'1': 'p1',
                '2': 'p2',
                '3': 'p3',
                '4': 'p4',
                '5': 'p5',
                '6': 'p6',
                '7': 'p7',
                '8': 'p8',
                '9': 'p9'
                }

        
        if player % 2 == 0:
            
            try:
                pos = int(input(f'Player Choosen: {x1}, Please Enter the Position (1 - 9): '))
            
            except ValueError:
                print('Invalid Input Player')
                
            if pos in range(1,10):

                if p1 == '' and dict[f'{pos}'] == 'p1':
                    p1 = x1
                elif p2 == '' and dict[f'{pos}'] =='p2':
                    p2 = x1
                elif p3 == '' and dict[f'{pos}'] =='p3':
                    p3 = x1
                elif p4 == '' and dict[f'{pos}'] =='p4':
                    p4 = x1
                elif p5 == '' and dict[f'{pos}'] =='p5':
                    p5 = x1
                elif p6 == '' and dict[f'{pos}'] =='p6':
                    p6 = x1
                elif p7 == '' and dict[f'{pos}'] =='p7':
                    p7 = x1
                elif p8 == '' and dict[f'{pos}'] =='p8':
                    p8 = x1
                elif p9 == '' and dict[f'{pos}'] =='p9':
                    p9 = x1
                else:
                    print('Position is already Taken')
                    player-=1


                player+=1

                print(f''' 
         {p7} | {p8} | {p9}
        ---------------
         {p4} | {p5} | {p6}
        ---------------
         {p1} | {p2} | {p3}
              ''')

            else:
                print('Invalid Input')

        elif player % 2 != 0:

            pos = int(input(f'Player Choosen: {x2}, Please Enter the Position (1 - 9): '))
                
            if pos in range(1,10):

                if p1 == '' and dict[f'{pos}'] == 'p1':
                    p1 = x2
                elif p2 == '' and dict[f'{pos}'] =='p2':
                    p2 = x2
                elif p3 == '' and dict[f'{pos}'] =='p3':
                    p3 = x2
                elif p4 == '' and dict[f'{pos}'] =='p4':
                    p4 = x2
                elif p5 == '' and dict[f'{pos}'] =='p5':
                    p5 = x2
                elif p6 == '' and dict[f'{pos}'] =='p6':
                    p6 = x2
                elif p7 == '' and dict[f'{pos}'] =='p7':
                    p7 = x2
                elif p8 == '' and dict[f'{pos}'] =='p8':
                    p8 = x2
                elif p9 == '' and dict[f'{pos}'] =='p9':
                    p9 = x2              

                else:
                    print('Position is already Taken')
                    player-=1


                player+=1


                print(f''' 
            {p7} | {p8} | {p9}
            ---------------
            {p4}| {p5} | {p6}
            ---------------
            {p1} | {p2} | {p3}
                  ''')

            else:
                print('Position is not Valid !!!')



        if (p1 == x1 and p2 == x1 and p3 == x1) or (p1 == x1 and p4 == x1 and p7 == x1) or (p1 == x1 and p5 == x1 and p9 == x1) or (p2 == x1 and p5 == x1 and p8 == x1) or (p3 == x1 and p5 == x1 and p7 == x1) or (p3 == x1 and p6 == x1 and p9 == x1) or (p4 == x1 and p5 == x1 and p6 == x1) or (p7 == x1 and p8 == x1 and p9 == x1):
                print(f'Congrats, {x1} have Won the Game !!!')
                game_won = True
        elif (p1 == x2 and p2 == x2 and p3 == x2) or (p1 == x2 and p4 == x2 and p7 == x2) or (p1 == x2 and p5 == x2 and p9 == x2) or (p2 == x2 and p5 == x2 and p8 == x2) or (p3 == x2 and p5 == x2 and p7 == x2) or (p3 == x2 and p6 == x2 and p9 == x2) or (p4 == x2 and p5 == x2 and p6 == x2) or (p7 == x2 and p8 == x2 and p9 == x2):
                print(f'Congrats, {x2} have Won the Game !!!')
                game_won = True
        elif p1 != '' and p2 != '' and p3 != '' and p4 != '' and p5 != '' and p6 != '' and p7 != '' and p8 !='' and p9 !='' :
                print('Its a Tie')
                game_won = True
        else:
            pass


def play_or_not():

    lst = ['yes','no']
    inn = ''

    while inn not in lst:
        inn = input('Do you want to play again(Yes or No): ').lower()

    if inn == 'yes':
        game_on()
    else:
        quit()

def game_on():
    x1, x2 = play_symbol()
    player = whos_first()
    game_inputs(x1, x2, player)
    play_or_not()

game_on()   
