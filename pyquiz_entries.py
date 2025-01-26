import time
import sys

def typing_animation(text, delay= 0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Move to the next line after the animation
separator = "=" * 76

print(separator)
typing_animation("=====TYPE THE USER'S FULL NAME TO ACQUIRE THEIR RESULT AND INFORMATION======")
print(separator)


while True:
    first_name = input("Enter First name: ").capitalize()
    surname = input("Enter Surname: ").capitalize()

    user_name = first_name + " " + surname
    found = False

    with open("pyquiz_result.txt", "r") as f:

        for line in f:
            if user_name in line:
                found = True
                print(separator)
                typing_animation(f"RESULT FOUND: Result for {user_name}: ")
                print(line.strip())

                for line in range(6):
                    try:
                        typing_animation(next(f).strip())
                    except StopIteration:
                        break
                print(separator)
                break

        if not found:
            typing_animation(f"ERROR: THERE IS NO EXISTING RESULT FOR: {user_name}")
    
    retry = input("Do you want to search again? (Yes/No)").strip().lower()
    print(separator)
    if retry != "yes":
        break






