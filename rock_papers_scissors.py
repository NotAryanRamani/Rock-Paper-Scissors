import random

print("Welcome to Rock, Papers, Scissors!")

cpu_points = 0
user_points = 0

valid_moves = ['Rock', 'Papers', 'Scissors']

while cpu_points != 3 and user_points != 3:
    cpu_move = random.choice(valid_moves).capitalize()
    user_move = input("Select your move: ").capitalize()
    print("CPU chose ", cpu_move)
    if user_move == valid_moves[0]:
        if cpu_move == valid_moves[1]:
            cpu_points += 1
            print("CPU won this round! CPU Points: ", cpu_points)
        elif cpu_move == valid_moves[2]:
            user_points += 1
            print("User won this round! User Points: ", user_points)
        else:
            print("Its a Draw! CPU points: ", cpu_points, ", User Points: ", user_points)
    elif user_move == valid_moves[1]:
        if cpu_move == valid_moves[2]:
            cpu_points += 1
            print("CPU won this round! CPU Points: ", cpu_points)
        elif cpu_move == valid_moves[0]:
            user_points += 1
            print("User won this round! User Points: ", user_points)
        else:
            print("Its a Draw! CPU points: ", cpu_points, ", User Points: ", user_points)
    elif user_move == valid_moves[2]:
        if cpu_move == valid_moves[0]:
            cpu_points += 1
            print("CPU won this round! CPU Points: ", cpu_points)
        elif cpu_move == valid_moves[1]:
            user_points += 1
            print("User won this round! User Points: ", user_points)
        else:
            print("Its a Draw! CPU points: ", cpu_points, ", User Points: ", user_points)
    else:
        print("Please choose a valid move!")

if cpu_points == 3:
    print("CPU wins!")
elif user_points == 3:
    print("You win!")

print("Thanks for playing!")