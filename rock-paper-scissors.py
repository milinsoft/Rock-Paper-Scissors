import random


def taking_user_input():
    # This function takes and validates the user's input, as only options in a var "combinations" accepted
    # if validation passed successfully returns this input or starts the function over otherwise.
    # Additional options: "!exit" and "Bye!" commands interrupt program execution. "!rating" shows current user_score
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
    # This function determines an initial score, by opening "rating.txt" file for reading and writing (mode "r+").
    # if user's previous score is in "rating.txt" file, this score returned and user continues the game starting with the previous number
    # 0 returned otherwise
    with open("rating.txt", "r+") as f1:
        score_list = dict([x.rstrip(r"\n").split() for x in f1])
    return int(score_list[username]) if username in score_list else 0


def show_rating():
    # This function simply print's current user_score
    print("Your rating: ", user_score)


def pc_random_choice():
    # This function returns random option available in combinations list
    return random.choice(combinations)


def output_result():
    # This function access global user_score and updates it based on mid-game results.
    # To determine the winner the following algorithm implemented: combinations list splits into
    # two parts, and all elements that followed user_choice moved to the beginning of the list, then list is divided into two parts,
    # int division is used, even if number of choices is even. The first part of this sliced list are the winning options for PC.
    # if computer's choice is the same as users  - result is "draw" and 50 points added
    # if computer's choice in "winning_cases" then user lose and no points received,
    # otherwise user wins and 100 points received.

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
    options_set = input("please provide list of game options separated by comma like 'a,b,c' or press enter/return to play with with old good 'rock', 'paper', 'scissors'")
    print("Okay, let's start")
    return ["rock", "paper", "scissors"] if options_set == "" else options_set.split(",")


if __name__ == "__main__":
    print("DISCLAIMER: print '!exit' or 'Bye!' to stop the game")
    # calls main game logic
    username = input("Enter your name: ")  # setting username
    print("Hello,", username)  # greeting user
    combinations = set_game_mode()  # calling the function that  obtaining from input list of "playable options" in case user want use it's own.
    user_score = obtain_score()  # calling the function that sets an initial user_score
    # Initiating the infinite loop to make sure that game continues until user will enter "!exit" or "Bye!" to stop.
    while True:
        user_choice = taking_user_input()
        pc_option = pc_random_choice()
        output_result()
    # globals can be accessed without passing as arguments
