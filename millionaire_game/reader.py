from question import Question
import json


class Reader(Question):
    def __init__(self, question, options, correct_answer):
        super().__init__(question, options, correct_answer)

    def read_from_file(file_path):
        with open(file_path, 'r') as json_file:
            questions = json.load(json_file)
        return questions

    def print_from_file(questions):
        for question in questions:
            print(question)

    def convert_from_data(questions_data):
        question_list = [Question(data['question'], data['options'], data['correct_answer']) for data in questions_data]
        return question_list
