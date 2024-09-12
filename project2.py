'''
Project 2 - Shut The Box - Spring 2024  
Author: Aayush Narang (anarang27)

Shut The Box is a one player game that starts with a board that contains the numbers 1 through 9.
The player's turn involves rolling two six-sided die and choosing any combination of numbers on
the board that sum to the player's roll, which then eliminates the numbers from the board.
The player repeats their turn until either all the numbers on the board are zero or there are
no numbers on the board that sum to the players roll. The player wins if they can turn the entire
board to all zeros. 

I have neither given or received unauthorized assistance on this assignment.
Signed:  Aayush Narang

'''


import random

from project2_fcn import can_play


def print_board(board, dice1, dice2):
    
    '''
This function prints the board and the 2 dies. Furthermore, it also creates a display board which
replaces the zeroes with dashes. Then it prints the display board and the 2 dies.

'''
 
    display_board = []
    for num in board:
        if num == 0:
            display_board.append('-')
        else:
            display_board.append(num)  
    
    print(*display_board)
    print('dice1 = ' + str(dice1))
    print('dice2 = ' + str(dice2))
    
      

def get_input():
    
    '''
This function has zero parameters and return the input that the user gave in the form of a list of integers. It gets the
input from the user and does a single check of input validation which is checking whether or not the input consists of
2 numbers. First the input is taken from the user, then the input is made into a list using the split() method. Then it
checks whether or not the lsit contains only digits. Finally, once it's done with the check, the list is converted back
into integers.

'''

    while True:
        user_input = input('The numbers should sum to the total roll: ')
        input_list = user_input.split()
        
        valid_input = True
        for num in input_list:
            if num.isdigit() == False:
                valid_input = False
                print("Invalid input. Please enter only numbers.")
                break
                
        if valid_input == True:
            converted_input = []
            for num in input_list:
                converted_input.append(int(num))
            return converted_input


def check_input(user_input, board, total_roll_value):
    
    '''
This function has the user input, the board, and the total roll value as its parameters. It check the user input for any red flags
which include the values the of dies not totalling what the user put, putting duplicate numbers, and even if the number is not on
the board. The total roll value is checked by using comparison operators on the sum of the user input list and the duplicates are
checked by making a copy of the board. This function returns a boolean depending on whether the input entered is valid or not.

'''
    
    board_copy = board.copy()

    if sum(user_input) != total_roll_value:
        print("Input error: The sum of " + str(user_input) + " does not equal "  + str(total_roll_value) + ".")
        return False

    for num in user_input:
        if num not in board:
            print(str(num) + " is not on the board.")
            return False
    
        if num not in board_copy:
            print("You cannot enter the same number twice.")
            return False       
        else:
            board_copy.remove(num)
                    
    return True
        
   
def check_win(board):
    
    '''
This function takes in the board as its parameter and returns a boolean depending on if the game has been won. It returns false if
all the numbers on the board are not 0 and true if they are.

'''
    
    for num in board:
        if num != 0:
            return False
        
    return True
  
   
def main():
    
    '''
This function is the main driver of the program. Firstly, the board is initialized and the opening statement to the gam is printed.
Then the two dies are initialized using the random package. After that, a while loop is set up so that while it is true, the board
keeps printing and the program keeps checking whether the game can be played using the can_play function. Here, the program also
changes the numbers to zeroes when entered from the users end and then prints the final message of the game by calling the check_win
function.

'''
    
    
    board = [1,2,3,4,5,6,7,8,9]
    print('Welcome to Shut The Box')
    
    while True:
        
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        total_roll_value = dice1 + dice2
        print_board(board, dice1, dice2)
        
        
        if can_play(board, dice1, dice2):
            print('Enter the numbers you want to eliminate (separated by spaces)')
            user_input = get_input()
            
            
            if check_input(user_input, board, total_roll_value):
                for num in user_input:
                    board[num -1] = 0
        
        else:
            print('You have no moves left :( \nBetter luck next time!')
            
            break
        
        if check_win(board):
            print("You Shut The Box!")
            break
           
    


if __name__ == '__main__':
    main()
    
    
    

    