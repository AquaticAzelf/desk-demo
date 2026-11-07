"""Small text helpers."""
import re


def word_count(text: str) -> int:
    """Count the words in text."""
    return len(re.findall(r"[A-Za-z0-9]+", text))


def title_case(text: str) -> str:
    """Capitalise the first letter of every word."""
    return re.sub(r"[A-Za-z]+", lambda m: m.group(0).capitalize(), text)


def slugify(text):
    # This function converts the given text into a slug.
    # A slug is a URL-friendly version of a string.
    # First, we convert the text to lowercase.
    result = text.lower()
    # Next, we replace spaces with hyphens.
    result = result.replace(" ", "-")
    # Then, we remove any characters that are not alphanumeric or hyphens.
    final_result = ""
    for character in result:
        if character.isalnum() or character == "-":
            final_result = final_result + character
    # Finally, we return the final result.
    return final_result
