import random

def taking_user_input():
    # This function takes a user's input, checks if it's a valid, only ["scissors", "paper", 'rock'] options accepted
    # and returns this input if it's valid or starts over otherwise
    # at the 3rd stage "!exit" and "Bye!" options added to stop the game.
    user_choice = input().lower()
    if user_choice not in ["scissors", "paper", 'rock']:
        if user_choice == "!exit" or user_choice == "Bye!":
            exit()
        else:
            print("Invalid input")
            exit()
            #return taking_user_input()
    return user_choice


def pc_random_choice():
    # as at 2nd stage of the program computer depict an option randomly - the function no longer takes any arguments and returns random pc choice.
    pc_choice = random.choice(('rock', 'paper', 'scissors'))
    return pc_choice

def output_result(user_choice, pc_option):
    combinations = {'rock':'paper', 'paper':'scissors', 'scissors':'rock'}
    if combinations[pc_option] == user_choice:
        print(f"Well done. The computer chose {pc_option} and failed")
    elif combinations[user_choice] == pc_option:
        print(f"Sorry, but the computer chose {pc_option}")
    else:
        print(f"There is a draw ({pc_option})")


if __name__ == "__main__":
    while True:
        user_choice = taking_user_input()
        pc_option = pc_random_choice()
        output_result(user_choice, pc_option)
