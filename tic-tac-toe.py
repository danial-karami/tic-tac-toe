#! python3

#importing necessary
import random



#variables
#the dictionary of the board
board = {
    'top-L' : ' ','top-M' : ' ', 'top-R' : ' ',
    'mid-L' : ' ','mid-M' : ' ', 'mid-R' : ' ',
    'low-L' : ' ','low-M' : ' ', 'low-R' : ' '
    }


subs = { 1 : 'top-L', 2 : 'top-M', 3 : 'top-R',
         4 : 'mid-L', 5 : 'mid-M', 6 : 'mid-R',
         7 : 'low-L', 8 : 'low-M', 9 : 'low-R' }


#FUNCTION_DEFENITIONS:
#hint function
def hintNote():
    print('This is the hint for your turn:\n')
    print('\
top-L|top-M|top-R\n\
  -------------\n\
mid-L|mid-M|mid-R\n\
  -------------\n\
low-L|low-M|low-R\n')

    
#printBoard function
def printBoard():
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-----')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-----')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
    print('\n')


#checkValidKey function
def checkValidKey():
    check = True
    global userTurn
    while check:
        if userTurn not in board.keys():
            print('You did not choose proper key!!!')
            userTurn = input('Try again: ')
        elif userTurn in board.keys():
            check = False

            
#checkPlace function
def checkPlace():             #checks whether or not choosen place is empty
    check = True
    global userTurn
    while check:
            if computerChar in board[userTurn]:
                print('You did not choose an empty place!!!')
                userTurn = input('Try again: ')
                checkValidKey()
            elif computerChar not in board[userTurn]:
                check = False


def checkCorner(number):     #returns True when the called corner is empty 
    if number == 1:
        if board['top-L'] == ' ':
            return True
    elif number == 3:
        if board['top-R'] == ' ':
            return True
    elif number == 7:
        if board['top-R'] == ' ':
            return True
    elif number == 9:
        if board['top-R'] == ' ':
            return True
        

def user():                  #user function makes the turn of the user
    global userTurn
    userTurn = input('Now it is your turn:')
    checkValidKey()
    checkPlace()
    board[userTurn] = userChar
    

def cornerTurn():            #uses checkCorner function to make a turn  
    for i in [1, 3, 7, 9]:
        if checkCorner(i):
            board[subs[i]] = computerChar
            printBoard()
            break

    
def checkFinalTurn():
    anyChar = ['X', 'O']
    while True:
        if board[subs[1]] == board[subs[2]] in anyChar:
            if board[subs[3]] == ' ':
                    board[subs[3]] = computerChar
                    break 
        if board[subs[1]] == board[subs[3]] in anyChar:
            if board[subs[2]] == ' ':
                    board[subs[2]] = computerChar
                    break
        if board[subs[1]] == board[subs[4]] in anyChar:
            if board[subs[7]] == ' ':
                    board[subs[7]] = computerChar
                    break
        if board[subs[1]] == board[subs[5]] in anyChar:
            if board[subs[9]] == ' ':
                board[subs[9]] = computerChar
                break
        if board[subs[1]] == board[subs[7]] in anyChar:
            if board[subs[4]] == ' ':
                    board[subs[4]] = computerChar
                    break
        if board[subs[1]] == board[subs[9]] in anyChar:
            if board[subs[5]] == ' ':
                    board[subs[5]] = computerChar
                    break
        #done

        if board[subs[2]] == board[subs[3]] in anyChar:
            if board[subs[1]] == ' ':
                    board[subs[1]] = computerChar
                    break
        if board[subs[2]] == board[subs[5]] in anyChar:
            if board[subs[8]] == ' ':
                    board[subs[8]] = computerChar
                    break
        if board[subs[2]] == board[subs[8]] in anyChar:
            if board[subs[5]] == ' ':
                    board[subs[5]] = computerChar
                    break
        #done

        if board[subs[3]] == board[subs[5]] in anyChar:
            if board[subs[7]] == ' ':
                    board[subs[7]] = computerChar
                    break
        if board[subs[3]] == board[subs[6]] in anyChar:
            if board[subs[9]] == ' ':
                    board[subs[9]] = computerChar
                    break
        if board[subs[3]] == board[subs[7]] in anyChar:
            if board[subs[5]] == ' ':
                    board[subs[5]] = computerChar
                    break
        if board[subs[3]] == board[subs[9]] in anyChar:
            if board[subs[6]] == ' ':
                    board[subs[6]] = computerChar
                    break
        #done

        if board[subs[4]] == board[subs[5]] in anyChar:
            if board[subs[6]] == ' ':
                    board[subs[6]] = computerChar
                    break
        if board[subs[4]] == board[subs[6]] in anyChar:
            if board[subs[5]] == ' ':
                    board[subs[5]] = computerChar
                    break
        if board[subs[4]] == board[subs[7]] in anyChar:
            if board[subs[1]] == ' ':
                    board[subs[1]] = computerChar
                    break
        #done

        if board[subs[5]] == board[subs[6]] in anyChar:
            if board[subs[4]] == ' ':
                    board[subs[4]] = computerChar
                    break
        if board[subs[5]] == board[subs[7]] in anyChar:
            if board[subs[3]] == ' ':
                    board[subs[3]] = computerChar
                    break
        if board[subs[5]] == board[subs[8]] in anyChar:
            if board[subs[2]] == ' ':
                    board[subs[2]] = computerChar
                    break
        if board[subs[5]] == board[subs[9]] in anyChar:
            if board[subs[1]] == ' ':
                    board[subs[1]] = computerChar
                    break
        #done

        if board[subs[6]] == board[subs[9]] in anyChar:
            if board[subs[3]] == ' ':
                    board[subs[3]] = computerChar
                    break
        #done

        if board[subs[7]] == board[subs[9]] in anyChar:
            if board[subs[8]] == ' ':
                    board[subs[8]] = computerChar
                    break
        #done

        if board[subs[8]] == board[subs[7]] in anyChar:
            if board[subs[9]] == ' ':
                    board[subs[9]] = computerChar
                    break
        if board[subs[8]] == board[subs[9]] in anyChar:
            if board[subs[7]] == ' ':
                    board[subs[7]] = computerChar
                    break
            continue
        
        #done
        
        else:
            placeList = []
            for randomPlace in subs:
                if board[subs[randomPlace]] == ' ':
                   placeList.append(randomPlace)
                else:
                    continue
            selection = random.choice(placeList)    
            board[subs[selection]] = computerChar
            break

        

def checkWin():      #checks whether or not either user or computer won
    youWin = '-*-*-*-*-*-*-*- YOU WIN -*-*-*-*-*-*-*-'
    youLose = '''--------------------------------------------------\n\
--- Oops --- Game Over --- Computer beaten you ---\n\
--------------------------------------------------'''
    end = True
    if board[subs[1]] == board[subs[4]] == board[subs[7]]:
        if board[subs[1]] == userChar:
            print(youWin)
            return end
        else:
            print(youLose)
            return end    
    elif board[subs[1]] == board[subs[2]] == board[subs[3]]:
        if board[subs[1]] == userChar:
            print(youWin)
            return end
        else:
            print(youLose)
            return end    
    elif board[subs[1]] == board[subs[5]] == board[subs[9]]:
        if board[subs[1]] == userChar:
            print(youWin)
            return end
        else:
            print(youLose)
            return end
    elif board[subs[4]] == board[subs[5]] == board[subs[6]]:
        if board[subs[4]] == userChar:
            print(youWin)
            return end
        else:
            print(youLose)
            return end
    elif board[subs[7]] == board[subs[8]] == board[subs[9]]:
        if board[subs[7]] == userChar:
            print(youWin)
            return end
        else:
            print(youLose)
            return end
    elif board[subs[3]] == board[subs[5]] == board[subs[7]]:
        if board[subs[3]] == userChar:
            print(youWin)
            return end
        else:
            print(youLose)
            return end
    elif board[subs[2]] == board[subs[5]] == board[subs[8]]:
        if board[subs[2]] == userChar:
            print(youWin)
            return end
        else:
            print(youLose)
            return end
    elif board[subs[3]] == board[subs[6]] == board[subs[9]]:
        if board[subs[3]] == userChar:
            print(youWin)
            return end
        else:
            print(youLose)
            return end


def checkEnd():
    anyChar = ['X', 'O']
    endList = []
    for i in subs.keys():
       if board[subs[i]] in anyChar:
           endList.append(i)
           
    if len(endList) == 9:   
       print(' NO MORE TURNS LEFT')
       print(' -------------------')
       print('|No loser, No Winner|')
       print(' -------------------')
       return True


print('-----------------------Welcome to my Tic-Tac-Toe game-----------------------')
hintNote()
#set while loop for main repetition
endEnd = False
while not endEnd:
    #Start
    print('Do you want to be X or O?')
    userChar = input().upper()
    userValidation = True

    while userValidation:
        if userChar == 'X' or userChar == 'O':
            userValidation = False
        elif userChar != 'X' or userChar != 'O':
            print('Please choose X or O: ')
            userChar = input().upper()
            
    if userChar == 'X':
        computerChar = 'O'
    elif userChar == 'O':
        computerChar = 'X'
        
    print('The Computer will be: ' + computerChar)
    print('Well, you choosed your character first, the computer will go first.')

    #the first computer and user turn
    board['mid-M'] = computerChar
    printBoard()
    user()
    printBoard()
    cornerTurn()

    while True:
        user()
        printBoard()
        
        if checkWin():
            break
        if checkEnd():
            break
        
        checkFinalTurn()       #checks if there is a final turn for user
        printBoard()
        
        if checkWin():
            break
        if checkEnd():
            break

    ans = input('Do you want to play again? (yes\\no)').upper()
    if ans == 'YES':
        for i in subs:
            board[subs[i]] = ' '
        continue
    else:
        print('Well, maybe another time.')
        endEnd = True
#TO DO: set a while loop for checking if the input is valid or not   
        


















