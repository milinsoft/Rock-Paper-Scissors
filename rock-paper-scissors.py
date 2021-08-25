import random
#random.seed(0)

def taking_user_input():
    # This function takes a user's input, checks if it's a valid, only ["scissors", "paper", 'rock'] options accepted
    # and returns this input if it's valid or starts over otherwise
    user_choice = input().lower()
    if user_choice not in ["scissors", "paper", 'rock']:
        print("incorrect option selected, please try again")
        return taking_user_input()
    return user_choice


def pc_random_choice():
    # as at 2nd stage of the program computer depict an option randomly - the function no longer takes any arguments and returns random pc choice.
    pc_choice = random.choice(('rock', 'paper', 'scissors'))
    return pc_choice

def output_result(user_choice, pc_option):
    # this function uses combinations dictionary to choose the winner.
    # "combinations" keys are the options of the game and it's keys represents the option that defeats the key
    # This function does not return anything, but prints out the result.
    combinations = {'rock':'paper', 'paper':'scissors', 'scissors':'rock'}
    if combinations[pc_option] == user_choice:
        print(f"Well done. The computer chose {pc_option} and failed")
    elif combinations[user_choice] == pc_option:
        print(f"Sorry, but the computer chose {pc_option}")
    else:
        print(f"There is a draw ({pc_option})")


if __name__ == "__main__":
    user_choice = taking_user_input()
    pc_option = pc_random_choice()
    output_result(user_choice, pc_option)



