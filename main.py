from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")


# class User:
#     def __init__(self, user_id, username):
#         self.id = user_id
#         self.name = username
#         self.followers = 0
#         self.following = 0
#
#     def follow(self, user):
#         user.followers += 1
#         self.following += 1
#
#
# user_1 = User("001", "Chewbacca")
# print(user_1.id, user_1.name)
#
# user_2 = User("002", "Darth Vader")
# print(user_2.id, user_2.name)
#
# user_1.follow(user_2)
# print(f"user 1 has {user_1.followers} followers")
# print(user_1.following)
# print(f"user 2 has {user_2.followers} followers")
# print(user_2.following)
