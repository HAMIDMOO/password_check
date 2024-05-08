import random
lst = [1, 2, 3]


def player_action():
    player = input("enter your action... ")
    if player == "rock":
        player = 3
    elif player == "paper":
        player = 2
    elif player == "scissors":
        player = 1
    else:
        contin = input("your action has not known try again? Y or N")
        if contin == "Y":
            player_action()
    return player



def winner():
    player_1_point = 0
    player_2_point = 0
    player_2 = int(random.choice(lst))
    player_1= player_action()
  
    for i in range(0, 5):

        if player_2 == player_1:
            print("action {}th ".format(i+1))
            print("your action is {}   and the system action is {} ".format(player_1, player_2))
            print("Your point -> ",player_1_point,"   ","system point -> " , player_2_point)
            print("------------------------------------------")
            
            if (i+1) <=4:
                player_1 = player_action()
                player_2 = int(random.choice(lst))

        elif player_1 == 1 and player_2 == 2:
            player_1_point += 1
            print("action {}th ".format(i+1))
            print("your action is {}   and the system action is {} ".format(player_1, player_2))
            print("Your point -> ",player_1_point,"   ","system point -> " , player_2_point)
            print("------------------------------------------")           
            if (i+1) <=4:
                player_1 = player_action()
                player_2 = int(random.choice(lst))


        elif player_1 == 1 and player_2 == 3:
            player_2_point += 1
            print("action {}th ".format(i+1))
            print("your action is {}   and the system action is {} ".format(player_1, player_2))
            print("Your point -> ",player_1_point,"   ","system point -> " , player_2_point)
            print("------------------------------------------")      
            if (i+1) <=4:
                player_1 = player_action()
                player_2 = int(random.choice(lst))


        elif player_1 == 2 and player_2 == 1:
            player_2_point += 1
            print("action {}th ".format(i+1))
            print("your action is {}   and the system action is {} ".format(player_1, player_2))
            print("Your point -> ",player_1_point,"   ","system point -> " , player_2_point)
            print("------------------------------------------")
            
            if (i+1) <=4:
                player_1 = player_action()
                player_2 = int(random.choice(lst))


        elif player_1 == 2 and player_2 == 3:
            player_1_point += 1
            print("action {}th ".format(i+1))
            print("your action is {}   and the system action is {} ".format(player_1, player_2))
            print("Your point -> ",player_1_point,"   ","system point -> " , player_2_point)
            print("------------------------------------------")
            
            if (i+1) <=4:
                player_1 = player_action()
                player_2 = int(random.choice(lst))


        elif player_1 == 3 and player_2 == 1:
            player_1_point += 1
            print("action {}th ".format(i+1))
            print("your action is {}   and the system action is {} ".format(player_1, player_2))
            print("Your point -> ",player_1_point,"   ","system point -> " , player_2_point)
            print("------------------------------------------")
            
            if (i+1) <=4:
                player_1 = player_action()
                player_2 = int(random.choice(lst))

        elif player_1 == 3 and player_2 == 2:
            player_2_point += 1
            print("action {}th ".format(i+1))
            print("your action is {}   and the system action is {} ".format(player_1, player_2))
            print("Your point -> ",player_1_point,"   ","system point -> " , player_2_point)
            print("------------------------------------------")
            
            if (i+1) <=4:
                player_1 = player_action()
                player_2 = int(random.choice(lst))

        
    if player_1_point > player_2_point:
        print("------------------------------------------")
        print(player_1_point,"   ",  player_2_point)
        print("the winner is playeeerrrrrr1111111111")
        
    elif player_2_point > player_1_point:
        print("------------------------------------------")
        print(player_1_point,"   ",  player_2_point)
        print("the winner is playeeerrrrrr222222")
    else:
        print("------------------------------------------")
        print(player_1_point,"   ",  player_2_point)
        print("ddrrraaawwwwww")


winner()
