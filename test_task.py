import unittest

from numpy.testing import assert_allclose

from task import Task


class TestTask(unittest.TestCase):
    def test_resolution(self):
        t = Task()

        # On remplace les majuscules par des minuscules :
        assert_allclose(t.a @ t.x, t.b)


if __name__ == "__main__":
    unittest.main()
