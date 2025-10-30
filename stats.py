def count_book_words(file_contents: str):
    """Count the total words of a text book."""
    total_words = 0
    for word in file_contents.split():
        if word != "":
            total_words += 1
    return total_words
