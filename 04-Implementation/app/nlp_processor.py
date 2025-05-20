"""NLP processing for chatbot."""
import nltk
from nltk.tokenize import word_tokenize

SLANG_MAP = {
    'hw': 'homework',
    'lect': 'lecture'
}

def process_query(text):
    tokens = word_tokenize(text.lower())
    processed = [SLANG_MAP.get(token, token) for token in tokens]
    return ' '.join(processed)