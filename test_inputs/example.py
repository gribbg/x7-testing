""""
Example file for testing maketests
"""

from .example_imported import ClassGotImported, func_got_imported, another_func_got_imported

TEST_EXCLUDE = ['AClassToExclude']
TEST_INCLUDE = ['ClassGotImported', 'func_got_imported']
TEST_INCLUDE += ['another_func_got_imported']
SOMETHING = False       # set to True to include Something() class


def a_function(with_arg):
    # Silliness to make these items appear 'used'
    return [ClassGotImported, func_got_imported, another_func_got_imported, with_arg]


class AClassToExclude(object):
    """A class to exclude from testing via TEST_EXCLUDE"""
    pass


class AClass(object):
    class AClassSubclass(object):
        def nothing(self):
            pass

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self, c):
        return self.a + self.b + c

    if SOMETHING:
        def other(self):
            return self == self

        def yet_one_more(self):
            return self != self

    def __str__(self):
        return 'AClass(%s, %s)' % (self.a, self.b)


if False and SOMETHING:
    class Something(object):
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def swap(self):
            self.x, self.y = self.y, self.x

        def format(self):
            return '(%r, %r)' % (self.x, self.y)


    def some_function():
        pass


if __name__ == '__main__':
    ac = AClass(a_function(1), 2)
    print(ac, ac.add(3))
