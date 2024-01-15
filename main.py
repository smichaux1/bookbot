def main():
    book_path = "books/frankenstein.txt"
    book_text = read_book(book_path)
#    print(book_text)
    w_count = count_words(book_text)
#    print (f"word count is {w_count}")
    l_count = count_letters(book_text)
#    print(l_count)
    print_report(book_path,w_count,l_count)
    
def read_book(book):  
    with open(book) as f:
        return f.read()
    
def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letter_count = {}
    ltext = text.lower()
    for letter in ltext:
        if (letter in letter_count) and letter.isalpha():
            letter_count[letter] += 1
        elif letter.isalpha():
            letter_count[letter] = 1
    return letter_count

def print_report(path, count, dictionary):
    letter_list = list(dictionary.items())
    letter_list.sort(key=lambda x: x[1], reverse=True)
    print(f"--- Begin report of {path} ---\n\n{count} words found in the document\n")
 
    for x in range(0,len(letter_list)):
        print(f"The '{letter_list[x][0]}' character was found {letter_list[x][1]} times")
    print("--- End report ---")

main()