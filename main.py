from stats import get_num_words, get_characters, get_report_list
import sys 

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents    

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) 
    print("============ BOOKBOT ============")
    book_path = sys.argv[1] 
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    text = get_book_text(book_path)
    count_words = get_num_words(text)
    print(f"Found {count_words} total words")
    print("--------- Character Count -------")
    count_chars = get_characters(text)
    report = get_report_list(count_chars) 

    for item in report:
        print(f"{item['char']}: {item['num']}")
    
    print("============= END ===============")

main()
    
    