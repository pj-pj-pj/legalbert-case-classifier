import re, pandas as pd
from src.loader import tokenizer

MODEL_PATH = "../models/legalbert_model_20260125_145604"

# cleaning function
def clean_legal_text(text, label=None):
    """
    Legal text cleaning function.
    For legal_fees class, we keep numbers intact.
    """
    if not isinstance(text, str):
        return ""

    # 1. Handle line breaks and tabs
    text = text.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')

    # 2. Remove dates
    date_patterns = [
        r'\b\d{1,2}[-/]\d{1,2}[-/]\d{2,4}\b',  # DD-MM-YYYY
        r'\b\d{4}[-/]\d{1,2}[-/]\d{1,2}\b',    # YYYY-MM-DD
        r'\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \d{1,2},? \d{4}\b',
    ]
    for pattern in date_patterns:
        text = re.sub(pattern, '[DATE]', text, flags=re.IGNORECASE)

    # 3. Preserve legal punctuation but remove excessive special chars
    text = re.sub(r'[^\w\s.,;:?!()\-\[\]{}"\'§¶@#$%&*+=<>]', ' ', text)

    # 4. Normalize whitespace
    text = re.sub(r'\s+', ' ', text).strip()

    # 5. Remove numbers for non-legal_fees
    if label != "legal_fees":
        text = ' '.join(re.findall(r"\d*[a-zA-Z][\w]*", text))

    return text

def load_cleaned_csv():
  return pd.read_csv("data/interim/cleaned.csv")
  

def tokenize_function(examples):
    return tokenizer(
        examples["cleaned_text"],
        truncation=True,
        padding="max_length",
        max_length=512
    )
    