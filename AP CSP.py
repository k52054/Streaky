
habits = ["Exercise", "Read 10 Pages", "Practice Python"]

def progress(habit_list):
    total_habits = len(habit_list)
    count = 0

    print("\nDaily Check-in")

    for h in habit_list:
        user_choice = input("Did you " + h + " today? (y/n): ")
        if user_choice.lower() == "y":
            count += 1
    percentage = (count / total_habits) * 100
    return percentage

def results(score):
    print("\nResults")
    print("You completed " + str(score) + "% of your habits today.")
    if score == 100:
        print("Perfect Day! 100% complete.")
    elif score >= 50:
        print("Good job! You did more than half.")
    else:
        print("Tomorrow is a new chance!")


print("Welcome to your Daily Habit Tracker!")

run = True
while run:
    user_input = input("Do you want to \nAdd a new Habit - 1 \nCheck off your Habits - 2 \nEnter option :")
    if user_input == "1":
        new_habit = input("Enter a new habit to track: ")
        if new_habit in habits:
            useInput = input("Are you sure you want to add a duplicate? (y/n): ")
            if useInput.lower() == "y":
                habits.append(new_habit)
        else:
            habits.append(new_habit)
    elif user_input == "2":
        score = progress(habits)
        results(score)
        break
    else:
        print("Enter proper value")
