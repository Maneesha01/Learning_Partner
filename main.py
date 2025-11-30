import os
from dotenv import load_dotenv

from agents.content_agent import ContentAgent
from agents.quiz_agent import QuizAgent
from evaluation.evaluator import Evaluator
from observability.logger import setup_logger
from observability.metrics import Metrics
from observability.tracer import Tracer


def main():
    # Load environment variables
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")

    logger = setup_logger()
    tracer = Tracer()
    metrics = Metrics()

    logger.info("Learning Partner started")
    
    # Initialize agents
    content_agent = ContentAgent(api_key)
    quiz_agent = QuizAgent(api_key)
    evaluator = Evaluator()

    # Get input
    text = input("Enter content or paste notes: ")

    tracer.trace("Starting summary generation")
    summary = content_agent.summarize(text)
    print("\n📘 Summary:")
    print(summary)

    tracer.trace("Generating quiz questions")
    quiz_questions = quiz_agent.generate_quiz(text)
    metrics.increment_quiz_count()

    print("\n📝 Quiz Questions:")
    for q in quiz_questions:
        print("-", q)

    logger.info("Quiz generated")
    print("\n📊 Total quizzes generated:", metrics.get_quiz_count())


if __name__ == "__main__":
    main()
