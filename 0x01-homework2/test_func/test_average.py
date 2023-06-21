import average
import unittest


class averageTest(unittest.TestCase):
    def test_average():
        average()

    def test_average(self):
        assert average.average(average.mean) == 42




if __name__=="__main__":
    unittest()
