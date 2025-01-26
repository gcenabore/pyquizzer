#create a list of questions
#ask the user's info before answering the questions
#set conditions for the answers
#ask the user for answer, if correct, print correct, otherwise print incorrect
#count the number of correct answers
#store the user's info and score in a txt file, to find their data later
#display the user's score

questions = [
    { 
        "question": "Who is the creator of python?",
        "options": ["A. Dennis Ritchie", "B. Guido Van Rossum", "C. James Gosling", "D. Brendan Eich"],
        "answer": "B"
    },

    {
        "question": "In which year was python released?",
        "options": ["A. 1991", "B. 1989", "C. 1995", "D. 2000"],
        "answer": "A"
    },

    {
        "question": "The name 'python' was derived from which of the following?",
        "options": ["A. A type of snake", "B. A british comedy troupe", "C. A scientific term", "D. An acronym"],
        "answer": "B"
    },

    {
        "question": "Which of the following is NOT a key philosophy of Python as stated in 'The Zen of Python'?",
        "options": ["A. Readability counts", "B. Complex is better than simple", "C. There should be one—and preferably only one—obvious way to do it", "D. Speed is the most important feature"],
        "answer": "D"
    },

    {
        "question": "Python 2 was officially discontinued in which year?",
        "options": ["A. 2020", "B. 2019", "C. 2021", "D. 2022"],
        "answer": "A"
    }

]

separator = "=" * 50

def start_quiz():
    print(separator)
    start = input("Are you ready to start the quiz? (yes/no): ").lower()
    if start == "no":
        print(separator)
        print("                 Okay, Goodbye!")
        print(separator)
        exit()
    else:
        print(separator)
        start == "yes"
        print(separator)
        print("                Welcome to the Python Quiz!",)
        print("     You will be presented with 5 multiple choice questions.")
        print("          Enter the letter of the correct answer.")
        print("                   Let's get started!")
        print(separator)

start_quiz()

def user_info():

    while True:
        try:
            full_name = input("Please enter your Full Name: ").split()

            if len(full_name) < 2 or not all(name.isalpha() for name in full_name):
                raise ValueError("Invalid: Enter a valid FULL NAME")

            age = input("Please enter your Age: ")
            if not age.isdigit():
                raise ValueError("Invalid: Enter a DIGIT AGE")
            digit = int(age)

            cys = input("Please enter your Course, Year, Section: ").upper()
            if not cys.strip():
                raise ValueError("Invalid: Course, Year, Section cannot be EMPTY.")
            break  

        except ValueError as e:
            print(e)
user_info()


def quiz(questions):
    score = 0
    for question in questions:
        print(question["question"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer: ").upper()

        if answer == question["answer"]:
            print("Correct! yeheyy! Tama ka perd Congrats!!")
            score += 1
        else:
            print("Incorrect!! Mali ka! Try again next time parekoy!")
    print(f"you got {score} out of {len(questions)} questions correct.")
quiz(questions)