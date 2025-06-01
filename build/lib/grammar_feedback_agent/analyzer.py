from typing import List
from openai import AzureOpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Azure OpenAI client
api_key = os.getenv("AZURE_OPENAI_API_KEY")
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")

if not api_key or not endpoint:
    raise ValueError("Azure OpenAI credentials are missing or empty in the .env file.")

client = AzureOpenAI(
    api_key=api_key,
    api_version="2023-05-15",
    azure_endpoint=endpoint
)

def grammar_check(text: str) -> List[str]:
    """
    Analyzes the grammar of the input text using Azure OpenAI.

    Args:
        text (str): The text to analyze.

    Returns:
        List[str]: A list of grammar suggestions.
    """
    try:
        prompt = f"Analyze the grammar in the following text and provide suggestions for improvement:\n\n{text}"
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a grammar expert."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300
        )
        suggestions = response.choices[0].message.content.strip().split("\n")
        return [s.strip() for s in suggestions if s.strip()] or ["- No grammar issues found."]
    except Exception as e:
        return [f"- Error analyzing grammar: {str(e)}"]