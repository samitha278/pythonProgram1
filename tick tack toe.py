def checker(dict):
    '''check who wins according to given dictionary'''
    alist = ["X ","O "]

    b_value = False

    #check all wining conditions
    for index,j in enumerate(alist):

        #check horizontal conditions
        for i in range(3):
            condition_1 = dict[1+3*i]==j and dict[2+3*i]==j and dict[3+3*i]==j
            condition_2 = dict[1+i]==j and dict[4+i]==j and dict[7+i]==j

            if condition_1 == True or condition_2 == True:
                print(f"player {index+1} wins!!")
                b_value = True
                
        #check diagonal conditions    
        for i in range(2):
            condition_3 = dict[1+i*2]==j and dict[5]==j and dict[9-i*2]==j

            if condition_3 == True:
                print(f"player {index+1} wins!!")
                b_value = True

    return b_value
    

def print_dict(dict):
    '''print given dictionary's value like 3*3 squre'''

    for num in dict:
        print(dict[num],end="")

        if num%3==0:
            print()
    return 0


def play_game():
    '''tick tack toe game function'''

    #main dictionary to route game
    dict = {
        1:"_ ",2:"_ ",3:"_ ",
        4:"_ ",5:"_ ",6:"_ ",
        7:"_ ",8:"_ ",9:"_ "
        }

    #print dictionary
    print_dict(dict)
    
    counter = 0

    #loop break when certain conditions met
    while True:
        #input number from player 1 and player 2
        num = int(input())
        
        if counter%2==0:
            dict[num] = "X "
        else:
            dict[num] = "O "

        #print dictionary
        print_dict(dict)

        #increasing counter by 1
        counter += 1

        #check who wins or not
        if checker(dict):
            break
        
        if counter == 9:
            print("Draw!")
            break

    return 0


def main():
    play_game()

if __name__ == '__main__':
    main()
