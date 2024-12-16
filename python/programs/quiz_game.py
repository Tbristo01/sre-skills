# Python Quiz Game
questions = (
    "Which team has won the most NBA championships?",
    "Who is known as 'His Airness' in basketball?",
    "Which player holds the record for the most points scored in a single NBA game?",
    "What team did Kobe Bryant spend his entire career with?",
    "Which NBA team is known as 'The Big Apple' team?"
)

options = (
    ("A. Chicago Bulls", "B. Boston Celtics",
     "C. Los Angeles Lakers", "D. Golden State Warriors"),
    ("A. Michael Jordan", "B. LeBron James", "C. Magic Johnson", "D. Kobe Bryant"),
    ("A. Wilt Chamberlain", "B. Michael Jordan",
     "C. Karl Malone", "D. Kareem Abdul-Jabbar"),
    ("A. Chicago Bulls", "B. Los Angeles Clippers",
     "C. Los Angeles Lakers", "D. San Antonio Spurs"),
    ("A. Brooklyn Nets", "B. Miami Heat",
     "C. New York Knicks", "D. Philadelphia 76ers")
)

# Answer key
answer_key = ("B", "A", "A", "C", "C")


guesses = []
score = 0
question_num = 0

for question in questions:
    print("*"*60)
    print(question)
    for option in options[question_num]:
        print(option)
    print()
    guess= input("Enter (A,B,C,D): ").upper()
    guesses.append(guess)

    if guess==answer_key[question_num]:
        score+=1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"{answer_key[question_num]} is the correct answer!")

    question_num+=1
print("*"*60)
