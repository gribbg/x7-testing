# Originally auto-generated on 2019-09-16-16:32:52 -0400 Eastern Daylight Time
# By 'C:/Users/glenn/PycharmProjects/devtools/gg/devtools/maketests/__main__.py -v -f gg.devtools.maketests.types'

from unittest import TestCase
from gg.devtools.testing.annotations import tests
from gg.devtools.maketests import types


@tests('gg.devtools.maketests.types.MaketestsError')
class TestMaketestsError(TestCase):
    def test_simple(self):
        self.assertTrue('If it parsed, then it works')


@tests('gg.devtools.maketests.types')
class Test0types(TestCase):
    """Tests for stand-alone functions in gg.devtools.maketests.types module"""

    @tests('gg.devtools.maketests.types.is_namedtuple')
    def test_is_namedtuple(self):
        self.assertTrue(types.is_namedtuple(types.ParsedModule))
        self.assertFalse(types.is_namedtuple(Test0types))
