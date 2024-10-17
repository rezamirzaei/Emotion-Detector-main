import unittest
from EmotionDetection.emotion_detection import emotion_detector, extract_emotion

class TestEmotionDetection(unittest.TestCase):

    def test_happy_statement(self):
        result = extract_emotion(emotion_detector("I am glad this happened"))
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_angry_statement(self):
        result = extract_emotion(emotion_detector("I am really mad about this"))
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_disgust_statement(self):
        result = extract_emotion(emotion_detector("I feel disgusted just hearing about this"))
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_sad_statement(self):
        result = extract_emotion(emotion_detector("I am so sad about this"))
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_fear_statement(self):
        result = extract_emotion(emotion_detector("I am really afraid that this will happen"))
        self.assertEqual(result['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()

