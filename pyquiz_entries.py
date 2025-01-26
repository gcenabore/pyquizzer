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

