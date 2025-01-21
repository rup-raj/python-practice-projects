from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for questions in question_data:
    new_q = Question(questions["category"],questions["type"],questions["difficulty"],questions["question"],questions["correct_answer"])
    question_bank.append(new_q)

user1_quiz = QuizBrain(question_bank)

while user1_quiz.is_quiz_over():
    user1_quiz.next_question()

print("\n===========================")
print("You completed the quiz.")
print(f"Your final score is : {user1_quiz.score}/{len(question_bank)}")