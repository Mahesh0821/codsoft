import random
print("* rock   *paper   *scissor")
choice=input("enter your choice: ")
lst=["rock","paper","sissor"]
cmp_choice=random.choice(lst)

if choice=="rock":
    if cmp_choice=="rock":
        print("match tie")
    elif cmp_choice=="paper":
        print("computer wins")
        print("papers covers the rock")
    else:
        print("You wins")
        print("rock smashes the scissor")

elif choice=="paper":
    if cmp_choice=="paper":
        print("match tie")
    elif cmp_choice=="rock":
        print("you wins")
        print("papers covers the rock")
    else:
        print("computer wins")
        print("scissor cuts the paper")

elif choice=="rock":
    if cmp_choice=="rock":
        print("match tie")
    if cmp_choice=="paper":
        print("computer wins")
        print("papers covers the rock")
    else:
        print("You wins")
        print("rock smashes the scissor")
