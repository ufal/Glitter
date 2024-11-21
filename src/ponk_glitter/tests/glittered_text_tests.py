import unittest

from lib.glitter_common import GlitteredText, GlitteredToken


class TestGlitteredText(unittest.TestCase):

    def setUp(self):
        self.models = ["model1", "model2"]
        self.gt = GlitteredText(self.models)
        raw_tokens = reversed([(f"test_token{i}", 0.1 * i) for i in range(6)])
        self.tokens = [GlitteredToken(rt[0], raw_tokens) for rt in raw_tokens]
        for t in self.tokens:
            self.gt.append(t)

    def test_used_models_property(self):
        self.assertEqual(type(self.gt.used_models), list)
        self.assertEqual(self.gt.used_models, self.models)

    def test_content_property(self):
        self.assertEqual(type(self.gt.content), list)
        self.assertEqual(self.gt.content, self.tokens)

    def test_len(self):
        self.assertEqual(len(self.gt), len(self.tokens))

    def test_getitem(self):
        for i in range(len(self.tokens)):
            self.assertEqual(self.gt[i], self.tokens[i])

    def test_contains(self):
        for t in self.tokens:
            self.assertTrue(t in self.gt)

        self.assertFalse("not_in_tokens" in self.gt)

    def test_reversed(self):
        self.assertEqual(list(reversed(self.gt)), list(reversed(self.tokens)))

    def test_iter(self):
        self.assertEqual(list(iter(self.gt)), self.tokens)
