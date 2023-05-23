import unittest
from task1.functions1 import sentences_amount, not_declarative_sentences_amount, \
    average_sentence_length, average_word_length, n_grams


class Task1Tests(unittest.TestCase):
    def test_amount_of_non_declarative_sentence_1(self):
        test_input = "Abc. Abc?!! Abc... abc. ABC! Abc..."
        TEST = "Test 1"

        expected_amount_of_non_declarative_sentence = 2

        self.assertEqual(expected_amount_of_non_declarative_sentence,
                         not_declarative_sentences_amount(test_input),
                         f'incorrect non declarative sentences amount {TEST}')

    def test_average_length_of_word_1(self):
        test_input = "Abc. Abc?!! Abc... abc. ABC! Abc..."
        TEST = "Test 1"

        expected_average_length_of_word = 3

        self.assertEqual(expected_average_length_of_word, average_word_length(test_input),
                         f'incorrect average length of the word {TEST}')

    def test_amount_of_ngrams_1(self):
        test_input = "Abc. Abc?!! Abc... abc. ABC! Abc..."
        TEST = "Test 1"

        K = 10
        N = 2

        expected_K_NGrams = [('abc abc', 5)]

        self.assertEqual(expected_K_NGrams, n_grams(test_input, N, K),
                         f'incorrect average length of the word {TEST}')

    def test_amount_of_sentence_1(self):
        test_input = ""
        TEST = "Test 2"

        expected_amount_of_sentence = 0
        self.assertEqual(expected_amount_of_sentence, sentences_amount(test_input),
                         f'incorrect sentences amount {TEST}')

    def test_average_length_of_sentence_1(self):
        test_input = ""
        TEST = "Test 2"

        expected_average_length_of_sentence = 0

        self.assertEqual(expected_average_length_of_sentence, average_sentence_length(test_input),
                         f'incorrect average length of sentence {TEST}')

    def test_amount_of_non_declarative_sentence_2(self):
        test_input = ""
        TEST = "Test 2"

        expected_amount_of_non_declarative_sentence = 0

        self.assertEqual(expected_amount_of_non_declarative_sentence,
                         not_declarative_sentences_amount(test_input),
                         f'incorrect non declarative sentences amount {TEST}')

    def test_average_length_of_word_2(self):
        test_input = ""
        TEST = "Test 2"

        expected_average_length_of_word = 0

        self.assertEqual(expected_average_length_of_word, average_word_length(test_input),
                         f'incorrect average length of the word {TEST}')

    def test_amount_of_ngrams_2(self):
        test_input = ""
        TEST = "Test 2"

        K = 10
        N = 2

        expected_K_NGrams = []

        self.assertEqual(expected_K_NGrams, n_grams(test_input, N, K),
                         f'incorrect average length of the word {TEST}')

    def test_amount_of_sentence_3(self):
        test_input = "ABCd, \"And?! Abcvkdr...\" Aaaaaaaa? Abdc!!!"
        TEST = "Test 3"

        expected_amount_of_sentence = 3
        self.assertEqual(expected_amount_of_sentence, sentences_amount(test_input),
                         f'incorrect sentences amount {TEST}')

    def test_average_length_of_sentence_3(self):
        test_input = "ABCd, \"And?! Abcvkdr...\" Aaaaaaaa? Abdc!!!"
        TEST = "Test 3"

        expected_average_length_of_sentence = 9

        self.assertEqual(expected_average_length_of_sentence, average_sentence_length(test_input),
                         f'incorrect average length of sentence {TEST}')

    def test_average_length_of_word_3(self):
        test_input = "ABCd, \"And?! Abcvkdr...\" Aaaaaaaa? Abdc!!!"
        TEST = "Test 3"
        expected_average_length_of_word = 5

        self.assertEqual(expected_average_length_of_word, average_word_length(test_input),
                         f'incorrect average length of the word {TEST}')

