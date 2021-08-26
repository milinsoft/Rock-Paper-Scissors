# globals can be accessed without passing as arguments
import random


def taking_user_input():
    # This function takes a user's input, checks if it's a valid, only ["scissors", "paper", 'rock'] options accepted
    # and returns this input if it's valid or starts over otherwise
    # at the 3rd stage "!exit" and "Bye!" options added to stop the game.
    user_option = input().lower()
    if user_option not in combinations:
        if user_option == "!exit" or user_option == "Bye!":
            exit()
        elif user_option == "!rating":
            show_rating()
            return taking_user_input()
        else:
            print("Invalid input")
            exit()
    return user_option


# noinspection PyTypeChecker
def obtain_score():
    with open("rating.txt", "r+") as f1:  # "r+" opens for reading and writing.
        score_list = dict([x.rstrip(r"\n").split() for x in f1])
    return int(score_list[username]) if username in score_list else 0


def show_rating():
    print("Your rating: ", user_score)


def pc_random_choice():
    # as at 2nd stage of the program computer depict an option randomly - the function no longer takes any arguments and returns random pc choice.
    return random.choice(combinations)


def output_result():
    global user_score
    n = combinations.index(user_choice)  # finding an index of user_choice in combination list
    winning_cases = combinations[n+1:] + combinations[:n]
    winning_cases = winning_cases[0:(len(winning_cases)//2)]
    if pc_option == user_choice:
        user_score += 50
        print(f"There is a draw ({pc_option})")
    elif pc_option not in winning_cases:
        print(f"Well done. The computer chose {pc_option} and failed")
        user_score += 100
    else:
        # user_score is not affected in this case
        print(f"Sorry, but the computer chose {pc_option}")


def set_game_mode():
    options_set = input()
    print("Okay, let's start")
    return ["rock", "paper", "scissors"] if options_set == "" else options_set.split(",")


if __name__ == "__main__":
    username = input("Enter your name: ")
    print("Hello,", username)
    combinations = set_game_mode()
    user_score = obtain_score()
    while True:
        user_choice = taking_user_input()
        pc_option = pc_random_choice()
        output_result()
