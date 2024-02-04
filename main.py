from utils import get_random_question
from question import *


def main():
    points = 0
    right_answers = 0
    user_input = int(input('Привет. На сколько вопросов ты хочешь попробовать ответить? '))

    for i in range(user_input):
        dict = get_random_question()
        question = Question(dict['q'], dict['d'], dict['a'])

        question.build_question()
        question.user_answer = input()
        if question.is_correct(question.user_answer):
            right_answers += 1
            points += question.score
        print(question.build_feedback())
    print(f'Вот и всё!\n'
    f'Отвечено {right_answers} вопроса из {user_input}\n'
    f'Набрано баллов: {points}')


if __name__ == "__main__":
    main()
