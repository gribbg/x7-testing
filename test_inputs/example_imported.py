"""
Just some things that get imported to confirm tests can be 'forcibly' generated for this class
"""


class ClassGotImported(object):
    def __init__(self, a):
        self.a = a

    def show(self):
        return str(self.a)


def func_got_imported():
    pass


def another_func_got_imported():
    pass
