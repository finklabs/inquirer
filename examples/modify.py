# -*- coding: utf-8 -*-
"""
* Modify kwargs and answers example
* run example by writing `python example/modify.py` in your console
"""
from __future__ import print_function, unicode_literals
from prompt_toolkit.contrib.completers import WordCompleter
from whaaaaat import style_from_dict, Token, prompt, print_json


style = style_from_dict({
        Token.QuestionMark: '#FF9D00 bold',
        Token.Instruction: '',  # default
        Token.Answer: '#5F819D bold',
        Token.Question: '',
    })


def suggest_colors(answers):
    colors = ['Green', 'White']
    if answers['first_name'] == 'Dave':
        colors = ['Red', 'Black']
    return {'completer': WordCompleter(colors)}


def enter_age(answers):
    if answers['enter_age'] is True:
        answers.update(prompt({
            'type': 'input',
            'name': 'age',
            'message': 'What\'s your age',
        }))
    answers.pop('enter_age', None)


questions = [
    {
        'type': 'input',
        'name': 'first_name',
        'message': 'What\'s your first name'
    },
    {
        'type': 'input',
        'name': 'favorite_color',
        'message': 'What\'s your favorite color (tab for options)',
        'modifyKwargs': suggest_colors
    },
    {
        'type': 'confirm',
        'name': 'enter_age',
        'message': 'Enter your age',
        'modifyAnswers': enter_age
    }
]

answers = prompt(questions, style=style)
print_json(answers)
