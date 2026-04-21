import os
import csv
import json


class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def check_file(self):
        exists = os.path.exists(self.filename)
        print(f"Checking file... Found: {exists}")
        return exists

    def create_output_folder(self, folder='output'):
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Folder {folder} created.")


class DataLoader:
    def __init__(self, filename):
        self.filename = filename
        self.students = []

    def load(self):
        with open(self.filename, mode='r', encoding='utf-8') as f:
            self.students = list(csv.DictReader(f))
        print(f"Loaded {len(self.students)} students.")
        return self.students

    def preview(self, n=5):
        print("Preview:")
        for row in self.students[:n]:
            print(f"{row['student_id']} | {row['country']} | GPA: {row['GPA']}")


class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):
        counts = {}
        for s in self.students:
            country = s['country']
            counts[country] = counts.get(country, 0) + 1

        sorted_c = sorted(counts.items(), key=lambda x: x[1], reverse=True)

        self.result = {
            "total_countries": len(counts),
            "top_3": sorted_c[:3]
        }

    def print_results(self):
        print(f"Total countries: {self.result['total_countries']}")
        print("Top 3:", self.result['top_3'])


class ResultSaver:
    def __init__(self, result, path):
        self.result = result
        self.path = path

    def save_json(self):
        with open(self.path, 'w') as f:
            json.dump(self.result, f, indent=4)
        print(f"Saved to {self.path}")


# MAIN LOGIC
fm = FileManager('students.csv')
if fm.check_file():
    fm.create_output_folder()

    dl = DataLoader('students.csv')
    dl.load()
    dl.preview()

    analyser = DataAnalyser(dl.students)
    analyser.analyse()
    analyser.print_results()

    saver = ResultSaver(analyser.result, 'output/result.json')
    saver.save_json()
else:
    print("Stop: File not found.")