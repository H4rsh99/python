# India Quiz Game

# Define a list of questions, options, and correct answers
questions = [
    {
        "question": "What is the capital of India?",
        "options": ["New Delhi", "Mumbai", "Kolkata", "Chennai"],
        "correct_answer": "New Delhi"
    },
    {
        "question": "Which river is known as the 'Ganga' in India?",
        "options": ["Yamuna", "Brahmaputra", "Indus", "Ganges"],
        "correct_answer": "Ganges"
    },
    {
        "question": "What is the national animal of India?",
        "options": ["Lion", "Tiger", "Elephant", "Leopard"],
        "correct_answer": "Tiger"
    },
    {
        "question": "Which festival is known as the 'Festival of Lights' in India?",
        "options": ["Holi", "Diwali", "Eid", "Christmas"],
        "correct_answer": "Diwali"
    }
]

# Initialize the score
score = 0

# Welcome message
print("Welcome to the India Quiz Game!")

# Loop through each question
for idx, question_data in enumerate(questions, start=1):
    print(f"\nQuestion {idx}: {question_data['question']}")
    print("Options:")
    
    # Display options
    for option_idx, option in enumerate(question_data['options'], start=1):
        print(f"{option_idx}. {option}")
    
    # Get user's answer
    user_answer = input("Your answer (enter option number): ")
    
    # Check if the answer is correct
    if user_answer.isdigit() and 1 <= int(user_answer) <= len(question_data['options']):
        selected_option = question_data['options'][int(user_answer) - 1]
        if selected_option == question_data['correct_answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {question_data['correct_answer']}")
    else:
        print("Invalid input. Skipping this question.")

# Display final score
print("\nQuiz completed!")
print(f"Your score: {score}/{len(questions)}")

# Provide feedback based on the score
if score == len(questions):
    print("Congratulations! You got a
