def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letters_dict = get_letters_dict(text)
    sorted_list = get_book_sort(letters_dict)
    print(f"""
--- Begin report of {book_path} ---
{num_words} words found in the document
""")
    
    for item in sorted_list:
        if item["letter"].isalpha():
            print(f"The {item['letter']} character was found {item['num']} times")
    
    print ("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_letters_dict(text):
    letters = {}
    for letter in text:
        lowered = letter.lower()
        if lowered in letters:
            letters[lowered] += 1
        else:
            letters[lowered] = 1
    return letters


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_book_sort(letter_dict):
    sort_list = []
    for letter in letter_dict:
        sort_list.append({"letter": letter, "num": letter_dict[letter]})
    sort_list.sort(reverse=True, key=sort_on)
    return sort_list

def sort_on(dict):
    return dict["num"]

main()
