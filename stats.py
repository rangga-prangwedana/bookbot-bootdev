def count_book_words(file_contents: str):
    """Count the total words of a text book."""
    return len(file_contents.split())


def count_book_chars(file_contents: str):
    """Return a dictionary with total count of each characters in a book."""
    total_characters = {}
    # Not using split() means file_contents is a very long string.
    for char in file_contents: 
        if char.isalpha():
            lower = char.lower()
            if lower in total_characters:
                total_characters[lower] += 1
            else:
                total_characters[lower] = 1
    sorted_total_char = {key:value for key,value in sorted(total_characters.items(), key=lambda item: item[1], reverse=True)}

    return sorted_total_char
    
