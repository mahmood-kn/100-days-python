"""Day 17 - OOP"""
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
# class User:
#     """Creating user
#     """
#     def __init__(self,user_id:str,username) -> None:
#         self.id=user_id
#         self.username=username
#         self.followers=0
#         self.following=0

#     def follow(self,user:"User"):
#         """follow a user"""
#         user.followers+=1
#         self.following+=1
        
        
# john=User('001','john')
# sara=User('002','sara')
# john.follow(sara)
# print(john.following)
# print(sara.followers)

# Day exercise
question_bank:list[Question]=[]
for q in question_data:
    question_bank.append(Question(q["text"],q["answer"]))

quiz=QuizBrain(question_bank)
print(quiz.still_has_questions())
while quiz.still_has_questions():
    quiz.next_question()
    
print("You've completed the quiz")
print(f"Your final score was {quiz.score}/{len(question_bank)}")