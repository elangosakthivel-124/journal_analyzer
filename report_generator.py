from datetime import datetime

class ReportGenerator:
    def generate(self, text_data, image_data):
        mood = "Neutral"
        polarity = text_data["sentiment"]["polarity"]

        if polarity > 0.2:
            mood = "Positive"
        elif polarity < -0.2:
            mood = "Negative"

        return {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "mood": mood,
            "sentiment": text_data["sentiment"],
            "keywords": text_data["keywords"],
            "image_stats": image_data
        }
