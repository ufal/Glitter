import unittest

from lib.glitter_common import *


class TestNormalizeGlitteredTextWithSubwordTokens(unittest.TestCase):

    def setUp(self):
        self.raw_top_k_tokens = [("test_token1", 0.5),
                                 ("##test_token2", 0.4),
                                 ("test_token3", 0.3),
                                 ("test##_token4", 0.2)]
        self.top_k_tokens = [GlitteredToken(rt[0], self.raw_top_k_tokens) for rt in self.raw_top_k_tokens]
        self.models = ["model1"]
        self.gt = GlitteredText(self.models)


    def test(self):
        normalized_gt = normalize_glittered_text_with_subword_tokens(self.gt)
        normalized_text_str = str(normalized_gt)
        print(normalized_text_str)
        #self.assertEqual("test_token1test_token2 test_token3 test##_token4", normalized_text_str)

