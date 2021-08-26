import random
#random.seed(0)

def taking_user_input(user_score):
    # This function takes a user's input, checks if it's a valid, only ["scissors", "paper", 'rock'] options accepted
    # and returns this input if it's valid or starts over otherwise
    # at the 3rd stage "!exit" and "Bye!" options added to stop the game.
    user_choice = input().lower()
    if user_choice not in ["scissors", "paper", 'rock']:
        if user_choice == "!exit" or user_choice == "Bye!":
            exit()
        elif user_choice == "!rating":
            print("Your rating: ", user_score)
            return taking_user_input(user_score)
        else:
            print("Invalid input")
            exit()
            #return taking_user_input()
    return user_choice

def great_user(username):
    print("Hello,", username)


def obtain_score(username):
    with open("rating.txt", "r+") as f1:  # "r+" opens for reading and writing.
        score_list = dict([x.rstrip("\n").split() for x in f1])
        #print(score_list)
        if username in score_list:
            user_score = score_list[username]
        else:
            user_score = 0
    return int(user_score)


def show_rating(username):
    with open("rating.txt", "r+") as f1:  # "r+" opens for reading and writing.
        score_list = dict([x.rstrip("\n").split() for x in f1])
        #print(score_list)
        if username in score_list:
            print("Your rating: ", score_list[username])
        else:
            print("Your rating: 0")


def pc_random_choice():
    # as at 2nd stage of the program computer depict an option randomly - the function no longer takes any arguments and returns random pc choice.
    pc_choice = random.choice(('rock', 'paper', 'scissors'))
    return pc_choice


def output_result(user_choice, pc_option):
    global user_score
    combinations = {'rock':'paper', 'paper':'scissors', 'scissors':'rock'}
    if combinations[pc_option] == user_choice:
        user_score += 100
        print(f"Well done. The computer chose {pc_option} and failed")
    elif combinations[user_choice] == pc_option:
        # user_score is not affected in this case
        print(f"Sorry, but the computer chose {pc_option}")
    else:
        user_score += 50
        print(f"There is a draw ({pc_option})")


if __name__ == "__main__":
    username = input("Enter your name: ")
    great_user(username)
    user_score = obtain_score(username)

    while True:
        user_choice = taking_user_input(user_score)
        pc_option = pc_random_choice()
        output_result(user_choice, pc_option)
