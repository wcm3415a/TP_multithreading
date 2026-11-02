import unittest

from numpy.testing import assert_allclose

from task import Task


class TestTask(unittest.TestCase):
    def test_resolution(self):
        t = Task()

        # On lance le calcul
        t.work()

        # On vérifie le résultat
        assert_allclose(t.a @ t.x, t.b)


if __name__ == "__main__":
    unittest.main()
