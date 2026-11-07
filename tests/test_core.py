from textkit import title_case, word_count


def test_word_count():
    assert word_count("hello there") == 2


def test_title_case():
    assert title_case("hello there") == "Hello There"
