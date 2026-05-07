def remove_duplicated_words(line: str) -> str:
    
   words = line.split()
   unique_words = []

   for word in words:
    if word not in unique_words:
        unique_words.append(word)

    return " ".join(unique_words)
