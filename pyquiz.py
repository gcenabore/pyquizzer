#create a list of questions
#ask the user's info before answering the questions
#set conditions for the answers
#ask the user for answer, if correct, print correct, otherwise print incorrect
#count the number of correct answers
#store the user's info and score in a txt file, to find their data later
#display the user's score
import time
import sys

def typing_animation(text, delay= 0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Move to the next line after the animation

questions = [
    { 
        "question": "1. Who is the creator of python?",
        "options": ["A. Dennis Ritchie", "B. Guido Van Rossum", "C. James Gosling", "D. Brendan Eich"],
        "answer": "B"
    },

    {
        "question": "2. In which year was python released?",
        "options": ["A. 1991", "B. 1989", "C. 1995", "D. 2000"],
        "answer": "A"
    },

    {
        "question": "3. The name 'python' was derived from which of the following?",
        "options": ["A. A type of snake", "B. A british comedy troupe", "C. A scientific term", "D. An acronym"],
        "answer": "B"
    },

    {
        "question": "4. Which of the following is NOT a key philosophy of Python as stated in 'The Zen of Python'?",
        "options": ["A. Readability counts", "B. Complex is better than simple", "C. There should be one—and preferably only one—obvious way to do it", "D. Speed is the most important feature"],
        "answer": "D"
    },

    {
        "question": "5. Python 2 was officially discontinued in which year?",
        "options": ["A. 2020", "B. 2019", "C. 2021", "D. 2022"],
        "answer": "A"
    }

]

separator = "=" * 75

def start_quiz():
    print(separator)
    start = input("Are you ready to start the quiz? (yes/no): ").lower()
    if start == "no":
        print(separator)
        typing_animation("                             Okay, Goodbye!                                    ")
        print(separator)
        exit()
    else:
        print(separator)
        start == "yes"
        print(separator)
        typing_animation("                     Welcome to the Python Quiz!                     ",)
        typing_animation("          You will be presented with 5 multiple choice questions.          ")
        typing_animation("               Enter the letter of the correct answer.               ")
        typing_animation("                        Let's get started!                        ")
        print(separator)

start_quiz()

def user_info(questions):

    with open("user_info.txt", "a") as file:
        while True:
            try:
                full_name = input("Please enter your Full Name: ").split()
                full_name = [name.title() for name in full_name]
                if len(full_name) < 2 or not all(name.isalpha() for name in full_name):
                    raise ValueError(typing_animation("Invalid: Enter a valid FULL NAME"))

                age = input("Please enter your Age: ")
                if not age.isdigit():
                    raise ValueError(typing_animation("Invalid: Enter a DIGIT AGE"))
                digit = int(age)

                cys = input("Please enter your Course, Year, Section: ").upper()
                if not cys.strip():
                    raise ValueError(typing_animation("Invalid: Course, Year, Section cannot be EMPTY."))
                break  
            except ValueError as e:
                print(e)
            
        score = 0
        for question in questions:
            print(separator,"\n", question["question"], "\n")
            for option in question["options"]:
                print(option)
            answer = input("Enter your answer: ").upper()

            if answer == question["answer"]:
                print(separator)
                typing_animation("              Correct! yeheyy! Tama ka perd Congrats!!              ")
                print(separator, "\n")
                score += 1
            else:
                print(separator)
                typing_animation("               Incorrect!! Mali ka! Try again next time parekoy!               ")
                print(separator, "\n")

        print(separator)
        typing_animation("                         Quiz Completed!                         ")
        typing_animation(f"              You got {score} out of {len(questions)} questions correct.              ")
        typing_animation("                  Thank you for participating!                  ")
        print(separator)

        file.write(separator + "\n")
        file.write(f"Full Name: {' '.join(full_name)}\n")
        file.write(f"Age: {digit}\n")
        file.write(f"Course, Year, Section: {cys}\n")
        file.write(f"Score: {score}/{len(questions)}\n")
        file.write(separator + "\n")

user_info(questions)


# def quiz(questions):
#     score = 0
#     for question in questions:
#         print(separator,"\n", question["question"], "\n")
#         for option in question["options"]:
#             print(option)
#         answer = input("Enter your answer: ").upper()

#         if answer == question["answer"]:
#             print(separator)
#             print("              Correct! yeheyy! Tama ka perd Congrats!!")
#             print(separator, "\n")
#             score += 1
#         else:
#             print(separator)
#             print("               Incorrect!! Mali ka! Try again next time parekoy!")
#             print(separator, "\n")
#     print(separator)
#     print("                         Quiz Completed!")
#     print(f"              You got {score} out of {len(questions)} questions correct.")
#     print("                  Thank you for participating!")
#     print(separator)

# quiz(questions)