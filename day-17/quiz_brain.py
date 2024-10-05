class QuizBrain:
    def __init__(self,q_list) -> None:
        self.question_number=0
        self.question_list=q_list
        self.score=0
    
    def still_has_questions(self):
        return len(self.question_list) > self.question_number
    
    def next_question(self):
        current_question=self.question_list[self.question_number]
        self.question_number+=1
        choice=input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(choice,current_question.answer)
        
    def check_answer(self,choice,answer):
        if choice.lower()==answer.lower():
            self.score+=1
            print("You got it write")
        else:
            print("You got it wrong")
        print(f"The correct answer was: {answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")