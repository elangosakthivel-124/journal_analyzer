from textblob import TextBlob
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download("punkt", quiet=True)
nltk.download("stopwords", quiet=True)

STOPWORDS = set(stopwords.words("english"))

class TextAnalyzer:
    def analyze(self, text: str) -> dict:
        blob = TextBlob(text)

        sentiment = {
            "polarity": round(blob.sentiment.polarity, 3),
            "subjectivity": round(blob.sentiment.subjectivity, 3)
        }

        tokens = word_tokenize(text.lower())
        keywords = [
            w for w in tokens
            if w.isalpha() and w not in STOPWORDS
        ]

        return {
            "sentiment": sentiment,
            "keywords": list(set(keywords))
        }
