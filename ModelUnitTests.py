import unittest
from model import Model

m = Model()

class ModelUnitTests(unittest.TestCase):

    #test errortext for multiple input letters
    def test_multipleLetterError(self):
        m.testLetter('hello')
        self.assertEqual(m.errortext, 'Please input a single character.')

    #test errortext for non english characters
    def test_nonEnglishError(self):
        m.testLetter('3')
        self.assertEqual(m.errortext, 'Please input an English letter.')

    #test errortext for nultiple non-english characters
    def test_multipleNonEnglishError(self):
        m.testLetter('333')
        self.assertEqual(m.errortext, 'Please input a single character.')

    #test errorext for a valid input (not case sensitive)
    def test_correctLetter(self):
        m.word = 'and'
        m.testLetter('A')
        self.assertIsNone(m.errortext)

    #test errortext for a repeated letter (not case sensitive)
    def test_repeatLetterError(self):
        m.word = 'and'
        m.testLetter('a')
        m.testLetter('A')
        self.assertEqual(m.errortext, 'Please guess a new letter.')

    #test indices list for correct guess
    def test_correctGuessIndices(self):
        m.word = 'test'
        m.testLetter('t')
        self.assertEqual(m.indices, [0,3])

    #test correctLetters list for correct guess
    def test_correctGuessLettersList(self):
        m.word = 'test'
        m.testLetter('t')
        self.assertEqual(m.correctLetters, ['t', 't'])

    #test wrongLetters list for an incorrect guess
    def test_incorrectLetters(self):
        m.wrongLetters = []
        m.word = 'friend'
        m.testLetter('o')
        self.assertEqual(m.wrongLetters, ['o'])

    #test gameState increments correctly
    def test_gameState(self):
        m.gameState = 0
        m.word = 'friend'
        m.testLetter('o')
        self.assertEqual(m.gameState, 1)

if __name__ == '__main__':
    unittest.main()
