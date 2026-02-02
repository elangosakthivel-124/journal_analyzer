import sqlite3
import json
from analyzer.text_analysis import TextAnalyzer
from analyzer.image_analysis import ImageAnalyzer
from analyzer.report_generator import ReportGenerator

DB_PATH = "database/journal.db"

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS journal (
                id INTEGER PRIMARY KEY,
                date TEXT,
                report TEXT
            )
        """)

def save_report(report: dict):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "INSERT INTO journal (date, report) VALUES (?, ?)",
            (report["date"], json.dumps(report))
        )

def run(text_entry: str, image_path: str):
    text_analyzer = TextAnalyzer()
    image_analyzer = ImageAnalyzer()
    report_generator = ReportGenerator()

    text_data = text_analyzer.analyze(text_entry)
    image_data = image_analyzer.analyze(image_path)

    report = report_generator.generate(text_data, image_data)
    save_report(report)

    print("\n📊 Daily Journal Analysis")
    print(json.dumps(report, indent=2))

if __name__ == "__main__":
    init_db()

    sample_text = """
    Today was productive. I felt focused and calm while working on my project.
    """

    sample_image = "storage/images/sample.jpg"
    run(sample_text, sample_image)
