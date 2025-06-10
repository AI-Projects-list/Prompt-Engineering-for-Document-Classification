
def generate_prompt(document_text):
    return f"""You are a document classification assistant. Classify the following document into one of the categories: Finance, Legal, Health, Technology, Education.

Document:
"""
{document_text}
"""

Classification:
"""
