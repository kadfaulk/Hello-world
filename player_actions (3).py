#kadari faulkner 3/12/2021


def check_play_again(user_input):
    #Your code here
    if user_input == "y":
        print("Yes I want to play again")
    elif user_input == "n":
        print("No I don't want to play again")
    else:
        print("invlid input")



#x = input("What is your name?")
#if x == "Ben":
#    print("Hello bro")
#elif x == "Kadari":
#    print("Hello dude")


check_play_again(input("Would you like to play again? Type Y for Yes or N for No: \n"))


