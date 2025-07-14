import sys
import os

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    if not os.path.exists(book_path):
        print(f"Error: File {book_path} not found")
        sys.exit(1)
    
    from stats import get_num_words, count_letters, sort_letter_count
    letter_count = count_letters(get_book_text(book_path))
    #book_text = get_book_text(book_path)
    
    #print(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count -----------")
    print(f"Found {get_num_words(get_book_text(book_path))} total words")
    print("----------- Letter Count -----------")
    print(sort_letter_count(letter_count))
    print("============ END ============")

if __name__ == "__main__":
    main()