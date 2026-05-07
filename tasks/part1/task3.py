from typing import Iterable

def build_from_unique_words(*lines: Iterable[str], word_number: int) -> str:
    result = []

    for line in lines:
        words = line.split()

    unique_words = []
    seen = set()

    for word in words:
        if word not in seen:
            seen.add(word)
            unique_words.append(word)

    if 0 <= word_number < len(unique_words):
        result.append(unique_words[word_number])

    return " ".join(result)