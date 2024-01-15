def main():
    book_text = read_book("books/frankenstein.txt")
    print(book_text)
    w_count = count_words(book_text)
    print (f"word count is {w_count}")
    l_count = count_letters(book_text)
    print(l_count)
    
def read_book(book):  
    with open(book) as f:
        return f.read()
    
def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letter_count = {}
    for letter in text:
        if letter.lower() in letter_count:
            letter_count[letter.lower()] += 1
        else:
            letter_count[letter.lower()] = 1
    return letter_count

main()