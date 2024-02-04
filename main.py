from utils import get_random_question


class Question:
    def __init__(self, question, difficulty, answer):
        self.question = question
        self.difficulty = difficulty
        self.answer = answer

    def get_points(self):
        return int(self.difficulty) * 10

    def is_correct(self, user_answer):
        return user_answer == self.answer

    def build_question(self):
        print(f'Вопрос: {self.question}')
        print(f'Сложность: {self.difficulty}/5')

    def build_feedback(self, user_answer):
        if Question.is_correct(user_answer):
            print(f'Ответ верный, получено {Question.get_points} баллов')
            return 0
        else:
            print(f'Ответ неверный. Верный ответ – {self.answer}')
            return 1


def main():
    right_answers = 0
    points = 0
    user_input = int(input('Привет. На сколько вопросов ты хочешь попробовать ответить? '))
    for i in range(user_input):
        dict = get_random_question()
        question = Question(dict['q'], dict['d'], dict['a'])

        question.build_question()
        if question.build_feedback(input()):
            points += question.get_points()
            right_answers += 1
    print(f'''
    Вот и всё!
    Отвечено {right_answers} вопроса из {user_input}
    Набрано баллов: {points}
    ''')


if __name__ == "__main__":
    main()
