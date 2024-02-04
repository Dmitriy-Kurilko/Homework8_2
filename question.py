class Question:
    def __init__(self, ask, difficulty, answer):
        self.ask = ask
        self.difficulty = difficulty
        self.answer = answer

        self.user_answer = None
        self.score = int(self.difficulty) * 10

    def get_points(self):
        return self.score

    def is_correct(self, user_answer):
        return user_answer == self.answer

    def build_question(self):
        print(f'Вопрос: {self.ask}')
        print(f'Сложность: {self.difficulty}/5')

    def build_feedback(self):
        if self.is_correct(self.user_answer):
            return f'Ответ верный, получено {self.score} баллов'
        return f'Ответ неверный. Верный ответ – {self.answer}'