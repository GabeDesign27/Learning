from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []

# access each value in data.py to build question bank, a bank of question objects.
for i in question_data:
    question_text = i["question"]
    question_answer = i["correct_answer"]
    question = Question(question_text, question_answer)
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"The quiz is complete.\nYour final score is {quiz.score}/{quiz.question_number}")
