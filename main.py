from stats import count_book_words, count_book_chars


def get_book_text(filepath: str = "books/frankenstein.txt"):
    """Read the content of a text book."""
    with open(filepath, encoding="utf-8") as f:
        file_contents = f.read()
    return file_contents
        

def main():
    book_path = "books/frankenstein.txt"
    book_contents = get_book_text(book_path)
    total_words = count_book_words(book_contents)
    total_chars = count_book_chars(book_contents)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words.")
    print("--------- Character Count -------")

    for key, value in total_chars.items():
        print(f"{key}: {value}")

    print("============= END ===============")



if __name__ == "__main__":
    main()
