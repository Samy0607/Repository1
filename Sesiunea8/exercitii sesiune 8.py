from sesiunea7.exercitii import FormaGeometrica, Patrat, Cerc
import unittest
import pytest

# 1.
class Test(unittest.TestCase):

    def test_patrat_latura(self):
        l = Patrat(6)
        self.assertEqual(l)

    def test_patrat_aria(self):
        p = Patrat(5)
        self.assertEqual(p.aria(), 5 * 5)

    def test_cerc_aria(self):
        c = Cerc(10)
        self.assertEqual(c.aria(), 3.14 * 10 ** 2)

# 2.
class TestPatrat(unittest. TestCase):
    def test_patrat_aria(self):
        p = Patrat(5)
        self.assertEqual(p.aria(), 5 * 5)

class TestCerc(unittest. TestCase):
    def test_cerc_aria(self):
        c = Cerc(10)
        self.assertEqual(c.aria(), 3.14 * 10 ** 2)

# 3.
class Test1(pytest.TestReport):

    def test_patrat_latura(self):
        l1 = Patrat(6)
        assert l1 == 6

    def test_patrat_aria(self):
        p1 = Patrat(5)
        assert p1.aria() == 5 * 5

    def test_aria_cerc(self):
        c1 = Cerc(10)
        assert c1.aria() == 3.14 * 10 ** 2


