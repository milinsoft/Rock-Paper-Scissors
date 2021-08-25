def taking_user_input():
    # This function takes a user's input, checks if it's a valid, only ["scissors", "paper", 'rock'] options accepted
    # and returns this input if it's valid or starts over otherwise
    user_choice = input().lower()
    if user_choice not in ["scissors", "paper", 'rock']:
        print("incorrect option selected, please try again")
        return taking_user_input()
    return user_choice


def computers_choice(user_choice):
    # as in this stage of program computer must always win, this function takes user's input value as an argument,
    # and uses the dict to pick an option for computer that defeats the one picked by the user, and
    # returns picked option for computer
    combinations = {'rock':'paper', 'paper':'scissors', 'scissors':'rock'}
    comp_choice = combinations[user_choice]
    return comp_choice


if __name__ == "__main__":
    user_choice = taking_user_input()
    computer = computers_choice(user_choice)
    print(f"Sorry, but the computer chose {computer}")

