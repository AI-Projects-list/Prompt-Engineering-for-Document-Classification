
from prompts import generate_prompt
import openai

openai.api_key = "your-api-key"

def classify_document(document_text):
    prompt = generate_prompt(document_text)
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=10,
        temperature=0
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    with open("examples/sample_doc.txt", "r") as file:
        doc = file.read()

    category = classify_document(doc)
    with open("results/classification.txt", "w") as out_file:
        out_file.write(f"Classification: {category}")
    print("Classification completed. Check results/classification.txt")
