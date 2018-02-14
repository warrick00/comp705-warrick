import unittest
class Lab4Test(unittest.TestCase):

    def test_squared(self):
        """
        Tests lab4.squared()
        """
        func = lab4.squared
        case1 = [1, 2, 3]
        expexted1 = [1, 4, 9]
        self.assertEqual(func(case1), expexted1)

    if __name__ == '__main__':
        try:
            import lab4
            print("lab4.py module found.Testing...")
        except ImportError:
            print("missing lab4.py module")
