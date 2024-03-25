import time
import random
class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

def display_welcome():
    print('Welcome to the Python Quiz!')
def display_question(question):
    print(question.text)

def get_user_answer():
    answer = input('Enter your answer: ')
    return int(answer)

def check_answer(question, user_answer):
    if user_answer == question.answer:
        print('Correct!')
    else:
        print('Incorrect!')

def display_score(score):
    print(f'Your score is {score} out of {len(questions)}')

def main():
    display_welcome()
    score = 0
    timer_per_question = 30
    elapsed_time = 0
    remaining_time = timer_per_question
    questions = [
        Question('What is 2 + 2?', 4),
        Question('What is 3 x 3?', 9),
        Question('What is 5 - 2?', 3),
        Question('What is 7 + 1?', 8),
        Question('What is 6 x 2?', 12),
    ]

    random.shuffle(questions)

    for question in questions:
        display_question(question)
        start_time = time.time()
        user_answer = get_user_answer()
        elapsed_time = time.time() - start_time

        remaining_time = timer_per_question - elapsed_time
        if remaining_time > 0:
            time.sleep(remaining_time)

        check_answer(question, user_answer)
        if user_answer == question.answer:
            score += 1

    display_score(score)

if __name__ == '__main__':
    main()
