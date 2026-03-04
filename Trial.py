import random

def get_question():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["Paris", "Berlin", "Madrid", "Rome"],
            "answer": "Paris"
        },
        {
            "question": "Which planet is closest to the Sun?",
            "options": ["Mercury", "Venus", "Earth", "Mars"],
            "answer": "Mercury"
        },
        {
            "question": "Which is the largest ocean?",
            "options": ["Pacific", "Atlantic", "Indian", "Southern"],
            "answer": "Pacific"
        },
        {
            "question": "Which is the largest animal?",
            "options": ["Elephant", "Whale", "Lion", "Giraffe"],
            "answer": "Blue Whale"
        },
        {
            "question": "Which is the largest country in the world?",
            "options": ["Russia", "Canada", "USA", "China"],
            "answer": "Russia"
        }
    ]

    question = random.choice(questions)
    print(question["question"])
    for i, option in enumerate(question["options"]):
        print(f"{i + 1}. {option}")
    return question

def play_game():
    question = get_question()
    user_answer = input("Enter the number of your answer: ")
    user_answer = int(user_answer) - 1

    if question["options"][user_answer] == question["answer"]:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is {question['answer']}")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        play_game()

play_game()