"""Small text helpers."""
import re


def word_count(text: str) -> int:
    """Count the words in text."""
    return len(re.findall(r"[A-Za-z0-9]+", text))


def title_case(text: str) -> str:
    """Capitalise the first letter of every word."""
    return re.sub(r"[A-Za-z]+", lambda m: m.group(0).capitalize(), text)
