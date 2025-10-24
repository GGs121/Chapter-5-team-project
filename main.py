def main():
    
    def menu():

    
        if choice == 1:
            
            getnames()
            start_new_game()
        elif choice == 2:
            
            setrang()
        else:
            stopfunc()
        
    
        
    menu()
    
def start_new_game(minrange, maxrange, name1, name2, randnum):
    win = 1
    totalturns = 0
    while win == 1:
        player1g = int(input('\n',name1,'guees your number inbetween',minrange, 'and', maxrange))
        
        if player1g == randnum:
            print('WINNER!!!')
            win = 0
        if player1g > randum:
            print('guess lower')
            print()
            
        if player1g < randum:
            print('guess higher')
            print()
            
        player2g = int(input('\n',name2,'guees your number inbetween',minrange, 'and', maxrange))
        
        if player2g == randnum:
            print('WINNER!!!')
            win = 0
            
        if player2g > randum:
            print('guess lower')
            print()
            
        if player2g < randum:
            print('guess higher')
            print()
            
        totalturns = totalturns + 1
        print('TURN COUNT: ',totalturns)
        
main()