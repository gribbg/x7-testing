# Originally auto-generated on 2020-12-16-18:25:48 -0500 EST
# By '--verbose --verbose gg.devtools.testing.extended'

from unittest import TestCase
from gg.devtools.testing.annotations import tests
from gg.devtools.testing import extended
from gg.devtools.testing.extended import ExtendedMatcherImage
from gg.devtools.testing.support import PicklerExtensionImage


@tests(extended.ExtendedMatcher)
class TestExtendedMatcher(TestCase):
    @tests(extended.ExtendedMatcher.__init__)
    def test___init__(self):
        # __init__(self, test_case: 'TestCaseExtended', type: Type)
        pass  # TODO-impl gg.devtools.testing.extended.ExtendedMatcher.__init__ test

    @tests(extended.ExtendedMatcher.almost_equal)
    def test_almost_equal(self):
        # almost_equal(self, first, second, places=None, delta=None) -> Union[bool, str]
        pass  # TODO-impl gg.devtools.testing.extended.ExtendedMatcher.almost_equal test

    @tests(extended.ExtendedMatcher.explain_mismatch)
    def test_explain_mismatch(self):
        # explain_mismatch(self, new_data, old_data) -> Tuple[bool, Union[str, NoneType]]
        pass  # TODO-impl gg.devtools.testing.extended.ExtendedMatcher.explain_mismatch test


@tests(extended.ExtendedMatcherImage)
class TestExtendedMatcherImage(TestCase):
    @tests(extended.ExtendedMatcherImage.__init__)
    def test___init__(self):
        # __init__(self, test_case: 'TestCaseExtended')
        pass  # TODO-impl gg.devtools.testing.extended.ExtendedMatcherImage.__init__ test

    @tests(extended.ExtendedMatcherImage.explain_mismatch)
    def test_explain_mismatch(self):
        # explain_mismatch(self, new_data, old_data) -> Tuple[bool, Union[str, NoneType]]
        pass  # TODO-impl gg.devtools.testing.extended.ExtendedMatcherImage.explain_mismatch test

    @tests(extended.ExtendedMatcherImage.show_images)
    def test_show_images(self):
        # show_images(self, new_data, old_data)
        pass  # TODO-impl gg.devtools.testing.extended.ExtendedMatcherImage.show_images test


@tests(extended.TestCaseExtended)
class TestTestCaseExtended(extended.TestCaseExtended):
    PICKLERS = [PicklerExtensionImage]
    MATCHERS = [ExtendedMatcherImage]
    SAVE_MATCH = not True

    @tests(extended.TestCaseExtended.almostEqual)
    @tests(extended.TestCaseExtended.almostEqualFloat)
    def test_almostEqual(self):
        # almostEqual(self, first: Any, second: Any, places: int = None, msg: Any = None, delta: float = None)
        self.assertEqual(True, self.almostEqual(1, 1))
        self.assertEqual(True, self.almostEqual(1, 1.000000001))
        self.assertEqual('1~=~1.0000001: 1 != 1.0000001 within 7 places (1e-07 difference)',
                         self.almostEqual(1, 1.0000001))
        self.assertEqual(True, self.almostEqual(1, 1.7, delta=0.7))
        self.assertEqual('1~=~1.8: 1 != 1.8 within 0.7 delta (0.8 difference)',
                         self.almostEqual(1, 1.8, delta=0.7))
        with self.assertRaises(TypeError):
            self.almostEqual(1, 2, places=3, delta=4)
        self.assertEqual(True, self.almostEqual([1, 2, 3], [1.001, 2.002, 3.003], places=2))
        self.assertEqual(True, self.almostEqual([1, 2, 3], [1.001, 2.002, 3.003], delta=0.004))
        self.assertEqual('[1, 2, 3]~=~[1.001, 2.002, 3.003]@ [1]: 2 != 2.002 within 0.001 delta (0.0019999999999997797 difference)',
                         self.almostEqual([1, 2, 3], [1.001, 2.002, 3.003], delta=0.001))
        self.assertEqual('[1, 2, 3]~=~[1.001, 2.002, 3.003]@ [0]: 1 != 1.001 within 3 places (0.001 difference)',
                         self.almostEqual([1, 2, 3], [1.001, 2.002, 3.003], places=3))
        self.assertEqual(True, self.almostEqual({3}, {3}))
        self.assertEqual("{3}~=~{3.01}: almostEqual: don't understand type: set", self.almostEqual({3}, {3.01}))

    @tests(extended.TestCaseExtended.assertAlmostEqual)
    def test_assertAlmostEqual(self):
        # assertAlmostEqual(self, first: Any, second: Any, places: int = None, msg: Any = None, delta: float = None) -> None
        pass  # TODO-impl gg.devtools.testing.extended.TestCaseExtended.assertAlmostEqual test

    @tests(extended.TestCaseExtended.assertAlmostMatch)
    def test_assertAlmostMatch(self):
        # assertAlmostMatch(self, new_data, case='0', func=None, cls=None)
        pass  # TODO-impl gg.devtools.testing.extended.TestCaseExtended.assertAlmostMatch test

    @tests(extended.TestCaseExtended.assertMatch)
    def test_assertMatch(self):
        # assertMatch(self, new_data, case='0', func=None, cls=None)
        pass  # TODO-impl gg.devtools.testing.extended.TestCaseExtended.assertMatch test

    @tests(extended.TestCaseExtended.match)
    def test_match(self):
        # match(self, new_data, case='0', func=None, cls=None, matcher: Union[Callable[[Any, Any], Any], NoneType] = None)
        pass  # TODO-impl gg.devtools.testing.extended.TestCaseExtended.match test

    @tests(extended.TestCaseExtended.matchExact)
    def test_matchExact(self):
        # matchExact(self, new_data, old_data) -> Union[bool, str]
        pass  # TODO-impl gg.devtools.testing.extended.TestCaseExtended.matchExact test

    def test_something(self):
        for tag in 'abc':
            with self.subTest(tag):
                output = 'Example: %s' % tag
                if tag == 'c':
                    # noinspection PyPackageRequirements
                    from PIL import Image
                    output = Image.new('1', (2, 2), 'black')
                self.assertMatch(output, tag)


@tests(extended)
class TestModExtended(TestCase):
    """Tests for stand-alone functions in gg.devtools.testing.extended module"""
