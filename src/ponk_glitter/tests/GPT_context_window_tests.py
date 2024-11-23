import unittest

from lib.context_window import GPTContextWindow


class GPTContextWindowTests(unittest.TestCase):

    def setUp(self):
        self.tokenized_text = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.size = 5
        self.context_window = GPTContextWindow(self.tokenized_text, self.size)

    def test_iteration(self):
        expected = [[1, 2, 3, 4, 5],  # first window
                    [4, 5, 6, 7, 8],  # overlapping window
                    [6, 7, 8, 9, 10]]  # last window

        for i, window in enumerate(self.context_window):
            self.assertEqual(window, expected[i])

    def test_iteration_text_shorter_than_size(self):
        tokenized_text = [1, 2, 3]
        size = 5
        context_window = GPTContextWindow(tokenized_text, size)
        expected = [[1, 2, 3]]

        for i, window in enumerate(context_window):
            self.assertEqual(window, expected[i])

    def test_iteration_text_equal_to_size(self):
        tokenized_text = [1, 2, 3, 4, 5]
        size = 5
        context_window = GPTContextWindow(tokenized_text, size)
        expected = [[1, 2, 3, 4, 5]]

        for i, window in enumerate(context_window):
            self.assertEqual(window, expected[i])

    def test_len(self):
        self.assertEqual(3, len(self.context_window))
        self.assertEqual(1, len(GPTContextWindow([1, 2, 3], 5)))
        self.assertEqual(1, len(GPTContextWindow([1, 2, 3, 4, 5], 5)))
