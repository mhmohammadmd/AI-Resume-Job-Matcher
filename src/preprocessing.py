import re

def clean_text(text):
    """Lowercase, remove special characters and extra spaces."""
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)  # keep letters only
    text = re.sub(r"\s+", " ", text)      # remove extra spaces
    return text.strip()
