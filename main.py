# import modules, objects, and dependencies
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


# create question bank of question objects
question_bank = []
for i in question_data:
    question_text = i['text']
    question_answer = i['answer']
    new_question = Question(question = question_text, answer = question_answer)
    question_bank.append(new_question)

# New quizbrain object
quiz = QuizBrain(question_bank)
quiz.next_question()

# while loop to keep running the quiz when there are questions
while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
