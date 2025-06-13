"""
Simple demo script for the TextUtils library.
It runs some examples in Spanish to test the functions.
Uses Facade and Template Method design patterns.
"""

from abc import ABC
from text_utils_program import TextUtils


#Implementing Facade pattern to simplify the use of TextUtils functions.
"""Facade gives an easy way to use many text functions together."""
class TextUtilsFacade:
    """Simple interface to use TextUtils functions."""

    @staticmethod
    def analyze_text(text: str) -> dict:
        """
        Use different functions from TextUtils to analyze the text.
        Returns a dictionary with results.
        """
        return {
            "text": text,
            "word_count": TextUtils.count_words(text),
            "character_count": TextUtils.count_characters(text),
            "reversed_text": TextUtils.reverse_text(text),
            "without_punctuation": TextUtils.remove_punctuation(text),
            "is_palindrome": TextUtils.is_palindrome(text),
        }


#Usign Template Method pattern to define a clear process for text analysis.
"""Template Method is used to define a clear process to analyze the text"""

class TextProcessor(ABC):
    """Base class to analyze text step by step."""

    def __init__(self, text):
        self.text = text

    def process(self):
        """
        This method runs the full process:
        1. Show the original text
        2. Analyze it
        3. Show the results
        """
        self.display_header()
        result = TextUtilsFacade.analyze_text(self.text)
        self.display_result(result)
        self.display_footer()

    def display_header(self):
        """Print the original text."""
        print(f"Text: {self.text}")

    def display_result(self, result: dict):
        """Print the results of the analysis."""
        print(f"Word count: {result['word_count']}")
        print(f"Character count: {result['character_count']}")
        print(f"Reversed text: {result['reversed_text']}")
        print(f"Without punctuation: {result['without_punctuation']}")
        print(f"Is palindrome?: {'Yes' if result['is_palindrome'] else 'No'}")

    def display_footer(self):
        """Print a line to separate each example."""
        print("-" * 30)


# Using the TextProcessor class to run examples.
def main():
    #Example 1
    txt1 = "Una rosa es una rosa"
    print("Example 1")
    TextProcessor(txt1).process()

    # Example 2
    txt2 = "Anita atina"
    print("Example 2")
    TextProcessor(txt2).process()

    #Example 3
    txt3 = "¿Cómo estás hoy?"
    print("Example 3")
    TextProcessor(txt3).process()


if __name__ == "__main__":
    main()
