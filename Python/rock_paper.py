import random
game = ''' _______________________________________
|\ ___________________________________ /|
| | _                               _ | |
| |(+)        _           _        (+)| |
| | ~      _--/           \--_      ~ | |
| |       /  /             \  \       | |
| |      /  |               |  \      | |
| |     /   |               |   \     | |
| |     |   |    _______    |   |     | |
| |     |   |    \     /    |   |     | |
| |     \    \_   |   |   _/    /     | |
| |      \     -__|   |__-     /      | |
| |       \_                 _/       | |
| |         --__         __--         | |
| |             --|   |--             | |
| |               |   |               | |
| |                | |                | |
| |                 |                 | |
| |                                   | |
| |         LET'S START GAME          | |
| | _                               _ | |
| |(+)                             (+)| |
| | ~                               ~ | |
|/ ----------------------------------- \|
 ---------------------------------------
'''
print(game)
user_choice = input("Enter Your move(Rock , Paper , Scissor):")
computer_choice = random.choice(["Rock","Paper","Scissor"])
print(user_choice,computer_choice)
if (user_choice==computer_choice):
    print("Match Tie")
elif (user_choice=="Rock"):
    if (computer_choice=="Paper"):
        print("Paper cover rock,Computer Wins")
    else:
        print("Rock Smashes Scissor,You won")
elif(user_choice=="Paper"):
    if(computer_choice=="Scissor"):
        print("Scissor cut Paper, Computer wins")
    else:
        print("Paper Cover Rock You won")
elif(user_choice=="Scissor"):
    if(computer_choice=="Rock"):
        print("Rock Smashes scissor, Computer wins")
    else:
        print("Scissor cut Paper,You won")                            
    