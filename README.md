# Text Utils

A Python library providing various text processing utilities following best programming practices.

## Installation

```bash
pip install text_utils
```

## Features

* **Word Counting**
  Count the number of words in a given text.
* **Character Counting**
  Count the total number of characters in a text.
* **Text Reversal**
  Reverse the order of characters in a text string.
* **Punctuation Removal**
  Remove all punctuation characters using regular expressions.
* **Palindrome Check**
  Determine if a text is a palindrome, ignoring punctuation, whitespace, and letter casing.

## Project Structure

```
text_utils/
├── setup.py
├── requirements.txt
├── README.md
├── text_utils_program/
│   ├── __init__.py
│   └── text_utils_class.py
├── test/
│   ├── __init__.py
│   └── text_utils_tests.py
└── scripts/
    └── main.py
```

## Demo Script

"""
Demo script for the TextUtils library.
You can run the demo directly from the root of the project with.
"""
```bash
python scripts/main.py
```

## Development

1. Clone the repository:

   ```bash
   git clone https://github.com/Samuel-Cantarero/text_utils.git
   ```
2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install development dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Install the package in editable mode:

   ```bash
   pip install -e .
   ```

## Running Tests

```bash
python -m unittest test/text_utils_tests.py
```

## Best Practices Implemented

1. **Object-Oriented Design**: Encapsulates functionality within a utility class.
2. **Modularity**: Separates different concerns into distinct methods.
3. **Documentation**: Comprehensive docstrings for all public methods.
4. **Testing**: Unit tests covering all core functions.
5. **Error Handling**: Utilizes regular expressions to robustly process text.
6. **Clean Code**: Descriptive naming and clear code structure.


