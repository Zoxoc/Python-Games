questions = [{"question": "1. What is the capital of India?",
              "options": ["A.Mumbai", "B.Delhi", "C.Hyderabad", "D.Bangalore"],
              "answer": "B"
              },
             {"question": "2. Who owns Google?",
              "options": ["A.Google Corp", "B.Sundar Pichai", "C.Alphabet Inc.", "D.BlackRock"],
              "answer": "C"
              },
             {"question": "3. How many IPL Trophies do RCB have?",
              "options": ["A. 1", "B. 0", "C. 2", "D. 5"],
              "answer": "B"},
             {"question": "4. Which is the largest ocean?",
              "options": ["A.Atlantic Ocean", "B.Indian Ocean", "C.Pacific Ocean", "D.Arctic Ocean"],
              "answer": "C"}
             ]


def run_quiz(questions):
    score = 0
    for n in questions:
        print(n["question"])
        for option in n["options"]:
            print(option)
        user_answer = input("Enter your answer [A,B,C,D]: ").upper()
        print("\n")
        if user_answer == n['answer']:
            score += 1
    print(f"Your Quiz Score is {score}/{len(questions)}")


run_quiz(questions)
