import unittest

from SentimentAnalysis.sentiment_analysis import sentiment_analyzer


class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_positive(self):
        result = sentiment_analyzer("I love working with Python")
        self.assertEqual(result['label'], "SENT_POSITIVE")

    def test_sentiment_negative(self):
        result = sentiment_analyzer("I hate working with Python")
        self.assertEqual(result['label'], "SENT_NEGATIVE")

    def test_sentiment_neutral(self):
        result = sentiment_analyzer("I am neutral on Python")
        self.assertEqual(result['label'], "SENT_NEUTRAL")

if __name__ == '__main__':
    unittest.main() 
