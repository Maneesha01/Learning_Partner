# Learning Partner

**A multi-agent AI system to help students revise study material efficiently and test their knowledge.**

---

## Problem Statement

Students often struggle to revise large amounts of study material efficiently or quickly check their understanding of a topic. Traditional studying can be time-consuming, and learners may not receive instant feedback on what they’ve understood correctly.

**Learning_Partner** addresses this by providing a tool that automatically summarizes content and generates quizzes, allowing learners to revise smarter, test their knowledge, and get immediate feedback.

---

## Why Agents?

Agents are ideal for this problem because multiple tasks need to work independently but collaboratively:

* Summarizing study content
* Generating quizzes
* Monitoring agent outputs and performance

By using agents, each task can run in parallel or be extended separately. This modular approach makes the system scalable, maintainable, and ready for future AI enhancements.

---

## What We Created

A multi-agent learning assistant with the following components:

> **Content Review Agent** – Summarizes documents or links to extract key concepts.

> **Quiz Generation Agent** – Creates multiple-choice or short-answer questions based on summaries.

> **Evaluation Engine** – Monitors and evaluates agent performance, ensuring summaries and quizzes meet quality criteria.

> **Observability Layer** – Logs activities and metrics for monitoring and debugging.

These agents work together to provide a seamless study and revision experience while ensuring the agents perform effectively.

---

## Architecture

```
          +----------------+
          |   User Input   |
          | (Document/Link)|
          +-------+--------+
                  |
                  v
      +------------------------+
      | Content Review Agent    |
      | - Summarizes content    |
      +-----------+------------+
                  |
                  v
      +------------------------+
      | Quiz Generation Agent   |
      | - Generates questions   |
      +-----------+------------+
                  |
                  v
      +------------------------+
      | Evaluation Engine       |
      | - Monitors agent output |
      +-----------+------------+
                  |
                  v
      +------------------------+
      | Observability Layer     |
      | - Logs & metrics        |
      +------------------------+
                  |
                  v
           +-------------------+
           | Agent Performance  |
           | Reports & Logs     |
           +-------------------+
```

---

## How It Works

1. The user inputs study material (document or link).
2. The Content Review Agent summarizes the content.
3. The Quiz Agent generates questions.
4. The **Evaluation Engine** checks the quality and correctness of agent outputs.
5. All activity is logged in the Observability Layer for monitoring.

---

## The Build

* **Language:** Python
* **Libraries:** Standard Python libraries (modular structure, logging, file handling)
* **Environment:** Virtual environment using `venv`
* **Configuration:** `.env` file for environment variables or API keys
* **Structure:** Modular folders (`agents/`, `evaluation/`, `observability/`) for clean separation of concerns

The project is lightweight, modular, and designed for future enhancements like AI integration and cloud deployment.

---

## If I Had More Time

* Integrate LLM/NLP models for intelligent summarization and concept extraction.
* Add a web-based UI for easier user interaction.
* Implement persistent storage (database) to track agent performance over time.
* Containerize the project with Docker and deploy it on Cloud.
