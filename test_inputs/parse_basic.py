"""Test input file for parse test_parse.py"""

import sys
from x7.lib import annotations
from x7.lib.annotations import tests
from test_inputs.example_imported import ClassGotImported, func_got_imported
from typing import NamedTuple

TEST_INCLUDE = ['ClassGotImported', 'func_got_imported']
TEST_EXCLUDE = ['excluded_function', 'ExcludedClass']

NamedTupleToIgnore = NamedTuple('NamedTupleToIgnore', ignore=int)


class ExcludedClass(object):
    pass


def excluded_function():
    pass


THIS_LINE_IS = 23


@tests(annotations)
class TestModExample(object):
    START_LINE = 26

    @tests(tests)
    def test_tests(self):
        return ClassGotImported, func_got_imported

    @tests('test_inputs.example_imported')
    def test_example_imported(self):
        pass

    END_LINE = 38


@tests(TestModExample)
class TestModExample2(object):
    START_LINE = 41

    @tests(TestModExample.test_tests)
    def test1(self):
        pass

    @tests(TestModExample.test_example_imported)
    def test2(self):
        pass

    END_LINE = 53


@tests(excluded_function)
def a_function(a, b):
    return a+b


a_function.START_LINE = 56
a_function.END_LINE = 58
