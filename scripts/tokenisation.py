import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

# Install the NLTK library if you haven't already: pip install nltk
# Make sure you have the necessary NLTK resources downloaded
nltk.download('punkt')

def tokenize_text(text):
    """
    Tokenizes the input text into sentences and words.
    Args:text (str): The input text string.
    Returns: dict: A dictionary with two keys - 'sentences' and 'words'.
    """
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)
    
    # Tokenize the text into words
    words = word_tokenize(text)

    return {
        'sentences': sentences,
        'words': words
    }

if __name__ == "__main__":
    # Example usage
    sample_text = """Natural language processing (NLP) is a field of artificial intelligence. 
    It focuses on the interaction between computers and humans through language."""
    
    tokenized_output = tokenize_text(sample_text)
    
    print("Sentences:", tokenized_output['sentences'])
    print("Words:", tokenized_output['words'])

# Output:
  Sentences: ['Natural language processing (NLP) is a field of artificial intelligence.', 'It focuses on the interaction between computers and humans through language.']
  Words: ['Natural', 'language', 'processing', '(', 'NLP', ')', 'is', 'a', 'field', 'of', 'artificial', 'intelligence', '.', 'It', 'focuses', 'on', 'the', 'interaction', 'between', 'computers', 'and', 'humans', 'through', 'language', '.']


# How to Run:
# Run the script: python tokenization.py
