import os
import json
import random


def load_questions():
    '''
    Возвращает данные файла questions.json в виде списка словарей.
    '''
    with open(os.path.join('questions.json')) as file:
        return json.load(file)


def get_random_question():
    '''
    Возвращает рандомный словарь из questions.json
    '''
    lst = load_questions()
    return lst[random.randint(0, 4)]