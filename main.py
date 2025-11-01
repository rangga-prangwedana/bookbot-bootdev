import sys
from stats import count_book_words, count_book_chars


def get_book_text(filepath: str):
    """Read the content of a text book."""
    try:
        with open(filepath, encoding="utf-8") as f:
            file_contents = f.read()
        return file_contents
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: {filepath} was not found.")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred while reading '{filepath}': {e}") from e

        

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_file>")
        sys.exit(1)
    book_path = sys.argv[1]
    try:
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

    except FileNotFoundError as e:
        print(e)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)



if __name__ == "__main__":
    main()
