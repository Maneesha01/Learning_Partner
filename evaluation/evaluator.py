class Evaluator:
    """
    Evaluates the student's answers or assesses quiz quality.
    """

    def evaluate_answer(self, correct_answer: str, user_answer: str) -> bool:
        return correct_answer.lower().strip() == user_answer.lower().strip()

    def evaluate_quiz_quality(self, questions: list) -> str:
        if len(questions) < 3:
            return "Low quality quiz – too few questions"
        return "Quiz quality looks good"
