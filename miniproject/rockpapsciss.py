# Rock Paper Scissor

# Rock > Scissor
# Paper > Rock
# Paper > Scissor

import random as rn

while True:

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

    dics = {"r": "Rock", "p": "Paper", "s": "Scissor"}

    choice = input(
        "Rock -> input r\nPaper -> input p\nScissor -> input s\n\nEnter Your Choice: "
    )

    chslist = ["Rock", "Paper", "Scissor"]

    pcchoice = rn.choice(chslist)

    print(f"You Choose: {dics[choice]}\nPC Choose: {pcchoice}\n")
    fn(dics[choice], pcchoice)
    inp = input('\nContinue? "y"\nExit? "k"\nEnter: ')
    print(
        "------------------------------------------------------------------------------------"
    )
    if inp == "k":
        break
