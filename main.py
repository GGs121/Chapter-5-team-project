import random


def main():
    
    continue_program = "y"
    min_val = 1 #set default min and max value
    max_val = 1000



    if continue_program == 'y': #input validation
        while continue_program.lower() == "y": #menu
            print("--- Number Guessing Game ---")
            print("1. Start New Game")
            print("2. Choose Range")
            print("3. Exit")
            
            choice = input(":> ")
            print()

            if choice == "1":
                player1, player2 = get_player_names()
                secret_number = generate_num(min_val, max_val)
                play_game(player1, player2, secret_number, min_val, max_val)

            elif choice == "2":
                min_val = int(input("Enter the minimum value: "))
                max_val = int(input("Enter the maximum value: "))
                print(f"Range is now {min_val} and {max_val}")
                print()

            elif choice == "3":
                print("Thank you for playing")
                break

            else:
                print("Please choose a valid menu option.")
                
            continue_program = input("Would you like to return to the main menu? (y/n): ")
            print()
        else:
            print('thanks for playing')





def get_player_names(): #get_player_names accepts no arguements
    #has user input their names and stroes them in variables
    
    player1 = input("Enter Player 1's name: ")
    player2 = input("Enter Player 2's name: ")
    return player1, player2
    

def generate_num(min_val, max_val): #generate num accepts two arguements which are min_val and max_val
    #generate the secret number for player to guess 
    secret_number = random.randint(min_val, max_val)
    return secret_number
    

def play_game(player1, player2, secret_number):
    
    
    attempts_p1 = 0 #set player 1's turns
    attempts_p2 = 0 #set player 2 turns
    total_turns = 0 #set total turns
    win = 1 #checks if the number is correct
    while win == 1:  
        p1g = int(input(f'{player1} please enter your guess between {min_val} and {max_val}: '))
        p2g = int(input(f'{player2} please enter your guess between {min_val} and {max_val}: '))
         
        if p1g > secret_number:
            print(player1, 'needs to guess lower')
            attempts_p1 += 1
        elif p1g < secret_number:
            print(player2, 'needs to guess higher')
            attempts_p1 += 1
        if p1g == secret_number:
            print('WINNER!!!')
            print()
            print(player1, 'used', attempts_p1, 'turns')
            print(player2, 'used', attempts_p1, 'turns')
            print('total turns used', total_turns)
            print()
            break
            
        if p2g > secret_number:
            print(player2, 'needs to guess lower')
            attempts_p2 += 1
        elif p2g < secret_number:
            print(player2, 'needs to guess higher')
            attempts_p2 += 1
        if p2g == secret_number:
            print('WINNER!!!')
            print()
            print(player1, 'used', attempts_p1, 'turns')
            print(player2, 'used', attempts_p1, 'turns')
            print('total turns used', total_turns)
            print()


main()
