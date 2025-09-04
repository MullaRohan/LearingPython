# Rock Paper Scissor

# Rock > Scissor
# Paper > Rock
# Paper > Scissor


import random as rn
import msvcrt as ms


def fn(user, pc):
    if user == pc:
        print("The Game is Draw")
    elif (
        (user == "Rock" and pc == "Scissor")
        or (user == "Paper" and pc == "Rock")
        and (user == "Scissor" and pc == "Paper")
    ):
        print("Congratulation, You Win!!!🎉")
    else:
        print("Daamn😣\nYou Lose. Better Luck Next Time")


while True:

    dics = {"r": "Rock", "p": "Paper", "s": "Scissor"}

    print(
        "Rock -> input r\nPaper -> input p\nScissor -> input s\n\nEnter Your Choice: "
    )
    choice = ms.getch().decode().lower()
    if choice not in dics.keys():
        print("inValid Choice")
        continue
    chslist = ["Rock", "Paper", "Scissor"]

    pcchoice = rn.choice(chslist)

    print(f"You Choose: {dics[choice]}\nPC Choose: {pcchoice}\n")
    fn(dics[choice], pcchoice)
    print('\nPress any key to continue.\nExit? "press k"\nEnter: ')
    UserChoice = ms.getch().decode().lower()
    print(
        "------------------------------------------------------------------------------------"
    )
    if UserChoice == "k":
        print("Thanks for play RockPaperScissor")
        break
