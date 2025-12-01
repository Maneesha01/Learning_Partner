Learning_Partner

Learning_Partner is a simple parallel multi-agent system designed to support students in understanding study material and testing their knowledge.
The project demonstrates how two independent agents can be orchestrated together, along with evaluation and observability components commonly used in real-world AI applications.

Overview

The system processes a piece of study material using two agents running in parallel:

Content Agent – Generates a concise summary and identifies key points.

Quiz Agent – Creates relevant practice questions based on the same input.

The outputs are combined to give the learner both an understanding of the material and a way to evaluate their knowledge.

Features

Parallel Multi-Agent Workflow
Two agents execute at the same time and return structured outputs.

Evaluation Module
Evaluates summary and quiz quality based on relevance, clarity, completeness, and accuracy.

Observability
Includes logging, metrics, and tracing to provide transparency and support debugging.

Secure API Handling
Uses a .env file to safely store API keys. A .env.example file shows required variables.

Project Structure
Learning_Partner/
├── agents/
│   ├── content_agent.py
│   └── quiz_agent.py
│
├── evaluation/
│   └── evaluator.py
│
├── observability/
│   ├── logger.py
│   ├── metrics.py
│   └── tracer.py
│
├── .env.example
├── .gitignore
├── requirements.txt
├── main.py
└── README.md


