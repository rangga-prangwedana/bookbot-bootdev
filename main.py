from stats import count_book_words


def get_book_text(filepath: str = "books/frankenstein.txt"):
    """Read the content of a text book."""
    with open(filepath, encoding="utf-8") as f:
        file_contents = f.read()
    return file_contents
        

def main():
    book_contents = get_book_text("books/frankenstein.txt")
    total_words = count_book_words(book_contents)
    print(f"Found {total_words} total words.")


if __name__ == "__main__":
    main()
