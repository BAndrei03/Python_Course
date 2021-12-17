class QuizBrain():

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
        #     return True
        # else:
        #     return False

    def next_question(self):
        curret_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(print(f"Q. {self.question_number}. {curret_question.text} (True/False): "))
        self.check_answer(user_answer, curret_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You are right!")
            self.score += 1

        else:
            print("You are wrong!")
        print(f"Yhe correct answer was: {correct_answer}.")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")
