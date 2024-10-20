import unittest
from main import affiche

class TestAffiche(unittest.TestCase):
    def test_affiche_sans_parametre(self):
        self.assertEqual(affiche(), "12Fizz4BuzzFizz78FizzBuzz11Fizz1314FrisBee...")

if __name__ == '__main__':
    unittest.main()
