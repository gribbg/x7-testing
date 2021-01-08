# Auto-generated output for test_inputs.example.py, used by test_gen_code.py
# HEADER

from unittest import TestCase
from x7.lib.annotations import tests
from test_inputs import example
from test_inputs import example_imported


@tests(example.AClass)
class TestAClass(TestCase):
    @tests(example.AClass.__init__)
    def test___init__(self):
        # __init__(self, a, b)
        pass  # TO_DO-impl test_inputs.example.AClass.__init__ test

    @tests(example.AClass.__str__)
    def test___str__(self):
        # __str__(self)
        pass  # TO_DO-impl test_inputs.example.AClass.__str__ test

    @tests(example.AClass.add)
    def test_add(self):
        # add(self, c)
        pass  # TO_DO-impl test_inputs.example.AClass.add test


@tests(example.AClass.AClassSubclass)
class TestAClass0AClassSubclass(TestCase):
    @tests(example.AClass.AClassSubclass.nothing)
    def test_nothing(self):
        # nothing(self)
        pass  # TO_DO-impl test_inputs.example.AClass.AClassSubclass.nothing test


@tests(example_imported.ClassGotImported)
class TestClassGotImported(TestCase):
    @tests(example_imported.ClassGotImported.__init__)
    def test___init__(self):
        # __init__(self, a)
        pass  # TO_DO-impl test_inputs.example_imported.ClassGotImported.__init__ test

    @tests(example_imported.ClassGotImported.show)
    def test_show(self):
        # show(self)
        pass  # TO_DO-impl test_inputs.example_imported.ClassGotImported.show test
