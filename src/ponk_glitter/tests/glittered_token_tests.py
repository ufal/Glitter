import unittest

from lib.glitter_common import GlitteredToken


class TestGlitteredToken(unittest.TestCase):

    def setUp(self):
        self.top_k_tokens = [("test_token1", 0.5),
                             ("test_token2", 0.4),
                             ("test_original_token", 0.3),
                             ("test_token3", 0.2)]
        self.original_token = "test_original_token"
        self.token = GlitteredToken(self.original_token, self.top_k_tokens)

    def test_original_token_property(self):
        self.assertEqual(type(self.token.original_token), str)
        self.assertEqual(self.token.original_token, self.original_token)

    def test_probability_property(self):
        self.assertEqual(type(self.token.probability), float)
        self.assertEqual(self.token.probability, 0.3)

    def test_nth_property(self):
        self.assertEqual(type(self.token.nth), int)
        self.assertEqual(self.token.nth, 3)

    def test_vocab_size_property(self):
        self.assertEqual(type(self.token.vocab_size), int)
        self.assertEqual(self.token.vocab_size, 4)
