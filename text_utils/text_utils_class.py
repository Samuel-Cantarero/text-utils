#Import necessary libraries
import re

# Create a class for text utilities
class Text_Utils:

# Define method to count words
    @staticmethod
    def count_words(text):
        """Count the number of words in the given text."""
        words = text.split()
        return len(words)

# Define method to count characters
    @staticmethod
    def count_characters(text):
        """Count the number of characters in the given text."""
        return len(text)

#Define method to reverse text
    @staticmethod
    def reverse_text(text):
        """Return the text reversed."""
        return text[::-1]
    
#Define method to remove punctuation
    @staticmethod
    def remove_punctuation(text):
        """Remove all punctuation characters from the text using regular expressions."""
        # Replace any character that is not a word character or whitespace
        return re.sub(r"[^\w\s]", "", text)

# Define method to check if text is a palindrome
    @staticmethod
    def is_palindrome(text):
        """Check if the text is a palindrome, ignoring punctuation, whitespace, and case."""
        cleaned = Text_Utils.remove_punctuation(text).replace(" ", "").lower()
        return cleaned == cleaned[::-1]

__all__ = ['Text_Utils']