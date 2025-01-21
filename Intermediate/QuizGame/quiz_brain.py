class QuizBrain:

    def __init__(self,question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def is_quiz_over(self):
        if self.question_number == len(self.question_list):
            return False
        else:
            return True

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("You got it right!")
            print(f"Correct answer was: {correct_answer}")
            return True
        else:
            print("Wrong Answer!")
            return False

    def next_question(self):
        question = self.question_list[self.question_number].question
        answer = self.question_list[self.question_number].correct_answer
        self.question_number += 1

        user_answer = input(f"Q.{self.question_number}: {question} (True/False)?")

        if self.check_answer(user_answer,answer):
            self.score += 1

        print(f"Your current score is: {self.score}/{self.question_number}")

