import unittest
from itertools import zip_longest

from lib.context_window import GPTContextWindow


class GPTContextWindowTests(unittest.TestCase):

    def test_iteration_size_4(self):
        tokenized_text = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        size = 4
        context_window = GPTContextWindow(tokenized_text, size)
        expected = [
            (4, [1, 2, 3, 4]),  # first window
            (2, [3, 4, 5, 6]),  # overlapping window
            (2, [5, 6, 7, 8]),
            (1, [6, 7, 8, 9])  # last window
        ]

        for i, window in zip_longest(range(len(expected)), context_window):
            self.assertEqual(expected[i], window)

    def test_iteration_size_5(self):
        tokenized_text = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        size = 5
        context_window = GPTContextWindow(tokenized_text, size)
        expected = [
            (5, [1, 2, 3, 4, 5]),  # first window
            (2, [3, 4, 5, 6, 7]),  # overlapping window
            (2, [5, 6, 7, 8, 9])  # last window
        ]

        for i, window in zip_longest(range(len(expected)), context_window):
            self.assertEqual(expected[i], window)

    def test_iteration_text_shorter_than_size(self):
        tokenized_text = [1, 2, 3]
        size = 5
        context_window = GPTContextWindow(tokenized_text, size)
        expected = [(3, [1, 2, 3])]

        for i, window in enumerate(context_window):
            self.assertEqual(window, expected[i])

    def test_iteration_text_equal_to_size(self):
        tokenized_text = [1, 2, 3, 4, 5]
        size = 5
        context_window = GPTContextWindow(tokenized_text, size)
        expected = [(5, [1, 2, 3, 4, 5])]

        for i, window in enumerate(context_window):
            self.assertEqual(window, expected[i])

    def test_len(self):
        self.assertEqual(4, len(GPTContextWindow([1, 2, 3, 4, 5, 6, 7, 8, 9], 4)))
        self.assertEqual(3, len(GPTContextWindow([1, 2, 3, 4, 5, 6, 7, 8, 9], 5)))
        self.assertEqual(1, len(GPTContextWindow([1, 2, 3], 5)))
        self.assertEqual(1, len(GPTContextWindow([1, 2, 3, 4, 5], 5)))
