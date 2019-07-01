# unittest
import unittest

def cap_text(text):
    return text.title()

class mytest(unittest.TestCase):
    def test_one_word(self):
        wrd = 'ganesha'
        result = cap_text(wrd)
        self.assertEqual(result, 'Ganesha')

    def test_multiple_words(self):
        wrds = 'ganesha is the pratham pujya'
        result = cap_text(wrds)
        self.assertEqual(result, 'Ganesha Is The Pratham Pujya')

if __name__ == '__main__':
    unittest.main()
