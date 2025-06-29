
# Prompt Engineering for Document Classification

This project demonstrates how to use prompt engineering techniques to classify documents into categories using OpenAI's GPT model (can be adapted to any LLM with similar APIs).

## Project Structure

- `app.py`: Main application file that handles classification.
- `prompts.py`: Contains prompt templates for different strategies.
- `examples/`: Sample documents to classify.
- `results/`: Output classifications.

## Setup Instructions

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install requirements:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
python app.py
```

## How It Works

- Reads document from `examples/sample_doc.txt`.
- Applies a few-shot prompt to instruct the LLM to classify the document.
- Saves the classification result in `results/classification.txt`.

## Example Categories

- Finance
- Legal
- Health
- Technology
- Education

## Sample Prompt Format

```
You are a document classification assistant. Classify the following document into one of the categories: Finance, Legal, Health, Technology, Education.

Document:
"""
{{DOCUMENT_TEXT}}
"""

Classification:
```

