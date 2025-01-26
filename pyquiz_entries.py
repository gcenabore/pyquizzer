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

full_name = input("Enter Full name: ").split()
user_name = full_name[0] + " " + full_name[1]

found = False

with open("pyquiz_result.txt", "r") as f:
    for line in f:
        if user_name in line:
            found = True
            typing_animation(f"RESULT FOUND: Result for {user_name}: ")
            print(line.strip())
            print("_" * 100)
            break

    if not found:
        print(f"ERROR: THERE IS NO EXISTING RESULT FOR: {user_name}")    




