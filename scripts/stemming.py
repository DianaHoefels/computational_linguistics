# Install the NLTK library if you haven't already: bash pip install nltk

import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Make sure you have the necessary NLTK resources downloaded
nltk.download('punkt')

def stem_words(text):
    """
    Tokenizes the input text into words and applies stemming.

    Args:
        text (str): The input text string.

    Returns:
        list: A list of stemmed words.
    """
    # Initialize the Porter Stemmer
    stemmer = PorterStemmer()

    # Tokenize the text into words
    words = word_tokenize(text)

    # Stem each word in the tokenized text
    stemmed_words = [stemmer.stem(word) for word in words]

    return stemmed_words

if __name__ == "__main__":
    # Example usage
    sample_text = """Natural language processing includes tasks such as tokenization, stemming, and lemmatization. 
    It focuses on analyzing and understanding human languages."""
    
    stemmed_output = stem_words(sample_text)
    
    print("Stemmed Words:", stemmed_output)

# Output: Stemmed Words: ['natur', 'languag', 'process', 'includ', 'task', 'such', 'as', 'token', ',', 'stem', ',', 'and', 'lemmat', '.', 'it', 'focus', 'on', 'analyz', 'and', 'understand', 'human', 'languag', '.']
