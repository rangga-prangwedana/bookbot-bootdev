def count_book_words(file_contents: str):
    """Count the total words of a text book."""
    return len(file_contents.split())


def count_book_chars(file_contents: str):
    """Return a dictionary with total count of each characters in a book."""
    total_characters = {}
    for word in file_contents.split():
        for char in word:
            if not char == " ":
                if char.lower() not in total_characters:
                    total_characters[char.lower()] = 1
                else:
                    total_characters[char.lower()] += 1
    return total_characters
    
