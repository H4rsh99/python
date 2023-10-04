class Question:
    def __init__(self, question, options, correct_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer

    def is_correct(self, user_answer):
        return user_answer.lower() == self.correct_answer.lower()


class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0
        self.current_question_index = 0

    def add_question(self, question, options, correct_answer):
        self.questions.append(Question(question, options, correct_answer))

    def display_question(self):
        question = self.questions[self.current_question_index]
        print(f"\nQuestion {self.current_question_index + 1}: {question.question}\n")
        for i, option in enumerate(question.options, start=1):
            print(f"{i}. {option}")
        user_answer = input("Your answer (enter option number): ")
        return user_answer

    def start_game(self):
        print("Welcome to the Quiz Game!\n")
        for i in range(len(self.questions)):
            user_answer = self.display_question()
            if self.questions[self.current_question_index].is_correct(user_answer):
                print("Correct!\n")
                self.score += 1
           
