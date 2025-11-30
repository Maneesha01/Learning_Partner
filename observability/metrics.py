class Metrics:
    """
    Tracks basic runtime metrics (e.g., number of quizzes generated).
    """

    def __init__(self):
        self.counter = 0

    def increment_quiz_count(self):
        self.counter += 1

    def get_quiz_count(self):
        return self.counter
