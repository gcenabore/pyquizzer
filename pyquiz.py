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
def user_info():
    try:
        while True:
            full_name = input("Please enter your Full Name: ").split()
            first_name = full_name[0]
            surname = full_name[1]

            if first_name.isalpha() and surname.isalpha():
                break

            else:
                print("Invalid: Enter a valid name")

    except IndexError:
        print("Invalid: An error occurred. Please try again.")
    
    try:
        while True:
            age = input("Please enter your Age: ")

            if age.isdigit():
                digit = int(age)
                break
            else:
                print("Invalid: Enter a digit age")
    except ValueError:
        print("Invalid: An error occurred. Please try again.")
    
    try:
        while True: 
            cys = input("Please enter your Course, Year, Section: ").upper()
            if cys.strip():
                break
            else:
                print("Invalid: Course, Year, Section cannot be empty.")

    except ValueError:
        print("Invalid: An error occurred. Please try again.")

user_info()

def quiz(questions):
    score = 0
    for question in questions:
        print(question["question"])
        for option in question["options"]:
            print(option)

quiz(questions)