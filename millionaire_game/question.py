import json


class Question:
    def __init__(self, question, options, correct_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer

    def check_answer(self, user_answer):
        return user_answer == self.correct_answer

    def __str__(self):
        return self._format_question_and_options()

    def _format_question_and_options(self):
        responses = ""
        for id, res in enumerate(self.options):
            responses += f'{id + 1}) - {res}\n'
        return f"{self.question}\n{responses}"


    # def read_from_file(file_path):
    #     with open(file_path, 'r') as json_file:
    #         questions = json.load(json_file)
    #     return questions
    #
    # def print_from_file(questions):
    #     for question in questions:
    #         print(question)
    # def convert_from_data(questions_data):
    #     question_list = [Question(data['question'], data['options'], data['correct_answer']) for data in questions_data]
    #     return question_list