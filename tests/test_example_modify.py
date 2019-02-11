# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
import textwrap

from .helpers import keys
from .helpers import create_example_fixture


example_app = create_example_fixture('examples/modify.py')


def test_modify_kwargs(example_app):
    example_app.expect(textwrap.dedent("""\
        ? What's your first name  """))
    example_app.writeline('Dave')
    example_app.expect(textwrap.dedent("""\
        ? What's your first name  Dave
        ? What's your favorite color (tab for options)"""), rstrip_chars='\n')
    # unable to get tab test working so enter color manually
    if True:
        example_app.write('Red')
    else:
        example_app.write(keys.TAB)
        example_app.write(keys.DOWN)
    example_app.write(keys.ENTER)
    example_app.expect(textwrap.dedent("""\
        ? What's your favorite color (tab for options)  Red
        ? Enter your age  (Y/n)"""))
    example_app.write('n')
    example_app.expect(textwrap.dedent("""\
        ? Enter your age  No
        {
            "favorite_color": "Red",
            "first_name": "Dave"
        }

        """))     


def test_modify_answers(example_app):
    example_app.expect(textwrap.dedent("""\
        ? What's your first name  """))
    example_app.writeline('John')
    example_app.expect(textwrap.dedent("""\
        ? What's your first name  John
        ? What's your favorite color (tab for options)"""), rstrip_chars='\n')
    example_app.write('Green')
    example_app.write(keys.ENTER)
    example_app.expect(textwrap.dedent("""\
        ? What's your favorite color (tab for options)  Green
        ? Enter your age  (Y/n)"""))
    example_app.write('y')
    example_app.expect(textwrap.dedent("""\
        ? Enter your age  Yes
        ? What's your age  """))
    example_app.write('20')
    example_app.write(keys.ENTER)
    example_app.expect(textwrap.dedent("""\
        ? What's your age  20
        {
            "age": "20",
            "favorite_color": "Green",
            "first_name": "John"
        }

        """))     
