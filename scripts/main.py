"""
Simple demo script for the TextUtils library.
Runs concrete examples in Spanish to verify functionality.
"""
from text_utils_program import TextUtils

# Example 1
txt1 = "Una rosa es una rosa"
print(f"Text: {txt1}")
print(f"Word count: {TextUtils.count_words(txt1)}")
print(f"Character count: {TextUtils.count_characters(txt1)}")
print(f"Reversed text: {TextUtils.reverse_text(txt1)}")
print(f"Without punctuation: {TextUtils.remove_punctuation(txt1)}")
print(f"Is palindrome?: {'Yes' if TextUtils.is_palindrome(txt1) else 'No'}")
print("-" * 30)

# Example 2 
txt2 = "Anita atina"
print(f"Text: {txt2}")
print(f"Word count: {TextUtils.count_words(txt2)}")
print(f"Character count: {TextUtils.count_characters(txt2)}")
print(f"Reversed text: {TextUtils.reverse_text(txt2)}")
print(f"Without punctuation: {TextUtils.remove_punctuation(txt2)}")
print(f"Is palindrome?: {'Yes' if TextUtils.is_palindrome(txt2) else 'No'}")
print("-" * 30)

# Example 3
txt3 = "¿Cómo estas hoy?"
print(f"Text: {txt3}")
print(f"Word count: {TextUtils.count_words(txt3)}")
print(f"Character count: {TextUtils.count_characters(txt3)}")
print(f"Reversed text: {TextUtils.reverse_text(txt3)}")
print(f"Without punctuation: {TextUtils.remove_punctuation(txt3)}")
print(f"Is palindrome?: {'Yes' if TextUtils.is_palindrome(txt3) else 'No'}")
print("-" * 30)
