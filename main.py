from stats import get_num_words, get_characters

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents    

def main():
    book_path = "books/frankenstein.txt" 
    text = get_book_text(book_path)
    count_words = get_num_words(text)
    count_chars = get_characters(text) 
    print(f"Found {count_words} total words")
    print(count_chars)

main()
    
    